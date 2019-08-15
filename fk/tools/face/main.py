import os, sys
import numpy as np
import cv2
import utils
import time
from pyutil.thrift.thrift_client import ThriftRetryClient
from video_frame_cut_client import VideoFrameCutProcessor

sys.path.insert(0, './thrift/gen-py')
from face_predict import FacePredict
from face_predict.ttypes import *
from base.ttypes import *
from functools import partial
import multiprocessing as mp
import argparse

b = Base(Caller='lirixi.local')

result_queue = mp.Queue()

lst_path = '/home/lirixi/cephfs2/Data/musical/m20181101-20190120/tcs/labeled/lst/m20181101-20190120_part00-01_video_label3_b.lst'
save_path = '/home/lirixi/cephfs2/results/age/m20181101-20190120_part00-01_video_label3_b/merge_4f_0.txt'

result_queue = mp.Queue()

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
    line = line.strip().split('\t')
    label = line[1]
    url = line[2]
    vid = url.split('=')[-1]    
    try:
        frame_cut_client = VideoFrameCutProcessor('toutiao.videoarch.vframe.service.maliva.byted.org', need_binary=True)
        frames = frame_cut_client.process_video_id(vid, "num:4")
        print len(frames)
        #frames = [frames[1], frames[3], frames[4], frames[6]]

        client = FacePredictor(service_name, servers)

        resp = client.predict(frames, b)

        level = resp.predict_results[0].face_level.tag_id
        gender = resp.predict_results[0].face_gender.tag_id
        race = resp.predict_results[0].face_race.tag_id

        wline = '{}\t{}\t{}\t{}\t{}\t{}\n'.format(vid, url, label, level, gender, race)
        result_queue.put(wline)
        print resp
    except Exception, e:
        print 'process error', e


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--lst_path', type=str, default=lst_path)
    parser.add_argument('--save_path', type=str, default=save_path)
    args = parser.parse_args()
    service_name = 'lab.face_attr.muse.service.maliva.byted.org'

    with open(args.lst_path, 'r') as f:
        content = f.readlines()

    #fw = open(save_path, 'w')
    writer = mp.Process(target=write_to_file, args=(args.save_path,))
    writer.start()

    pool = mp.Pool(5)
    process = partial(process_image, service_name=service_name, servers=None)
    #process = partial(process_image, service_name=None, servers=[('10.110.238.189', 9285)])
    pool.map(process, content)
    pool.close()
    pool.join()
    result_queue.put(None)
    writer.join()
