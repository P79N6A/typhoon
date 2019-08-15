# -*- coding: UTF-8 -*-
import mxnet as mx
import argparse
import PIL.Image
import io
import numpy as np
#import cv2
#import tensorflow as tf
import os
from mxnet import ndarray as nd
#import matplotlib.pyplot

def parse_args():
    dir = "/mnt/cephfs_wj/vc/common/rhea/datasets/b004490e-1008-4a3f-8eb8-bbd04956bdc6"

    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description='data path information'
    )
    parser.add_argument('--bin_path', default=os.path.join(dir, 'xaa.rec'), type=str,
                        help='path to the binary image file')
    parser.add_argument('--idx_path', default=os.path.join(dir, 'xaa.idx'), type=str,
                        help='path to the image index path')
    parser.add_argument('--tfrecords_file_path', default=dir, type=str,
                        help='path to the output of tfrecords file path')
    args = parser.parse_args()
    return args

def getPicFromRec(imgidx, imgrec, args):
    output_path = os.path.join(args.tfrecords_file_path, 'tran.tfrecords')    
    sameLabelPicCount=0
    for i in imgidx:
        img_info = imgrec.read_idx(i)
        header, img = mx.recordio.unpack(img_info)
        label = int(header.label)
        imgDir = os.path.join('/work/dataSet/faces_ms1m_112x112', str(label))
        
        if not os.path.exists(imgDir):
            os.makedirs(imgDir)
            sameLabelPicCount=0
        #生成文件名
        file_name = str(imgDir + "/" + str(str(label) + '_' + str(sameLabelPicCount) + ".jpg"))
        sameLabelPicCount += 1
        #保存文件
        
        img = mx.image.imdecode(img)
        img = nd.transpose(img, axes=(2, 0, 1))       
        for index in range(1):
            a = img
            #得到RGB通道  
            arr1 = a[0].asnumpy()
            r = PIL.Image.fromarray(arr1).convert('L')  
            arr2 = a[1].asnumpy()
            g = PIL.Image.fromarray(arr2).convert('L')  
            arr3 = a[2].asnumpy()
            b = PIL.Image.fromarray(arr3).convert('L')  
            image = PIL.Image.merge("RGB",(r,g,b))  
            #显示图片  
            #matplotlib.pyplot.imshow(image)  
            #matplotlib.pyplot.show()  
            image.save(file_name, 'png')
        if i % 10000 == 0:
            print('%d num image processed' % i)


if __name__ == '__main__':
    # # define parameters   
    id2range = {}
    data_shape = (3, 224, 224)
    args = parse_args()

    imgrec = mx.recordio.MXIndexedRecordIO(args.idx_path, args.bin_path, 'r')

    s = imgrec.read_idx(0)
    header, _ = mx.recordio.unpack(s)
    print(header)
    print(header.label)

    imgidx = list(range(1, int(header.label[0])))

    seq_identity = range(int(header.label[0]), int(header.label[1]))
    for identity in seq_identity:
        s = imgrec.read_idx(identity)
        header, _ = mx.recordio.unpack(s)
        a, b = int(header.label[0]), int(header.label[1])
        id2range[identity] = (a, b)
    print('id2range', len(id2range))

    # # generate tfrecords
    getPicFromRec(imgidx, imgrec, args)