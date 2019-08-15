# coding:utf-8
import os

dir = '/mnt/cephfs_wj/vc/wangxiyu/data/unified_vulgar/test/random_gen'
movie_name = os.listdir(dir)

for i, temp in enumerate(movie_name):
    print i
    if len(temp.split('_')) > 1:

        new_name = temp.split('_')[0] + '.jpg'
        os.rename(os.path.join(dir, temp), os.path.join(dir, new_name))

print 'suss!!!'