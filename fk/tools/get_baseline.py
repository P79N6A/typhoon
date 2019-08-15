#encoding: utf-8
import sys
import csv
import os
import matplotlib
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':

    zheng_dir = '/Users/ounozomiyo/Desktop/data/Qtest/Qzheng_500.csv'
    fu_dir = '/Users/ounozomiyo/Desktop/data/Qtest/Qfu_test.csv'

    fenshu_dir = '/Users/ounozomiyo/Desktop/data/Qtest/out.csv'

    writer = csv.writer(open(r"/Users/ounozomiyo/Desktop/data/Qtest/Q.csv", 'w'))

    users = {}

    zheng_txts = csv.reader(open(zheng_dir, "r"))
    fu_txts = csv.reader(open(fu_dir, "r"))

    for zheng in zheng_txts:
        users[zheng[0]] = [zheng[0], zheng[1], 1]

    for fu in fu_txts:
        users[fu[0]] = [fu[0], fu[1], 0]

    print len(users)

    test_zheng_txts = csv.reader(open(fenshu_dir, "r"))
    for line in test_zheng_txts:
        id = line[0].split('\t')[0]
        fenshu = line[0].split('\t')[2]
        id = id.split('/')[-1].split('.')[0]

        users[id].append(float(fenshu))


    zheng_dir = '/Users/ounozomiyo/Desktop/data/Qtest/Qzheng.csv'
    fu_dir = '/Users/ounozomiyo/Desktop/data/Qtest/Qfu.csv'
    zheng_txts = csv.reader(open(zheng_dir, "r"))
    fu_txts = csv.reader(open(fu_dir, "r"))

    ###生成
    re_pre_fenshu = []
    recalls = []
    precisions = []

    for i in range(1, 100, 1):
        tp = 0
        fn = 0
        fp = 0
        for user in users.values():
            if user[2] == 1 and user[3] >= i*0.01:
                tp += 1
            elif user[2] == 0 and user[3] >= i*0.01:
                fp += 1
            elif user[2] == 1 and user[3] < i*0.01:
                fn += 1

        recall = tp * 1.0 / (tp+fn)
        precision = tp * 1.0 / (tp+fp)
        recalls.append(recall)
        precisions.append(precision)
        #print "tp: ", tp, "fp: ", fp, "fn: ", fn
        print "recall: ", recall, "    precision: ", precision, "      threshold: ", i*0.01

        re_pre_fenshu.append([recall, precision, i*0.01])

    precisions = np.array(precisions)
    recalls = np.array(recalls)

    ### 画图
    plt.figure(1)
    plt.xlim(0, 1)
    plt.ylim(0, 1)

    plt.xlabel('recall')
    plt.ylabel('pre')

    plt.plot(precisions, recalls, label=u"RP曲线")
    #plt.show()



    zhengs = {}
    fus = {}
    for zheng in zheng_txts:
        zhengs[zheng[0]] = zheng[1]
    for fu in fu_txts:
        fus[fu[0]] = fu[3]

    lis = users.values()
    # print lis
    lis.sort(key=lambda x: x[3], reverse=True)

    for li in lis:
        if li[0] in zhengs.keys():
            li[1] = zhengs[li[0]]
        if li[0] in fus.keys():
            li[1] = fus[li[0]]
        writer.writerow(li)
    # print lis





