import csv
import os

if __name__ == "__main__":
    dir1 = '/Users/ounozomiyo/Desktop/company/data/video_vulgar/test/resnet_fpn_101_xigua_9pos_nopad.csv'

    dir2 = '/Users/ounozomiyo/Desktop/company/data/video_vulgar/test/url_score_pos.csv'

    dir4 = '/Users/ounozomiyo/Desktop/company/data/video_vulgar/test/url_score_pos_nopad.csv'

    read1 = csv.reader(open(dir1, 'r'))
    read2 = csv.reader(open(dir2, 'r'))

    write_jinshen_pre = csv.writer(open(dir4, 'w'))

    scores = {}

    for line in read1:
        scores[line[0]] = float(line[1])


    for line in read2:
        if line[0] in scores.keys():
            write_jinshen_pre.writerow([line[0], line[1], scores[line[0]], line[3]])