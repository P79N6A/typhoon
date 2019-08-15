#encoding: utf-8
import sys
import os
import numpy as np
import csv
import mxnet as mx

from data.data import FileIter

batch_size = 1
gpus = [1]
model_name = 'se_resnet-50_fk_224_3-10'
ctx = [mx.gpu(i) for i in gpus]
model_prefix = os.path.join(config.model_dir, model_name)
epoch = 33
#epoch = 173

print("batch_size:", batch_size)

eval_data = FileIter(
    root_dir=config.data_dir,
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
for i, batch in enumerate(eval_data):
    mod.forward(batch, is_train=False)
    prob = mod.get_outputs()[0]

    pred = prob.reshape((batch_size, 2))
    label = batch.label[0].reshape((batch_size,))

    preds = [pred.as_in_context(ctx[0])]
    labels = [label.as_in_context(ctx[0])]

    pred_label = preds[0].asnumpy().astype('float32')[:, 1]
    label = labels[0].asnumpy().astype('float32')

    mx.metric.check_label_shapes(label, pred_label)
    label_pres.append([label, pred_label])

    i += 1
    #print(i, id, label, pred_label)
    #lis_csv.append([i, id[0].split('/')[-1], label[0], pred_label[0]])

print("end pre!!!")

# ###############
# # save out.csv
# print("start save!!!")
# writer_fu = csv.writer(open(r"./data/out_fu.csv", 'w'))
# writer_zheng = csv.writer(open(r"./data/out_zheng.csv", 'w'))
#
# lis_csv.sort(key=lambda x: x[3], reverse=True)
#
# for li in lis_csv:
#     if li[2] == 0:
#         writer_fu.writerow(li)
#     if li[2] == 1:
#         writer_zheng.writerow(li)
# print("end save!!!")
# ###############


###############
#生成RP图
for i in range(1, 100, 1):
    tp_num = 0
    fn_num = 0
    fp_num = 0
    for label, pred_label in label_pres:
        bin1 = (pred_label >= i*0.01)
        bin2 = (label == 1)
        tp = np.sum(bin1 * bin2)
        tp_num += tp
        fn_num += (np.sum(bin2) - tp)
        fp_num += (np.sum(bin1) - tp)
    recall = tp_num * 1.0 / (tp_num + fn_num)
    precison = tp_num * 1.0 / (tp_num + fp_num)
    print("recall: ", recall, "    precision: ", precison, "  threshold: ", i * 0.01)
#################

#################
#是否存在重复
lines = []
for line in lis_csv:
    lines.append(line[0])

print(len(set(lines)), len(lis_csv))
#################
