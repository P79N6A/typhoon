#encoding: utf-8
import sys
import os
import numpy as np
import csv
import mxnet as mx

from data_muth_image_fu_pos import FileIter

print "start_load_data"
batch_size = 1
gpus = [0]

model_name = 'resnet_fpn_101_xigua'
epoch = 9

model_dir = '/mnt/cephfs_wj/vc/wangxiyu/pro/mxnet/models/unified_vulgar/'

ctx = [mx.gpu(i) for i in gpus]
model_prefix = os.path.join(model_dir, model_name)


data_dir = '/mnt/cephfs_wj/vc/wangxiyu/data/video_vulgar/test/data'
file_name = model_name + "_" + str(epoch) + 'pos_nopad.csv'
train_w = csv.writer(open(os.path.join(data_dir, file_name), 'w'))

print "start_load_data"
positive_dir = os.path.join(data_dir, 'test_pos.csv')
positive_data = FileIter(
    data_dir=positive_dir,
    rgb_mean=(0, 0, 0),
    is_train=3,
    batch_size=batch_size)


print("start load model!!!")
sym, arg_params, aux_params = mx.model.load_checkpoint(model_prefix, epoch)
mod = mx.mod.Module(symbol=sym, 
                    data_names=['data'],
                    label_names=['softmax'],
                    context=ctx)
mod.bind(data_shapes=[('data', (batch_size, 3, 224, 224))], for_training=False)
mod.set_params(arg_params, aux_params)
print("end load model!!!")

test_scores = []

for i, batch in enumerate(positive_data):
    id, batch = batch[0], batch[1]
    print i
    mod.forward(batch, is_train=False)
    prob = mod.get_outputs()[0]
    pred = prob.reshape((batch_size, 2))
    label = batch.label[0].reshape((batch_size,))
    preds = [pred.as_in_context(ctx[0])]
    pred_label = preds[0].asnumpy().astype('float32')[:, 1]
    test_scores.append([id[0], pred_label[0]])

for test_score in test_scores:
    train_w.writerow(test_score)
