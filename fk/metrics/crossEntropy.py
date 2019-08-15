#encoding: utf-8
import mxnet as mx
import numpy as np

class CrossEntropy(mx.metric.EvalMetric):
    """Computes Cross Entropy loss."""

    def __init__(self, eps=1e-12, name='cross-entropy',
                 output_names=None, label_names=None):
        super(CrossEntropy, self).__init__(
            name, eps=eps,
            output_names=output_names, label_names=label_names)
        self.eps = eps

    def update(self, labels, preds):
        """Updates the internal evaluation result.

        Parameters
        ----------
        labels : list of `NDArray`
            The labels of the data.

        preds : list of `NDArray`
            Predicted values.
        """
        pred = preds[0].asnumpy().astype('float')[:, 1]
        label = labels[0].asnumpy().astype('float')

        mx.metric.check_label_shapes(label, pred)

        self.sum_metric += -1 * (label * np.log(pred+1e-14) + (1 - label) * np.log(1 - pred + 1e-14)).sum()
        self.num_inst += label.shape[0]

    def get(self):
        return ('Cross_entropy', self.sum_metric * 1.0 / self.num_inst)


    def reset(self):
        self.sum_metric = 0
        self.num_inst = 0

