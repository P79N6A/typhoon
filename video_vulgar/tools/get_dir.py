import csv
import os

if __name__ == "__main__":
    score_dir = '/mnt/cephfs_wj/vc/wangxiyu/data/unified_vulgar/gen_test.csv'
    tager_dir = '/mnt/cephfs_wj/vc/wangxiyu/data/unified_vulgar/dir.txt'

    read1 = csv.reader(open(score_dir, 'r'))

    dirs = []
    for read in read1:
        dirs.append(read[-1])

    with open(tager_dir, 'w') as f:
        for rsp in dirs:
            f.write("%s\n" % rsp)