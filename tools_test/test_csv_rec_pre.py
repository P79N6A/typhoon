#encoding: utf-8
import sys
import os
import numpy as np
import csv
from sklearn.metrics import roc_auc_score


def auc(score_dic, keys, name=None):
    labels = []
    preds = []
    for key in keys:
        labels.append(score_dic[key][1])
        preds.append(score_dic[key][0])

    y_true = np.array(labels)
    y_scores = np.array(preds)

    return "AUC", name, roc_auc_score(y_true, y_scores)



def get_recall_pre(score_dic, keys, name=None):
    max_f1 = 0
    the = 0
    for i in range(1, 100, 1):
        tp_num = 0
        fn_num = 0
        fp_num = 0
        for key in keys:
            #print score_dic[key][2]
            label = score_dic[key][1]
            pred_label = score_dic[key][0]
            bin1 = (pred_label >= i*0.01)
            bin2 = (label == 1)
            tp = np.sum(bin1 * bin2)
            tp_num += tp
            fn_num += (np.sum(bin2) - tp)
            fp_num += (np.sum(bin1) - tp)
        recall = tp_num * 1.0 / (tp_num + fn_num)
        precison = tp_num * 1.0 / (tp_num + fp_num)
        f1 = 2 * recall * precison / (recall + precison)

        if max_f1 < f1:
            max_f1 = f1
            the = i * 0.01

        # print(name + "_recall:", recall,
        #       " precision:", precison,
        #       " F1:", f1,
        #       " threshold:", i * 0.01)
    print(name + "_MAX_F1:", max_f1, 'the:', the)


def get_recall(score_dic, keys, score=0.5, name=None):
    tp_num = 0
    fn_num = 0
    fp_num = 0
    for key in keys:
        #print score_dic[key][2]
        label = score_dic[key][1]
        pred_label = score_dic[key][0]
        bin1 = (pred_label >= score)
        bin2 = (label == 1)
        tp = np.sum(bin1 * bin2)
        tp_num += tp
        fn_num += (np.sum(bin2) - tp)
        fp_num += (np.sum(bin1) - tp)
    recall = tp_num * 1.0 / (tp_num + fn_num)
    precison = tp_num * 1.0 / (tp_num + fp_num)
    print(name + "_recall: ", round(recall, 4),
          " precision: ", round(precison, 4),
          " F1:", round(2 * recall * precison / (recall + precison), 4),
          " threshold: ", round(score, 4))


if __name__ == "__main__":
    for i in range(1, 2, 1):
        print 'start: ', i
        score_dir = '/mnt/cephfs/lab/wangxiyu/data/resnet_fpn_101_6_27_' + str(i) + '.csv'
        file_dir = '/mnt/cephfs/lab/wangxiyu/data/gen_test.csv'
        score = csv.reader(open(score_dir, 'r'))
        file = csv.reader(open(file_dir, 'r'))

        txt_score = '/mnt/cephfs/lab/wangxiyu/data/baseline.txt'
        with open(txt_score) as f:
            lines = [line.split() for line in f]

        score_dic = {}
        online_dic = {}

        for line in lines:
            online_dic[line[0]] = [float(line[1])]

        for line in score:
            score_dic[line[0]] = [float(line[1])]

        for line in file:
            if line[0] in score_dic.keys():
                score_dic[line[0]].append(int(line[2]))
                score_dic[line[0]].append(line[1])

            if line[0] in online_dic.keys():
                online_dic[line[0]].append(int(line[2]))
                online_dic[line[0]].append(line[1])

        gen_keys = (list(set(score_dic.keys()).intersection(set(online_dic.keys()))))
        print "num:", len(gen_keys)

        huoshan_keys = [key for key in gen_keys if score_dic[key][2].split('_')[0] == 'huoshan']
        m_keys = [key for key in gen_keys if score_dic[key][2].split('_')[0] == 'M']
        t_keys = [key for key in gen_keys if score_dic[key][2].split('_')[0] == 'T']
        xigua_keys = [key for key in gen_keys if score_dic[key][2].split('_')[0] == 'xigua']
        banciyuan_keys = [key for key in gen_keys if score_dic[key][2].split('_')[0] == 'danciyuan']

        gen_keys = [key for key in gen_keys if score_dic[key][2].split('_')[0] != 'danciyuan']

        print 'test'
        # get_recall_pre(score_dic, m_keys, name='M')
        # get_recall_pre(score_dic, t_keys, name='T')
        # get_recall_pre(score_dic, banciyuan_keys, name='D')
        # get_recall_pre(score_dic, huoshan_keys, name='H')
        # get_recall_pre(score_dic, xigua_keys, name='X')
        # get_recall_pre(score_dic, gen_keys, name='G')

        print auc(score_dic, m_keys, name='M')
        print auc(score_dic, t_keys, name='T')
        #print auc(score_dic, banciyuan_keys, name='B')
        print auc(score_dic, huoshan_keys, name='H')
        print auc(score_dic, xigua_keys, name='X')
        print auc(score_dic, gen_keys, name='test')

        huoshan_keys = [key for key in gen_keys if online_dic[key][2].split('_')[0] == 'huoshan']
        m_keys = [key for key in gen_keys if online_dic[key][2].split('_')[0] == 'M']
        t_keys = [key for key in gen_keys if online_dic[key][2].split('_')[0] == 'T']
        xigua_keys = [key for key in gen_keys if online_dic[key][2].split('_')[0] == 'xigua']
        banciyuan_keys = [key for key in gen_keys if online_dic[key][2].split('_')[0] == 'danciyuan']

        print 'online:'
        # get_recall_pre(online_dic, m_keys, name='M')
        # get_recall_pre(online_dic, t_keys, name='T')
        # get_recall_pre(online_dic, banciyuan_keys, name='D')
        # get_recall_pre(online_dic, huoshan_keys, name='H')
        # get_recall_pre(online_dic, xigua_keys, name='X')
        # get_recall_pre(online_dic, gen_keys, name='G')

        print auc(online_dic, m_keys, name='M')
        print auc(online_dic, t_keys, name='T')
        #print auc(online_dic, banciyuan_keys, name='B')
        print auc(online_dic, huoshan_keys, name='H')
        print auc(online_dic, xigua_keys, name='X')
        print auc(online_dic, gen_keys, name='online')