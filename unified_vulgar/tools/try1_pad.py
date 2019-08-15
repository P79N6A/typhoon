#encoding: utf-8
import numpy as np
import cv2
import pickle
import matplotlib.pyplot
import PIL.Image

def array_to_image(filename):
    '''
    从二进制文件中读取数据并重新恢复为图片
    '''
    with open(filename, mode='rb') as f:
        arr = pickle.load(f) #加载并反序列化数据
    rows = arr.shape[0] #rows=5
    #pdb.set_trace()
    #print("rows:",rows)
    arr = arr.reshape(rows, 3, 32,32)
    print(arr)	#打印数组
    for index in range(rows):
        a = arr[index]
        #得到RGB通道
        r = PIL.Image.fromarray(a[0]).convert('L')
        g = PIL.Image.fromarray(a[1]).convert('L')
        b = PIL.Image.fromarray(a[2]).convert('L')
        image = PIL.Image.merge("RGB", (r, g, b))
        #显示图片
        matplotlib.pyplot.imshow(image)
        matplotlib.pyplot.show()

if __name__ == "__main__":
    img_dir = '/Users/ounozomiyo/Desktop/fff905d6c52241e99a2226d814742f14'
    array_to_image(img_dir)

