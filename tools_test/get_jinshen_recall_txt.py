import csv
import numpy as np
import os

root_dir = '/mnt/cephfs/lab/wangxiyu/test/'

random_dir = 'result_porn_random.csv'
positive_dir = 'result_porn.csv'

randoms = []
positives = []

# with open(os.path.join(root_dir, random_dir)) as f:
#     for line in f:
#         randoms.append(float(line.strip().split('\t')[1]))
#
# with open(os.path.join(root_dir, positive_dir)) as f:
#     for line in f:
#         positives.append(float(line.strip().split('\t')[1]))

pos_file = csv.reader(open(os.path.join(root_dir, positive_dir), 'r'))
random_file = csv.reader(open(os.path.join(root_dir, random_dir), 'r'))

for line in pos_file:
    if line and line[0].split('\t')[1] != '':
        positives.append(float(line[0].split('\t')[-1]))

for line in random_file:
    #print line, line[0].split('\t')[-1]
    if line:
        randoms.append(float(line[0].split('\t')[-1]))

out_file = os.path.join(root_dir, 'porn_jinshen.csv')
out_write = csv.writer(open(os.path.join(root_dir, out_file), 'w'))

print len(randoms)
print len(positives)

ratios = [i * 0.001 for i in range(1, 1000, 1)]

randoms.sort()

for ratio in ratios:

    thres = randoms[int(len(randoms) * (1 - ratio))]
    recall_nums = sum(np.array(positives) >= thres)

    out_write.writerow([float('%.4f' % thres), float('%.4f' % ratio), float(recall_nums) / len(positives)])

    print "Thres: %f, Ratio: %f, Recall: %f" % (float('%.4f' % thres), float('%.4f' % ratio), float(recall_nums) / len(positives))