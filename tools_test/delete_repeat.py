# -*- coding:utf-8 -*-
"""

用dhash判断是否相同照片
基于渐变比较的hash
hash可以省略(本文省略)
By Guanpx

"""
from PIL import Image
from os import listdir
import os
import hashlib
import sys

reload(sys)
sys.setdefaultencoding('utf8')

def picPostfix():  # 相册后缀的集合
    postFix = set()
    postFix.update(['bmp', 'jpg', 'png', 'tiff', 'gif', 'pcx', 'tga', 'exif',
                    'fpx', 'svg', 'psd', 'cdr', 'pcd', 'dxf', 'ufo', 'eps', 'JPG', 'raw', 'jpeg'])
    return postFix

def getDiff(width, high, image):  # 将要裁剪成w*h的image照片
    diff = []
    im = image.resize((width, high))
    imgray = im.convert('L')  # 转换为灰度图片 便于处理
    pixels = list(imgray.getdata())  # 得到像素数据 灰度0-255

    for row in range(high):  # 逐一与它左边的像素点进行比较
        rowStart = row * width  # 起始位置行号
        for index in range(width - 1):
            leftIndex = rowStart + index
            rightIndex = leftIndex + 1  # 左右位置号
            diff.append(pixels[leftIndex] > pixels[rightIndex])

    return diff  # *得到差异值序列 这里可以转换为hash码*

def getHamming(diff=[], diff2=[]):  # 暴力计算两点间汉明距离
    hamming_distance = 0
    for i in range(len(diff)):
        if diff[i] != diff2[i]:
            hamming_distance += 1

    return hamming_distance

def getmd5(file):
    # md5编码
    if not os.path.isfile(file):
        return
    fd = open(file,'rb')
    md5 = hashlib.md5()
    md5.update(fd.read())
    fd.close()
    return md5.hexdigest()

def md5(inpath):
    allfile = []
    md5list = {}
    sizelist = []
    identicallist = []

    uipath = unicode(inpath, "utf8")

    print "start load dir"
    for path, dir, filelist in os.walk(uipath):
        for filename in filelist:
            allfile.append(os.path.join(path, filename))
    print "end load dir"

    print "start find repeat"
    for photo in allfile:
        size = os.path.getsize(photo)
        if size not in sizelist:
            sizelist.append(size)
        else:
            md5sum = getmd5(photo)
            if md5sum not in md5list.keys():
                md5list[md5sum] = photo
            else:
                # print md5list[md5sum], photo
                identicallist.append(photo)
    print "end find repeat"

    print "identical photos: " + str(len(identicallist))
    print "count: " + str(len(allfile))
    print "count: " + str(len(allfile) - len(identicallist))

    print "start delect"
    for dir in identicallist:
        os.remove(dir)
    print "end delect"

def dhash(dirName, is_del=True):
    width = 32
    high = 32  # 压缩后的大小
    allDiff = {}
    postFix = picPostfix()  # 图片后缀的集合
    dirList = listdir(dirName)
    cnt = 0
    for name in dirList:
        cnt += 1
        print cnt  # 可以不打印 表示处理的文件计数
        if str(name).split('.')[-1] in postFix:  # 判断后缀是不是照片格式

            im = Image.open(r'%s/%s' % (dirName, unicode(str(name), "utf-8")))

            diff = getDiff(width, high, im)
            allDiff[str(name)] = diff
    print "repeat:"

    id = 0
    for one in dirList:
        id += 1
        print id
        if one in os.listdir(dirName):
            for two in os.listdir(dirName):
                if str(one) != ".DS_Store" and str(two) != ".DS_Store" and one != two:
                    ans = getHamming(allDiff[one], allDiff[two])
                    if ans <= 200:  # 判别的汉明距离，自己根据实际情况设置
                        print id, one, "and", two, "maybe same photo..."
                        if is_del:
                            file_dir = os.path.join(dirName, two)
                            if os.path.exists(file_dir):
                                os.remove(file_dir)
                                print "delling", two

if __name__ == '__main__':
    dirName = "/Users/ounozomiyo/Desktop/公司/data/fk_img_lab/train_woman_face/"
    #md5(dirName)

    dhash(dirName, is_del=True)
