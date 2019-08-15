#encoding: utf-8
import sys
import os
import numpy as np
import csv
import mxnet as mx

from data.data_muth_image import FileIter

batch_size = 1
gpus = [1]
model_dir = '/mnt/cephfs_wj/vc/wangxiyu/pro/mxnet/models/unified_vulgar/'
model_name = 'resnet101_5.16_pre_sgd'

ctx = [mx.gpu(i) for i in gpus]
model_prefix = os.path.join(model_dir, model_name)
epoch = 13

print("batch_size:", batch_size)

data_dir = '/mnt/cephfs_wj/vc/wangxiyu/data/video_vulgar/test/data/'

file_dir = os.path.join(data_dir, 'random_video_test.csv')

eval_data = FileIter(
    data_dir=file_dir,
    rgb_mean=(0, 0, 0),
    is_train=3,
    batch_size=batch_size)

# dir_test = "/mnt/cephfs_wj/vc/common/rhea/datasets/cc092d2d-5e79-4c8b-9212-61d06c83c411/"
#
# eval_data = mx.io.ImageRecordIter(
#         path_imgrec=dir_test,
#         data_shape=(3, 224, 224),
#         batch_size=batch_size,
#         shuffle=True,
#         preprocess_threads=20,
#         prefetch_buffer=20)

print("start load model!!!")
sym, arg_params, aux_params = mx.model.load_checkpoint(model_prefix, epoch)
mod = mx.mod.Module(symbol=sym, 
                    data_names=['data'],
                    label_names=['softmax_label'],
                    context=ctx)
mod.bind(data_shapes=[('data', (batch_size, 3, 224, 224))], for_training=False)
mod.set_params(arg_params, aux_params)
print("end load model!!!")
count = 0

label_pres = []

lis_csv = []

i = 0
print("start pre!!!")

positive_dic = []

for i, batch in enumerate(eval_data):
    id, batch = batch[0], batch[1]
    print i, id[0]
    mod.forward(batch, is_train=False)
    prob = mod.get_outputs()[0]
    pred = prob.reshape((batch_size, 2))
    label = batch.label[0].reshape((batch_size,))
    preds = [pred.as_in_context(ctx[0])]
    pred_label = preds[0].asnumpy().astype('float32')[:, 1]

    positive_dic.append([id[0], pred_label[0]])

pos_name = model_name + "_" + str(epoch) + 'pos.csv'
pos_w = csv.writer(open(os.path.join(data_dir, pos_name), 'w'))

for pos in positive_dic:
    pos_w.writerow(pos)

print("end pre!!!")