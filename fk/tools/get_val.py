#encoding: utf-8
import numpy as np
import requests as req
from PIL import Image
import urllib
import random
import shutil
import csv
import os

count = 0

train_1_dir = '/Users/ounozomiyo/Desktop/data/train/1'
train_0_dir = '/Users/ounozomiyo/Desktop/data/train/0'

val_1_dir = '/Users/ounozomiyo/Desktop/data/val/1'
val_0_dir = '/Users/ounozomiyo/Desktop/data/val/0'

train_vars = []
val_vars = []

for line in os.listdir(train_1_dir):
    train_vars.append(line.split('.')[0])
for line in os.listdir(train_0_dir):
    train_vars.append(line.split('.')[0])

for line in os.listdir(val_1_dir):
    val_vars.append(line.split('.')[0])
for line in os.listdir(val_0_dir):
    val_vars.append(line.split('.')[0])

print len(train_vars), len(val_vars)
print len(set(train_vars)), len(set(val_vars))

test_list = list(set(train_vars) & set(val_vars))

print test_list

test = csv.reader(open(r"/Users/ounozomiyo/Desktop/data/val/test.csv", "r"))
test_zhen = csv.writer(open(r"/Users/ounozomiyo/Desktop/data/test_zhen.csv", "w"))

for line in test:
    if line[0] not in test_list:
        test_zhen.writerow(line)
    else:
        file_dir = os.path.join(val_1_dir, line[0] + ".jpg")
        if os.path.exists(file_dir):
            os.remove(file_dir)
        file_dir = os.path.join(val_0_dir, line[0] + ".jpg")
        if os.path.exists(file_dir):
            os.remove(file_dir)


print len(set(train_vars) & set(val_vars))
print("suss!!!")
