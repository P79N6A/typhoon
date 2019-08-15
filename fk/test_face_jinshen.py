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

# 人脸数据
random_face_dir = '/mnt/cephfs_wj/vc/wangxiyu/pro/mxnet/git/mxnet/fk/tools/face/csvs_out/output_random_10w.csv'
positive_face_dir = '/mnt/cephfs_wj/vc/wangxiyu/pro/mxnet/git/mxnet/fk/tools/face/csvs_out/val_output_positive.csv'
positive_face = csv.reader(open(positive_face_dir, "r"))
random_face = csv.reader(open(random_face_dir, "r"))


# 图像数据
data_dir = '/mnt/cephfs_wj/vc/wangxiyu/data/fk_img_lab/csvs/'
positive_dir = os.path.join(data_dir, 'val_only_face_positive.csv')
random_dir = os.path.join(data_dir, 'val_random_10w.csv')


face_results = {}
for line in positive_face:
    face_results[line[0]] = line[2]

for line in random_face:
    face_results[line[0]] = line[2]

ctx = [mx.gpu(i) for i in gpus]
model_prefix = os.path.join(model_dir, model_name)


root_dir = 'data_csv'
file_name = model_name + "_" + str(epoch) + '.csv'

train_w = csv.writer(open(os.path.join(root_dir, file_name), 'w'))

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
                    label_names=['softmax'],
                    context=ctx)
mod.bind(data_shapes=[('data', (batch_size, 3, 224, 224))], for_training=False)
mod.set_params(arg_params, aux_params)
print("end load model!!!")
count = 0

positive_pres = []
random_pres = []


for id, batch in positive_data:
    mod.forward(batch, is_train=False)
    prob = mod.get_outputs()[0]
    pred = prob.reshape((batch_size, 2))

    label = batch.label[0].reshape((batch_size,))
    preds = [pred.as_in_context(ctx[0])]
    pred_label = preds[0].asnumpy().astype('float32')[:, 1]

    positive_pres.append([id[0], pred_label[0]])


for id, batch in random_data:
    mod.forward(batch, is_train=False)
    prob = mod.get_outputs()[0]
    pred = prob.reshape((batch_size, 2))

    label = batch.label[0].reshape((batch_size,))
    preds = [pred.as_in_context(ctx[0])]
    pred_label = preds[0].asnumpy().astype('float32')[:, 1]

    random_pres.append([id[0], pred_label[0]])

face_random = []
face_positive = []

for random in random_pres:
    if random[0] in face_results.keys():
        if face_results[random[0]] == '0':
            face_random.append(random[1])

for positive in positive_pres:
    if positive[0] in face_results.keys():
        if face_results[positive[0]] == '0':
            face_positive.append(positive[1])

ratios = [i * 0.001 for i in range(1, 1000, 1)]
face_random.sort(reverse=True)


for ratio in ratios:
    thres = face_random[int(len(random_pres) * ratio)]

    recall_nums = sum(np.array(face_positive) >= thres)

    #train_w.writerow([thres, ratio, float(recall_nums) / len(positive_pres)])
    train_w.writerow([thres, ratio, float(recall_nums) / len(face_positive)])

    print "Thres: %f, Ratio: %f, Recall: %f" % (thres, ratio, float(recall_nums) / len(positive_pres))
