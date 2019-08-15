#encoding: utf-8
import mxnet as mx
import numpy as np


class Accuracy(mx.metric.EvalMetric):
    # 在定义类名称的时候，括号里面表示继承哪个类

    def __init__(self, num=None):
        super(Accuracy, self).__init__('accuracy', num)

    def update(self, labels, preds):

        pred_label = mx.nd.argmax_channel(preds[0]).asnumpy().astype('int32')
        label = labels[0].asnumpy().astype('int32')

        mx.metric.check_label_shapes(label, pred_label)

        self.sum_metric += (pred_label.flat == label.flat).sum()
        self.num_inst += len(pred_label.flat)

    def get(self):
        return ("acc", self.sum_metric*1.0 / self.num_inst)

    def reset(self):
        self.sum_metric = 0
        self.num_inst = 0
