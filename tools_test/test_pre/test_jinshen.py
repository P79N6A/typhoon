#encoding: utf-8
import sys
import os
import numpy as np
import csv
import mxnet as mx

from data_muth_image import FileIter

batch_size = 1
gpus = [0]

model_name = 'resnet101_5.16_no_pre_sgd'
epoch = 13

model_dir = '/mnt/cephfs_wj/vc/wangxiyu/pro/mxnet/models/unified_vulgar/'

ctx = [mx.gpu(i) for i in gpus]
model_prefix = os.path.join(model_dir, model_name)


data_dir = '/mnt/cephfs_wj/vc/wangxiyu/data/unified_vulgar/test/csvs_data/'

file_name = model_name + "_" + str(epoch) + '.csv'
train_w = csv.writer(open(os.path.join(data_dir, file_name), 'w'))

random_name = model_name + "_" + str(epoch) + 'random.csv'
random_w = csv.writer(open(os.path.join(data_dir, random_name), 'w'))

pos_name = model_name + "_" + str(epoch) + 'pos.csv'
pos_w = csv.writer(open(os.path.join(data_dir, pos_name), 'w'))

positive_dir = os.path.join(data_dir, 'test_pos_gen.csv')
random_dir = os.path.join(data_dir, 'test_random_gen.csv')


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

positive_dic = []
random_dic = []

print "start pos!!!"
for i, batch in enumerate(positive_data):
    id, batch = batch[0], batch[1]
    print i, id[0]
    mod.forward(batch, is_train=False)
    prob = mod.get_outputs()[0]
    pred = prob.reshape((batch_size, 2))
    label = batch.label[0].reshape((batch_size,))
    preds = [pred.as_in_context(ctx[0])]
    pred_label = preds[0].asnumpy().astype('float32')[:, 1]

    positive_pres.append(pred_label[0])
    positive_dic.append([id[0], pred_label[0]])




print "start random!!!"

for i, batch in enumerate(random_data):
    id, batch = batch[0], batch[1]
    print i, id[0]
    mod.forward(batch, is_train=False)
    prob = mod.get_outputs()[0]
    pred = prob.reshape((batch_size, 2))
    label = batch.label[0].reshape((batch_size,))
    preds = [pred.as_in_context(ctx[0])]
    pred_label = preds[0].asnumpy().astype('float32')[:, 1]

    random_pres.append(pred_label[0])
    random_dic.append([id[0], pred_label[0]])


ratios = [i * 0.001 for i in range(1, 1000, 1)]
random_pres.sort()

print len(random_pres)
print len(positive_pres)


for random in random_dic:
    random_w.writerow(random)

for pos in positive_dic:
    pos_w.writerow(pos)

for ratio in ratios:
    thres = random_pres[int(len(random_pres) * (1 - ratio))]
    recall_nums = sum(np.array(positive_pres) >= thres)

    train_w.writerow([thres, ratio, float(recall_nums) / len(positive_pres)])

    print "Thres: %f, Ratio: %f, Recall: %f" % (thres, ratio, float(recall_nums) / len(positive_pres))