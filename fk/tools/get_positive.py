#encoding: utf-8
import numpy as np
import requests as req
from PIL import Image
import urllib
import random
import shutil
import csv
import os

root_dir = "/Users/ounozomiyo/Desktop/公司/data/fk_img_lab/val"

zheng_d = os.path.join(root_dir, '1')

positive_w = csv.writer(open(os.path.join(root_dir, 'train_positive.csv'), 'w'))

count = 0

test_lines = []

zheng_dir = '/mnt/cephfs_wj/vc/wangxiyu/data/fk_img_lab/val/1'

for line in os.listdir(zheng_d):
    test_lines.append([line.split('.')[0], 1, os.path.join(zheng_dir, line)])

random.shuffle(test_lines)

for line in test_lines:
    positive_w.writerow(line)

print("suss!!!")
