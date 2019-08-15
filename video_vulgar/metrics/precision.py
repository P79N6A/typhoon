#encoding: utf-8
import mxnet as mx
import numpy as np

class Precision(mx.metric.EvalMetric):
    def __init__(self, num=None):
        super(Precision, self).__init__('Precision', num)

    def update(self, labels, preds):
        pred_label = mx.nd.argmax_channel(preds[0]).asnumpy().astype('int32')
        label = labels[0].asnumpy().astype('int32')

        mx.metric.check_label_shapes(label, pred_label)

        bin1 = (pred_label == 1)
        bin2 = (label == 1)

        tp1 = np.sum(bin1 * bin2)
        self.tp += tp1
        self.fp += (np.sum(bin1) - tp1)

    def get(self):
        precison = self.tp * 1.0 / (self.tp + self.fp + 1e-3)
        return ("Precision", precison)

    def reset(self):
        self.tp = 0.0
        self.fp = 0.0
