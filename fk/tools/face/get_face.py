#encoding: utf-8
import sys
sys.path.append('./gen-py/')
import argparse
import threading
import random
import logging
import cv2
import time

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

from pyutil.consul.bridge import translate_one
from pyutil.thrift.thrift_client import ThriftRetryClient
from base.ttypes import *
from face_predict import FacePredict
from face_predict.ttypes import ImagesPredictReq, ImageInfo, VideoPredictReq


def parse_args():
    p = argparse.ArgumentParser(description='face pre get gender and race and level.')

    p.add_argument('--service_name', default='lab.face_attr.muse.service.maliva.byted.org')
    p.add_argument('--port', type=int)
    p.add_argument('--ip')
    p.add_argument('--list')
    p.add_argument('--num_processes', type=int, default=1)
    p.add_argument('--url', type=str, default='in_img.csv')
    p.add_argument('--output')
    p.add_argument('--type', default="img_dir", choices=["video_id", "url", "json", "img_dir"])
    p.add_argument('--frames_params', default="num:8", choices=["num:8", "num:5", "fps:0.6", "fps:1", "fps:2", "scenecut"])
    p.add_argument('--using_image_interface', action='store_true')
    p.add_argument('--frame_dc', default="lf", choices=['lf', 'alisg', 'maliva', 'lftest', 'all'])
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


if __name__ == "__main__":
    try:
        b = Base(Caller='lirixi.local')
        args = parse_args()
        service_name = args.service_name
        service_type = args.type
        ip = args.ip
        port = args.port

        # if service_name:
        #     client = ThriftProcessor(service_name)
        # else:
        #     client = ThriftProcessor(ip=ip, port=port)

        print service_name

        if service_type == 'img_dir':
            img_dir = args.url
            images_bin = []

            with open(img_dir) as f:
                lines = [line.strip() for line in f]

            for url in lines:
                image_info = ImageInfo()
                with open(url.strip()) as f:
                    data = f.read()
                    images_bin.append(data)

            print len(images_bin)

            client = FacePredictor(service_name, servers=None)
            rsp = client.predict(images_bin, b)

            print "!!!", rsp.predict_results

            print "@@@", rsp.BaseResp

            level = rsp.predict_results[0].face_level.tag_id   #年龄等级：
                                                               #0-2 0
                                                               #3-14 1
                                                               #15-17 2
                                                               #18-20 3
                                                               #21+ 4
            gender = rsp.predict_results[0].face_gender.tag_id #性别 M:男 F:女
            race = rsp.predict_results[0].face_race.tag_id     #种族

            print "@@@", rsp.BaseResp.Extra['faces']

            print "!!!", level, gender, race

        # for predict_result in rsp.predict_results:
        #     print predict_result.face_level
        #     print predict_result.face_gender
        #     print predict_result.face_race

    except Thrift.TException, ex:
        print "%s" % (ex.message)