#encoding: utf-8
import cv2
import numpy as np
from skimage import transform
import random
import matplotlib.pyplot as plt
import time


def pad_image(image):
    height, width, _ = image.shape

    dis_pad_row = max(height, width)
    dis_pad_col = max(height, width)

    hight_temp = max(dis_pad_col - height, 0)
    hight_temp1 = hight_temp // 2
    hight_temp2 = hight_temp - hight_temp1
    weight_temp = max(dis_pad_row - width, 0)
    weight_temp1 = weight_temp // 2
    weight_temp2 = weight_temp - weight_temp1
    fillnp = np.pad(image, ((hight_temp1, hight_temp2),
                            (weight_temp1, weight_temp2),
                            (0, 0)), 'constant', constant_values=0)
    return fillnp


def process(data):

    thread = 0.5

    shape = (3, 512, 512)

    data = pad_image(data)

    if random.random() > thread:
        # 随机裁剪
        data = cv2.resize(data, (shape[2] + 32, shape[1] + 32))
        h_start = random.randint(0, 31)
        w_start = random.randint(0, 31)
        data = data[h_start:h_start + shape[1], w_start:w_start + shape[2]]

    # 左右镜面
    if random.random() > thread:
        data = data[:, ::-1]

    # 上下镜面
    if random.random() > thread:
        data = data[::-1]

    # 高斯模糊
    if random.random() > thread:
        kernel_size = (5, 5)
        sigma = random.random()*2
        data = cv2.GaussianBlur(data, kernel_size, sigma)

    # 随机旋转
    if random.random() > thread:
        angle = random.randint(0, 360)
        data = transform.rotate(data, angle)
        data = np.array(data, dtype='float32')

    data = cv2.cvtColor(data, cv2.COLOR_BGR2RGB)
    #data = np.transpose(data, (2, 0, 1))
    return data

if __name__ == "__main__":

    img_dir = '/Users/ounozomiyo/Desktop/zkpqw7yglxtx9hbanbaaapyfcjmmc0s3.jpg'

    img = cv2.imread(img_dir)

    print img.shape

    start = time.time()
    img = process(img)
    end = time.time()

    # if img.shape[0] > img.shape[1]:
    #     img = np.transpose(img, (1, 0, 2))

    print end - start
    print img.shape

    # cv2.imshow("image", img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    plt.imshow(img)  # 显示图片
    plt.axis('off')  # 不显示坐标轴
    plt.show()
