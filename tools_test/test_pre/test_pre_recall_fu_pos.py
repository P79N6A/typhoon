#encoding: utf-8
import sys
import os
import numpy as np
import csv
import mxnet as mx

from data_muth_image_fu_pos import FileIter

batch_size = 1
gpus = [1]

model_name = 'resnet_fpn_101_6_27'
model_dir = '/mnt/cephfs_hl/vc/wangxiyu/models/unified_vulgar'

data_dir = '/mnt/cephfs/lab/wangxiyu/data/'

positive_dir = os.path.join(data_dir, 'gen_test.csv')
positive_data = FileIter(
    data_dir=positive_dir,
    rgb_mean=(0, 0, 0),
    is_train=3,
    batch_size=batch_size)

ctx = [mx.gpu(i) for i in gpus]

for epoch in range(1, 2, 1):
    print "start: ", epoch
    model_prefix = os.path.join(model_dir, model_name)

    file_name = model_name + "_" + str(epoch) + '.csv'
    train_w = csv.writer(open(os.path.join(data_dir, file_name), 'w'))

    sym, arg_params, aux_params = mx.model.load_checkpoint(model_prefix, epoch)

    mod = mx.mod.Module(symbol=sym,
                        data_names=['data'],
                        label_names=['softmax'],
                        context=ctx)

    # mod.bind(data_shapes=[('data', (batch_size, 3, 224, 224))], for_training=False)
    print "#"
    mod.bind(data_shapes=positive_data.provide_data,
             label_shapes=positive_data.provide_label,
             for_training=False)

    print "!"
    mod.set_params(arg_params, aux_params)
    test_scores = []

    positive_data.reset()
    for i, batch in enumerate(positive_data):
        id, batch = batch[0], batch[1]
        mod.forward(batch, is_train=False)
        prob = mod.get_outputs()[0]
        pred = prob.reshape((batch_size, 2))
        label = batch.label[0].reshape((batch_size,))
        preds = [pred.as_in_context(ctx[0])]
        pred_label = preds[0].asnumpy().astype('float32')[:, 1]
        test_scores.append([id[0], pred_label[0]])

    for test_score in test_scores:
        train_w.writerow(test_score)
