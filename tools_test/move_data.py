#encoding: utf-8
import os
import shutil
import csv
import multiprocessing as mp

def mymovefile(srcfile, dstfile):
    if not os.path.isfile(srcfile):
        print "%s not exist!"%(srcfile)
    else:
        fpath, fname = os.path.split(dstfile)    #分离文件名和路径
        if not os.path.exists(fpath):
            os.makedirs(fpath)                #创建路径
        shutil.move(srcfile, dstfile)          #移动文件
        print "move %s -> %s" % (srcfile, dstfile)


def mycopyfile(srcfile, dstfile):
    if not os.path.isfile(srcfile):
        print "%s not exist!" % (srcfile)
    else:
        fpath,fname = os.path.split(dstfile)    #分离文件名和路径
        if not os.path.exists(fpath):
            os.makedirs(fpath)                #创建路径
        shutil.copyfile(srcfile, dstfile)      #复制文件
        print "copy %s -> %s" % (srcfile, dstfile)

if __name__ == "__main__":
    srcfile_dir = '/Users/ounozomiyo/Desktop/company/data/unified_vulgar/test/data/danciyuan_random'
    dstfile_dir = '/Users/ounozomiyo/Desktop/company/data/unified_vulgar/test/data/random_gen'

    for i, img_dir in enumerate(os.listdir(srcfile_dir)):
        if i < 2000:
            srcfile = os.path.join(srcfile_dir, img_dir)
            dstfile = os.path.join(dstfile_dir, img_dir)
            if not os.path.exists(dstfile):
                mycopyfile(srcfile, dstfile)
            print i



    print "suss!!!"