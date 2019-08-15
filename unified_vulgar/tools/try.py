#encoding: utf-8
import numpy as np
import requests as req
from PIL import Image
import urllib
import cv2
import os
import mxnet as mx
import matplotlib.pyplot as plt
import random

### cv测试
# dir = '/Users/ounozomiyo/Desktop/data/fk/val/1/58783169729.jpg'
# img = cv2.imread(dir)
# destRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# plt.imshow(destRGB)
# plt.show()

### url测试
url = 'http://p-tcs.bytedance.net/img/banciyuan/user/3773444/item/c0jxe/f44a0b4e35c94cf58fbf8f6573991cd6.jpg~650x0_q90.image'
resource = urllib.urlopen(url)
if int(resource.getcode()) == 200:
    img = resource.read()
    img = cv2.imdecode(np.array(bytearray(img)), cv2.IMREAD_COLOR)
    # plt.imshow(img)
    # plt.show()

# ### rec测试
# root_dir = './'
# rec_name = 'test'
# rec_write = mx.recordio.MXIndexedRecordIO(os.path.join(root_dir, rec_name + ".idx"),
#                                           os.path.join(root_dir, rec_name + ".rec"), 'w')
#
# header = mx.recordio.IRHeader(0, 1, 1, 0)
# s = mx.recordio.pack_img(header, img)
# rec_write.write_idx(1, s)
#
# print rec_write.keys

dir1 = "/Users/ounozomiyo/pro/git/mxnet/unified_vulgar/tools"
dir = "/Users/ounozomiyo/Desktop/general1"

# data_iter = mx.io.ImageRecordIter(
#         path_imgrec=os.path.join(dir1, "test.rec"),
#         data_shape=(3, 224, 224),
#         batch_size=1,
#         preprocess_threads=1,
#         prefetch_buffer=20)
#
# data_iter.reset()
# batch = data_iter.next()
#
# for j, batch in enumerate(data_iter):
#     imgs, labels = batch.data[0], batch.label[0]
#     imgs = imgs.asnumpy()
#
#     for i in range(imgs.shape[0]):
#         img = imgs[i]
#
#         print img.shape
#
#         img = np.transpose(img, (1, 2, 0))
#         print type(img)
#         print img.shape, np.max(img)
#         img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#         plt.imshow(img)
#         plt.show()
#
#     if j == 10:
#         break

imgrec = mx.recordio.MXIndexedRecordIO(dir + ".idx", dir + ".rec", 'r')
l = imgrec.keys
id = random.sample(l, 1)[0]
print id
s = imgrec.read_idx(l[3])
header, img = mx.recordio.unpack(s)

img = cv2.imdecode(np.array(bytearray(img)), cv2.IMREAD_COLOR)

#img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

print img.shape, type(img)

plt.imshow(img)
plt.show()