#encoding: utf-8
import sys
import os
import numpy as np
import csv
import mxnet as mx

from data.data_muth_image import FileIter

batch_size = 1
gpus = [0]

model_name = 'se_resnet-50_4-28_face'
epoch = 81

model_dir = '/mnt/cephfs_wj/vc/wangxiyu/pro/mxnet/models/fk'

random_face_dir = '/mnt/cephfs_wj/vc/wangxiyu/pro/mxnet/git/mxnet/fk/tools/face/csvs_out/val_output_random.csv'
positive_face_dir = '/mnt/cephfs_wj/vc/wangxiyu/pro/mxnet/git/mxnet/fk/tools/face/csvs_out/val_output_positive.csv'


positive_face = csv.reader(open(positive_face_dir, "r"))
random_face = csv.reader(open(random_face_dir, "r"))


face_results = {}
for line in positive_face:
    face_results[line[0]] = int(line[2])

for line in random_face:
    face_results[line[0]] = int(line[2])

print "face_results", len(face_results.keys())

ctx = [mx.gpu(i) for i in gpus]
model_prefix = os.path.join(model_dir, model_name)


root_dir = 'data_csv'
file_name = model_name + "_" + str(epoch) + '.csv'
train_w = csv.writer(open(os.path.join(root_dir, file_name), 'w'))
data_dir = '/mnt/cephfs_wj/vc/wangxiyu/data/fk_img_lab/csvs'

positive_dir = os.path.join(data_dir, 'val_only_face_positive.csv')
random_dir = os.path.join(data_dir, 'val_random.csv')

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

label_pres = []

for id, batch in positive_data:
    mod.forward(batch, is_train=False)
    prob = mod.get_outputs()[0]
    pred = prob.reshape((batch_size, 2))

    preds = [pred.as_in_context(ctx[0])]
    pred_label = preds[0].asnumpy().astype('float32')[:, 1]

    label = batch.label[0].reshape((batch_size,))
    labels = [label.as_in_context(ctx[0])]
    label = labels[0].asnumpy().astype('float32')

    id = id[0].split('/')[-1].split('.')[0]
    positive_pres.append([id, pred_label[0]])
    label_pres.append([label, pred_label[0]])


for id, batch in random_data:
    mod.forward(batch, is_train=False)
    prob = mod.get_outputs()[0]
    pred = prob.reshape((batch_size, 2))
    preds = [pred.as_in_context(ctx[0])]
    pred_label = preds[0].asnumpy().astype('float32')[:, 1]

    label = batch.label[0].reshape((batch_size,))
    labels = [label.as_in_context(ctx[0])]
    label = labels[0].asnumpy().astype('float32')

    print "id:", id

    id = id[0].split('/')[-1].split('.')[0]

    random_pres.append([id, pred_label[0]])
    label_pres.append([label, pred_label[0]])

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