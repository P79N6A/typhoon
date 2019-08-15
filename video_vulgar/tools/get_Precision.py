import csv
import os
import matplotlib.pyplot as plt

if __name__ == "__main__":
    dir1 = '/Users/ounozomiyo/Desktop/company/data/video_vulgar/test/url_score_random_nopad.csv'

    dir2 = '/Users/ounozomiyo/Desktop/company/data/video_vulgar/test/jinshen_nopad.csv'

    read1 = csv.reader(open(dir1, 'r'))
    read2 = csv.reader(open(dir2, 'r'))

    dir4 = '/Users/ounozomiyo/Desktop/company/data/video_vulgar/test/ratio_pre_recall_nopad.csv'

    write_jinshen_pre = csv.writer(open(dir4, 'w'))

    urls = {}
    for read in read1:
        score = float(read[2])
        label = int(read[3])
        urls[read[0]] = [score, label]

    x = []
    y = []
    for read in read2:
        thres = float(read[0])
        ratio = float(read[1])
        recall = float(read[2])

        print thres

        pos_num = 0
        neg_num = 0
        for score, label in urls.values():
            if thres <= score:
                if label == 1:
                    pos_num += 1
                else:
                    neg_num += 1

        print neg_num, pos_num

        precision = pos_num*1.0 / (neg_num+pos_num)
        y.append(precision)
        x.append(recall)

        print('thres:', thres, 'ratio:', ratio, 'recall:', recall, 'precision:', precision)
        write_jinshen_pre.writerow([thres, ratio, recall, precision])

    fig, ax_label = plt.subplots()

    ax_label.scatter(x, y, c='r')

    for i, txt in enumerate(x):
        ax_label.annotate(' ', (x[i], y[i]))
    plt.show()
