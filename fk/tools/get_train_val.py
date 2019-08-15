import os
import csv
import random

fu_dir = "/Users/ounozomiyo/Desktop/data/f"
zheng_dir = "/Users/ounozomiyo/Desktop/data/z"

train_w = csv.writer(open(r"/Users/ounozomiyo/Desktop/data/train.csv", 'w'))
val_w = csv.writer(open(r"/Users/ounozomiyo/Desktop/data/val.csv", 'w'))

count = 0

train_lines = []
val_lines = []

lines = []

dir = "/mnt/cephfs/lab/wangxiyu/data/fk_img_lab/"

for line in os.listdir(fu_dir):
    lines.append([os.path.join(dir + 'f', line), 0])
for line in os.listdir(zheng_dir):
    lines.append([os.path.join(dir + 'z', line), 1])

random.shuffle(lines)

num = len(lines)

train_lines = lines[num//4:]
val_lines = lines[:num//4]


for line in train_lines:
    train_w.writerow(line)

for line in val_lines:
    val_w.writerow(line)

print("suss!!!")
