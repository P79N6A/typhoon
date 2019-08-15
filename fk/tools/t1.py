#encoding: utf-8
import mxnet as mx
import numpy as np
import matplotlib.pyplot as plt
import os
import sys
import subprocess
import tarfile

dir = '/Users/ounozomiyo/Desktop/data/val/1/109965730537.jpg'

img = mx.image.imdecode(open(dir, 'rb').read())

img_np = img.asnumpy()
print img_np.shape

tmp = mx.image.imresize(img, 100, 70)
tmp, coord = mx.image.random_crop(img, (150, 200))
print(coord)

plt.imshow(tmp.asnumpy())
plt.show()
