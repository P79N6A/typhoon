import csv
import os

if __name__ == "__main__":
    dir1 = '/mnt/cephfs_wj/vc/wangxiyu/data/video_vulgar/test/vulgar_test.csv'

    dir2 = '/mnt/cephfs_wj/vc/wangxiyu/data/video_vulgar/test/data/resnet101_5.16_pre_sgd_13pos.csv'

    dir4 = '/mnt/cephfs_wj/vc/wangxiyu/data/video_vulgar/test/data/url_score.csv'

    read1 = csv.reader(open(dir1, 'r'))
    read2 = csv.reader(open(dir2, 'r'))

    write_jinshen_pre = csv.writer(open(dir4, 'w'))

    urls = {}
    for read in read1:
        image = read[0].split('/')[-1]
        urls[image] = read[0]

    for line in read2:
        if line[0] in urls.keys():
            write_jinshen_pre.writerow([urls[line[0]], float(line[1])])