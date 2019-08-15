#encoding: utf-8
import numpy as np
import requests as req
from PIL import Image
import urllib
import random
import shutil
import csv
import os

root_dir = "/Users/ounozomiyo/Desktop/company/data/fk_img_lab/feiliao/"

read_r = csv.reader(open(os.path.join(root_dir, 'random_feiliao_5000.csv'), 'r'))
random_w = csv.writer(open(os.path.join(root_dir, 'random_feiliao_pre.csv'), 'w'))

pos_num = 0
for i, line in enumerate(read_r):
    if line[3] == '1':
        pos_num += 1
        print pos_num*1.0/(i+1), line[2]

        random_w.writerow([pos_num*1.0/(i+1), line[2]])
print("suss!!!")