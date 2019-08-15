#encoding: utf-8
import sys
import os
import numpy as np
import csv
import mxnet as mx

from data.data_muth_image import FileIter

batch_size = 1
gpus = [0]

model_name = 'resnet101_5.16_no_pre_sgd'
epoch = 20

model_dir = '/mnt/cephfs_wj/vc/wangxiyu/pro/mxnet/models/unified_vulgar/'

ctx = [mx.gpu(i) for i in gpus]
model_prefix = os.path.join(model_dir, model_name)


root_dir = 'data_csv'
file_name = "jinshen:" + model_name + "_" + str(epoch) + '.csv'

train_w = csv.writer(open(os.path.join(root_dir, file_name), 'w'))

data_dir = '/mnt/cephfs_wj/vc/wangxiyu/data/video_vulgar/test/data'

positive_dir = os.path.join(data_dir, 'test_pos.csv')
random_dir = os.path.join(data_dir, 'test_random.csv')

print positive_dir
print random_dir

positive_data = FileIter(
    data_dir=positive_dir,
    rgb_mean=(0, 0, 0),
    is_train=3,
    batch_size=batch_size)

random_data = FileIter(
    data_dir=random_dir,
    rgb_mean=(0, 0, 0),
    is_train=3,
    batch_size=batch_size)


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

positive_pres = []
random_pres = []

pos_scores = []
random_scores = []

for id, batch in positive_data:
    mod.forward(batch, is_train=False)
    prob = mod.get_outputs()[0]
    pred = prob.reshape((batch_size, 2))
    label = batch.label[0].reshape((batch_size,))
    preds = [pred.as_in_context(ctx[0])]
    pred_label = preds[0].asnumpy().astype('float32')[:, 1]
    positive_pres.append(pred_label)

    print id[0]
    pos_scores.append([id[0], pred_label[0]])

for id, batch in random_data:
    mod.forward(batch, is_train=False)
    prob = mod.get_outputs()[0]
    pred = prob.reshape((batch_size, 2))
    label = batch.label[0].reshape((batch_size,))
    preds = [pred.as_in_context(ctx[0])]
    pred_label = preds[0].asnumpy().astype('float32')[:, 1]
    random_pres.append(pred_label)

    print id[0]
    random_scores.append([id[0], pred_label[0]])

ratios = [i * 0.001 for i in range(1, 1000, 1)]
random_pres.sort()

print len(random_pres)
print len(positive_pres)

for ratio in ratios:
    thres = random_pres[int(len(random_pres) * (1 - ratio))]
    recall_nums = sum(np.array(positive_pres) >= thres)

    train_w.writerow([thres, ratio, float(recall_nums) / len(positive_pres)])

    print "Thres: %f, Ratio: %f, Recall: %f" % (thres, ratio, float(recall_nums) / len(positive_pres))

pos_w = csv.writer(open(os.path.join(root_dir, 'pos.csv'), 'w'))
random_w = csv.writer(open(os.path.join(root_dir, 'random.csv'), 'w'))


for score in random_scores:
    random_w.writerow(score)

for score in pos_scores:
    pos_w.writerow(score)