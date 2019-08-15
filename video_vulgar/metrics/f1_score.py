#encoding: utf-8
import mxnet as mx
import numpy as np

class f1_score(mx.metric.EvalMetric):

    def __init__(self, num=None):
        super(f1_score, self).__init__('f1_score', num)

    def update(self, labels, preds):

            pred_label = preds[0].asnumpy()
            pred_label = np.where(pred_label > 0.5, 1, 0).astype('int32')

            label = labels[0].asnumpy().astype('int32')

            bin1 = (pred_label == 1)
            bin2 = (label == 1)
            a = np.sum(bin1)
            b = np.sum(bin2)

            self.tp += np.sum(bin1 * bin2)
            self.fp += (np.sum(bin1) - self.tp)
            self.fn += (np.sum(bin2) - self.tp)

    def get(self):
        precison = self.tp * 1.0 / (self.tp + self.fp)
        recall = self.tp * 1.0 / (self.tp + self.fn)
        return ("f1-score", 2.0 * precison * recall/(precison + recall))

    def reset(self):
        self.tp = 0.0
        self.fn = 0.0
        self.fp = 0.0