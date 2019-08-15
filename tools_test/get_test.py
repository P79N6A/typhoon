#encoding: utf-8
import numpy as np
import requests as req
from PIL import Image
import urllib
import random
import shutil
import csv
import os

root_dir = "/mnt/cephfs_wj/vc/wangxiyu/data/video_vulgar/test/data/"

targer_dir = "/mnt/cephfs_wj/vc/wangxiyu/data/fk_img_lab/unified_vulgar/"

random_d = os.path.join(root_dir, 'test_images')
#pos_d = os.path.join(root_dir, 'pos')

#pos_w = csv.writer(open(os.path.join(root_dir, 'pos_feiliao.csv'), 'w'))
random_w = csv.writer(open(os.path.join(root_dir, 'random_video_test.csv'), 'w'))

count = 0

test_pos = []
test_random = []

# for line in os.listdir(pos_d):
#     test_pos.append([line.split('.')[0], 1, os.path.join(targer_pos, line)])
    #test_pos.append([os.path.join(zheng_d, line)])
for line in os.listdir(random_d):
    test_random.append([line.split('.')[0], 0, os.path.join(random_d, line)])
    #test_random.append([os.path.join(fu_d, line)])

random.shuffle(test_pos)
random.shuffle(test_random)

print len(test_pos)
print len(test_random)

# for i, line in enumerate(test_pos):
#     pos_w.writerow(line)

for i, line in enumerate(test_random):
    random_w.writerow(line)

print("suss!!!")
