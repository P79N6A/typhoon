from mxnet.io import DataBatch
import mxnet as mx
import os
import cv2
import numpy as np

model_dir = '/mnt/cephfs_wj/vc/wangxiyu/pro/mxnet/models/fk'
model_name = 'se_resnet-50_4-28_face'

model_prefix = os.path.join(model_dir, model_name)
sym, arg_params, aux_params = mx.model.load_checkpoint(model_prefix, 81)
mod = mx.mod.Module(symbol=sym,
                    data_names=['data'],
                    label_names=['softmax'],
                    context=mx.gpu(0))
mod.bind(data_shapes=[('data', (1, 3, 224, 224))], for_training=False)
mod.set_params(arg_params, aux_params)

img_dir = '/mnt/cephfs_wj/vc/wangxiyu/data/fk_img_lab/val/1'
img_name = '99959218864.jpg'

img_dir = os.path.join(img_dir, img_name)

with open(img_dir) as f:
    img = f.read()

img = cv2.imdecode(np.array(bytearray(img)), cv2.IMREAD_COLOR)

if img.shape[0] != img.shape[1]:
    if img.shape[0] > img.shape[1]:
        margin = (img.shape[0] - img.shape[1]) // 2
        img = img[margin:margin + img.shape[1], :]
    else:
        margin = (img.shape[1] - img.shape[0]) // 2
        img = img[:, margin:margin + img.shape[0]]

img = cv2.resize(img, (224, 224))

img = np.array(img, dtype='float32')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = np.transpose(img, (2, 0, 1))

img = np.reshape(img, (1, 3, 224, 224))

data = [mx.nd.array(img)]

batch = DataBatch(data=data)

print 'batch: ', batch

mod.forward(batch, is_train=False)

print 'forward ok'
prob = mod.get_outputs()[0]
pred = prob.reshape((1, 2))
pred_label = pred.asnumpy().astype('float32')[:, 1]
score = pred_label[0]

print 'score:', score

