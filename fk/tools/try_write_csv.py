#encoding: utf-8
import os
import csv
import numpy as np
import cv2

dir = '/Users/ounozomiyo/Desktop/company/data/fk_img_lab/val/1/13245332659.jpg'

with open(dir) as f:
    data = f.read()

img = cv2.imdecode(np.array(bytearray(data)), cv2.IMREAD_COLOR)


result, img_encode = cv2.imencode('.jpg', None)

print type(result), result

#data_encode = np.array(img_encode)
#str_encode = data_encode.tostring()
