# pylint: skip-file
import configparser
import os
import numpy as np
import mxnet as mx
import time
import logging
from collections import namedtuple
#from metrics.crossEntropy import CrossEntropy
from metrics.recall import Recall
from metrics.precision import Precision
from metrics.accuracy import Accuracy
from metrics.crossEntropy import CrossEntropy
#import matplotlib.pyplot as plt

from config import config
from threading import Thread, Condition

BatchEndParam = namedtuple('BatchEndParams', ['epoch', 'nbatch', 'eval_metric'])


class Solver(object):
    def __init__(self,
                 symbol,
                 ctx=None,
                 begin_epoch=0,
                 num_epoch=None,
                 arg_params=None,
                 aux_params=None,
                 batch_size=1,
                 learning_rate=1e-3,
                 momentum=0.9,
                 wd=0.0005,
                 clip_gradient=5,
                 n_class=28,
                 **kwargs):

        self.symbol = symbol
        self.arg_params = arg_params
        self.aux_params = aux_params
        if ctx is None:
            ctx = mx.cpu()
        self.ctx = ctx
        self.begin_epoch = begin_epoch
        self.num_epoch = num_epoch
        self.batch_size = batch_size
        self.learning_rate = learning_rate
        self.momentum = momentum
        self.wd = wd
        self.clip_gradient = clip_gradient
        self.n_class = n_class
        self.kwargs = kwargs.copy()

    def fit(self,
            train_data,
            eval_data,
            epoch_end_callback=None,
            batch_end_callback=None,
            logger=None):
        if logger is None:
            logger = logging
        logging.info('Start training with %s', str(self.ctx))

        # defined the metric

        metric = mx.metric.CompositeEvalMetric()
        metric.add(Accuracy())
        metric.add(Recall())
        metric.add(Precision())
        metric.add(CrossEntropy())

        lr_iters = [int(iepoch * 10000 / self.batch_size) for iepoch in
                    range(1, self.num_epoch - self.begin_epoch)]
        lr_scheduler = mx.lr_scheduler.MultiFactorScheduler(lr_iters, 0.99)

        # create Module, bind and set params
        mod = mx.mod.Module(symbol=self.symbol,
                            data_names=['data'],
                            label_names=['softmax'],
                            context=self.ctx)

        mod.bind(data_shapes=[('data', (self.batch_size, 3, 224, 224))],
                 label_shapes=[('softmax', (self.batch_size, ))])

        mod.set_params(self.arg_params, self.aux_params)

        # init optimizer
        mod.init_optimizer(
            optimizer='sgd',
            optimizer_params={
                'lr_scheduler': lr_scheduler,
                'learning_rate': self.learning_rate,
                'clip_gradient': 5,
                'momentum': self.momentum,
                'wd': self.wd})

        for epoch in range(self.begin_epoch, self.num_epoch):
            nbatch = 0

            train_data.reset()

            metric.reset()

            logger.info("start:%d", epoch)

            for batch in train_data:
                nbatch += 1
                mod.forward(batch, is_train=True)
                mod.backward()
                mod.update()
                mx.nd.waitall()
                outputs = mod.get_outputs()

                pred = outputs[0].reshape((self.batch_size, self.n_class))
                label = batch.label[0].reshape((self.batch_size, ))

                metric.update([label.as_in_context(self.ctx[0])], [pred.as_in_context(self.ctx[0])])

                batch_end_params = BatchEndParam(epoch=epoch, nbatch=nbatch, eval_metric=metric)
                batch_end_callback(batch_end_params)

            name, value = metric.get()
            logger.info("--------------->Epoch[%d] train-%s=%f", epoch, name[0], value[0])


            if eval_data:
                nbatch = 0
                logger.info(" in eval process...")
                metric.reset()
                eval_data.reset()

                for batch in eval_data:
                    nbatch += 1
                    mod.forward(batch)
                    outputs = mod.get_outputs()
                    pred = outputs[0].reshape((self.batch_size, self.n_class))
                    label = batch.label[0].reshape((self.batch_size, ))

                    metric.update([label.as_in_context(self.ctx[0])], [pred.as_in_context(self.ctx[0])])

                    batch_end_params = BatchEndParam(epoch=epoch, nbatch=nbatch, eval_metric=metric)
                    batch_end_callback(batch_end_params)

                name, value = metric.get()
                logger.info("------------->Epoch[%d] validation-%s=%f", epoch, name[0], value[0])

            if epoch_end_callback is not None:
                arg_params, aux_params = mod.get_params()
                epoch_end_callback(epoch, self.symbol, arg_params, aux_params)
