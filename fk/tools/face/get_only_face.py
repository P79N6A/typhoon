#encoding: utf-8
import csv

read_face_dir1 = 'csvs_out/val_output_positive.csv'
read_face_dir2 = 'csvs_out/val_output_random.csv'

read_dir = '/Users/ounozomiyo/Desktop/公司/data/fk_img_lab/csvs/val_positive.csv'
write_dir = 'val_only_face_positive.csv'

read_file1 = csv.reader(open(read_face_dir1, 'r'))
read_file2 = csv.reader(open(read_face_dir2, 'r'))

read_dir_file = csv.reader(open(read_dir, 'r'))

train_w = csv.writer(open(write_dir, 'w'))

lines = []
for line in read_file1:
    if line[2] == '0':
        lines.append(line[0])

for line in read_file2:
    if line[2] == '0':
        lines.append(line[0])

for line in read_dir_file:
    if line[0] in lines:
        train_w.writerow(line)

print 'suss!'