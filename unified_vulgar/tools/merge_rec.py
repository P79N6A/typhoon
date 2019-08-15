import mxnet as mx
import csv
import os
import time
import cv2
import numpy as np
import shutil
from random import shuffle

def mycopyfile(srcfile, dstfile):
    if not os.path.isfile(srcfile):
        print "%s not exist!" % (srcfile)
    else:
        fpath, fname = os.path.split(dstfile)
        if not os.path.exists(fpath):
            os.makedirs(fpath)
        shutil.copyfile(srcfile, dstfile)
        print "copy %s -> %s" % (srcfile, dstfile)

if __name__ == "__main__":
    root_dir = '/mnt/cephfs_wj/vc/wangxiyu/data/unified_vulgar/'

    train_read = csv.reader(open(os.path.join(root_dir, 'train.csv'), 'r'))

    id = 0
    pre_time = time.time()

    rec_dirs = []
    for line in train_read:
        dir = line[0]
        for file_name in os.listdir(dir):
            if file_name.endswith('.rec'):
                dir_name = file_name.split('.')[0]
                pref = os.path.join(dir, dir_name)
                rec_dirs.append(pref)

    print len(rec_dirs)

    shuffle(rec_dirs)
    for pref in rec_dirs:
        print "start read ", pref
        imgrec = mx.recordio.MXIndexedRecordIO(pref + ".idx", pref + ".rec", 'r')
        for imgidx in imgrec.keys:
            if id % 1000000 == 0:
                cur_time = time.time()
                if id != 0:
                    print "end write: ", rec_name
                rec_name = "general_1" + str(id // 1000000)
                rec_write = mx.recordio.MXIndexedRecordIO(os.path.join(root_dir, rec_name + ".idx"),
                                                          os.path.join(root_dir, rec_name + ".rec"), 'w')
                print 'time:', cur_time - pre_time, ' count:', id
                print "start write: ", rec_name
                pre_time = cur_time

            s = imgrec.read_idx(imgidx)
            header, img = mx.recordio.unpack(s)

            img = cv2.imdecode(np.array(bytearray(img)), cv2.IMREAD_COLOR)



            header = mx.recordio.IRHeader(0, float(header.label), id % 1000000, 0)
            s = mx.recordio.pack_img(header, img)

            rec_write.write_idx(id % 1000000, s)
            id += 1


    # mycopyfile('./general.idx', os.path.join(root_dir, 'general.idx'))
    # mycopyfile('./general.rec', os.path.join(root_dir, 'general.rec'))
    print "suss!!!", id









