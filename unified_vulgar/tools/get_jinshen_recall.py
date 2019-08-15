import csv
import numpy as np
import os

root_dir = '/Users/ounozomiyo/Desktop/company/data/video_vulgar/test'

random_dir = 'url_score_random_nopad.csv'
positive_dir = 'url_score_pos_nopad.csv'

out_file = 'jinshen_nopad.csv'

out_write = csv.writer(open(os.path.join(root_dir, out_file), 'w'))

randoms = []
positives = []

# with open(os.path.join(root_dir, random_dir)) as f:
#     for line in f:
#         randoms.append(float(line.strip().split('\t')[1]))
#
# with open(os.path.join(root_dir, positive_dir)) as f:
#     for line in f:
#         positives.append(float(line.strip().split('\t')[1]))

random_read = csv.reader(open(os.path.join(root_dir, random_dir), 'r'))
positive_read = csv.reader(open(os.path.join(root_dir, positive_dir), 'r'))

for line in random_read:
    randoms.append(float(line[2]))

for line in positive_read:
    #if line[3] == '1':
    positives.append(float(line[2]))

print len(randoms)
print len(positives)

print positives

ratios = [i * 0.001 for i in range(1, 1000, 1)]

randoms.sort()
print len(randoms)

for ratio in ratios:

    thres = randoms[int(len(randoms) * (1 - ratio))]
    recall_nums = sum(np.array(positives) >= thres)

    out_write.writerow([thres, float('%.4f' % ratio), float(recall_nums) / len(positives)])

    print "Thres: %f, Ratio: %f, Recall: %f" % (float('%.4f' % thres), float('%.4f' % ratio), float(recall_nums) / len(positives))