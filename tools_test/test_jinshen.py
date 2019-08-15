#encoding: utf-8
import sys
import os
import numpy as np
import csv
import mxnet as mx

from mxnet.unified_vulgar.config import config

batch_size = 1
gpus = [1]
model_name = 'se_resnet-101_3-24'
model_dir = '/mnt/cephfs_wj/vc/wangxiyu/pro/mxnet/models/unified_vulgar'
ctx = [mx.gpu(i) for i in gpus]
model_prefix = os.path.join(model_dir, model_name)
epochs = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#epoch = 173

print("batch_size:", batch_size)

# eval_data = FileIter(
#     root_dir=config.data_dir,
#     rgb_mean=(0, 0, 0),
#     is_train=3,
#     batch_size=batch_size)

dir_random = "/mnt/cephfs_wj/vc/common/rhea/datasets/b03639b0-b25c-44fb-b3b9-c992095d115b/xaa.rec"
dir_positive = "/mnt/cephfs_wj/vc/common/rhea/datasets/3a854937-3e80-4e99-957b-901652852206/xaa.rec"

root_dir = './'
out_file = model_name + '.csv'
out_write = csv.writer(open(os.path.join(root_dir, out_file), 'w'))

eval_random = mx.io.ImageRecordIter(
        path_imgrec=dir_random,
        data_shape=(3, 224, 224),
        batch_size=batch_size,
        shuffle=True,
        preprocess_threads=20,
        prefetch_buffer=20)

eval_positive = mx.io.ImageRecordIter(
        path_imgrec=dir_positive,
        data_shape=(3, 224, 224),
        batch_size=batch_size,
        shuffle=True,
        preprocess_threads=20,
        prefetch_buffer=20)

print("start load model!!!")

mods = []

for epoch in epochs:
    sym, arg_params, aux_params = mx.model.load_checkpoint(model_prefix, epoch)
    mod = mx.mod.Module(symbol=sym, data_names=['data'], label_names=['softmax_label'], context=ctx)
    mod.bind(data_shapes=[('data', (batch_size, 3, 224, 224))], for_training=False)
    mod.set_params(arg_params, aux_params)
    mods.append(mod)

print("end load model!!!")
count = 0

pres_random = {}
pres_positive = {}
lis_csv = []
i = 0
print("start pre!!!")
for i, batch in enumerate(eval_random):
    for mod_i in range(len(mods)):
        mods[mod_i].forward(batch, is_train=False)
        prob = mods[mod_i].get_outputs()[0]
        pred = prob.reshape((batch_size, 2))
        preds = [pred.as_in_context(ctx[0])]
        pred_label = preds[0].asnumpy().astype('float32')[:, 1]
        if mod_i not in pres_random.keys():
            pres_random[mod_i] = []
        pres_random[mod_i].append(pred_label)
    i += 1
    print "random batch: %d" % (i)

for i, batch in enumerate(eval_positive):
    for mod_i in range(len(mods)):
        mods[mod_i].forward(batch, is_train=False)
        prob = mods[mod_i].get_outputs()[0]
        pred = prob.reshape((batch_size, 2))
        preds = [pred.as_in_context(ctx[0])]
        pred_label = preds[0].asnumpy().astype('float32')[:, 1]
        if mod_i not in pres_positive.keys():
            pres_positive[mod_i] = []
        pres_positive[mod_i].append(pred_label)
    i += 1
    print "positive batch: %d" % (i)

print("end pre!!!")

ratio = 0.1

###############
#生成进审率
for mod_i in range(len(mods)):
    scores_random = pres_random[mod_i]
    scores_positive = pres_positive[mod_i]

    scores_random.sort()
    # print scores_random
    thres = scores_random[int(len(scores_random) * (1 - ratio))]
    recall_nums = np.sum(np.array(scores_positive) >= thres)

    out_write
    print "Epoch: %d, Thres: %f, Ratio: %f, Recall: %f" % (mod_i, thres, ratio, float(recall_nums) / len(scores_positive))
#################
