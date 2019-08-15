#encoding: utf-8
import numpy as np
import requests as req
from PIL import Image
import urllib
import random
import shutil
import csv
import os


root_dir = '/mnt/cephfs_wj/vc/wangxiyu/data/fk_img_lab/csvs'
train_w = csv.writer(open(os.path.join(root_dir, 'val_random_10w.csv'), 'w'))

count = 0

test_lines = []

fu_dir = 'face/in_img.csv'

random_face = csv.reader(open(fu_dir, "r"))

for line in random_face:
    train_w.writerow([line[0], 0, line[1]])

print("suss!!!")
