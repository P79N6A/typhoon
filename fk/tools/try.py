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

train_w = csv.writer(open(os.path.join(root_dir, 'feiliao_url.csv'), 'w'))

url_file = csv.reader(open(os.path.join(root_dir, 'random.csv'), "r"))

score_file = os.path.join(root_dir, 'out_random.txt')

lines = {}

for line in url_file:
    url = 'http://p1.feiliao.com/img/' + line[0] + '~noop.jpg'
    lines[url.split('/')[-1]] = url

with open(score_file) as f:
    for line in f:
        name = line.strip().split('\t')[0].split('/')[-1]
        score = line.strip().split('\t')[2]

        if name in lines.keys():

            train_w.writerow([lines[name], score])

print 'num: ', len(lines)
