import cv2
import csv

dir1 = '/Users/ounozomiyo/Desktop/gen_test.csv'
dir2 = '/Users/ounozomiyo/Desktop/resnet_fpn_101_0.csv'

dir3 = '/Users/ounozomiyo/Desktop/score_pos.csv'
dir4 = '/Users/ounozomiyo/Desktop/score_fu.csv'

read_1 = csv.reader(open(dir1, 'r'))
read_2 = csv.reader(open(dir2, 'r'))

write_pos = csv.writer(open(dir3, 'w'))
write_fu = csv.writer(open(dir4, 'w'))

score = {}
for line in read_2:
    score[line[0]] = float(line[1])

print len(score.keys())

for line in read_1:
    if line[0] in score.keys():
        if line[2] == '1':
            write_pos.writerow([line[0], line[1], score[line[0]]])
        else:
            write_fu.writerow([line[0], line[1], score[line[0]]])

print 'suss'