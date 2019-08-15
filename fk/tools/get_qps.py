#encoding: utf-8
import csv
import os

root_dir = "/mnt/cephfs/lab/wangxiyu/tag_1_normalization/audit_utils-master/predict_utils/"
train_w = os.path.join(root_dir, 'in.txt')

dir = '/mnt/cephfs/lab/wangxiyu/data/fk_img_lab/val/1/99999397599.jpg'

with open(train_w, 'w') as f:
    for i in range(50000):
        f.write(dir+'\n')

print("suss!!!")
