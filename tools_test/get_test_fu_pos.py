#encoding: utf-8
import numpy as np
import requests as req
from PIL import Image
import urllib
import random
import shutil
import csv
import os

root_dir = "/mnt/cephfs_wj/vc/wangxiyu/data/unified_vulgar/test/gen/"

targer_dir = "/mnt/cephfs_wj/vc/wangxiyu/data/unified_vulgar/"

random_w = csv.writer(open(os.path.join(targer_dir, 'gen_test.csv'), 'w'))

count_pos = 0
count_fu = 0

test_list = []

for folder_name in os.listdir(root_dir):
    folder_dir = os.path.join(root_dir, folder_name)
    for file_name in os.listdir(folder_dir):
        if folder_name.split('_')[1] == 'pos':
            label = 1
            count_pos += 1
        else:
            label = 0
            count_fu += 1
        test_list.append([file_name.split('.')[0], folder_name, label, os.path.join(folder_dir, file_name)])

random.shuffle(test_list)

print len(test_list), count_pos, count_fu


for i, line in enumerate(test_list):
    random_w.writerow(line)

print("suss!!!")
