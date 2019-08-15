#encoding: utf-8
import sys
sys.path.append('./gen-py/')
import argparse
import threading
import random
import logging
import cv2
import time
import csv
import numpy as np
import os
from thrift import Thrift
import multiprocessing as mp
from functools import partial

from pyutil.thrift.thrift_client import ThriftRetryClient
from base.ttypes import *
from face_predict import FacePredict
from face_predict.ttypes import ImagesPredictReq, ImageInfo, VideoPredictReq

b = Base(Caller='lirixi.local')
result_queue = mp.Queue()

read_queue = []
i = 0

def parse_args():
    p = argparse.ArgumentParser(description='face pre get gender and race and level.')
    p.add_argument('--service_name', default='lab.face_attr.muse.service.maliva.byted.org')
    p.add_argument('--input', type=str, default='in_img.csv')
    p.add_argument('--output', type=str, default='fu_output_random.csv')
    return p.parse_args()


class FacePredictor():
    def __init__(self, service_name=None, servers=None):
        self.client = ThriftRetryClient(FacePredict.Client,
                                        servers=servers, \
                                        consul_name=service_name, \
                                        nonblocking_server=False,
                                        timeout=10, \
                                        conn_timeout=5, max_retries=2)
        self.service_name = service_name

    def predict(self, image_data, b):
        images = [ImageInfo(image_data=x) for x in image_data]

        req = FacePredict.VideoPredictReq(frames=images,
                                          need_level=True,
                                          need_gender=True,
                                          need_race=True,
                                          Base=b)
        try:
            st = time.time()
            resp = self.client.PredictVideo(req)
            print('face predict succes.', time.time() - st, 's')
        except Exception, e:
            print 'predict error', e
            return None
        return resp


def write_to_file(result_path):
    global result_queue
    result = open(result_path, 'a')
    while True:
        line = result_queue.get()
        if line != None:
            result.write(line)
        else:
            break
    result.close()


def process_image(line, service_name, servers):

    try:
        global i
        line = line[1]
        file_name = line[0]
        images_bin = []
        with open(line) as f:
            data = f.read()
            images_bin.append(data)

        client = FacePredictor(service_name, servers)
        rsp = client.predict(images_bin, b)

        if rsp is not None and len(rsp.predict_results) > 0:
            level = rsp.predict_results[0].face_level.tag_id
            gender = rsp.predict_results[0].face_gender.tag_id
            race = rsp.predict_results[0].face_race.tag_id
            faces = rsp.BaseResp.Extra['faces']

            print i, [file_name, str(level), str(gender), str(race), str(faces)]

            result_queue.put([file_name, str(level), str(gender), str(race), str(faces)])

        i += 1
    except Exception, e:
        print 'process error', e


if __name__ == "__main__":
    try:
        exist = []
        args = parse_args()
        service_name = args.service_name

        if os.path.exists(args.output):
            read_file = csv.reader(open(args.output, 'r'))
            for line in read_file:
                exist.append(line[0])

        read_file = csv.reader(open(args.input, 'r'))
        client = FacePredictor(service_name, servers=None)
        i = 0

        for line in read_file:
            file_dir = line[2]
            file_name = line[0]
            if file_name not in exist:
                read_queue.append([file_name, file_dir])

        print 'num:', len(read_queue)

        writer = mp.Process(target=write_to_file, args=(args.output,))
        writer.start()

        pool = mp.Pool(10)
        process = partial(process_image, service_name=service_name, servers=None)
        # process = partial(process_image, service_name=None, servers=[('10.110.238.189', 9285)])
        pool.map(process, read_queue)
        pool.close()
        pool.join()
        result_queue.put(None)
        writer.join()

    except Thrift.TException, ex:
        print "%s" % (ex.message)