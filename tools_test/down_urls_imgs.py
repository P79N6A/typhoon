#encoding: utf-8
import numpy as np
import requests as req
from PIL import Image
import cStringIO
import csv
import urllib
import os
import multiprocessing as mp

def process(this_url):
    url = this_url[1]
    file_dir = this_url[0]
    name = file_dir.split('/')[-1]
    print name
    try:
        if not os.path.exists(file_dir):
            resource = urllib.urlopen(url)

            if int(resource.getcode()) == 200:
                output = open(file_dir, "wb")
                output.write(resource.read())
                output.close()
            else:
                return False
        return True
    except Exception as ex:
        print("error", name, url, ex)
        return False

if __name__ == "__main__":

    root_dir = '/Users/ounozomiyo/Desktop/company/data/unified_vulgar/test/down/'
    down_dir = "/Users/ounozomiyo/Desktop/company/data/unified_vulgar/test/down/data/"

    files_dir = ['huoshan_pos', 'huoshan_random', 'm_pos', 'm_random', 't_pos', 't_random', 'xigua_pos', 'xigua_random']

    lines = []

    # for file_dir in files_dir:
    #     csv_dir = root_dir + file_dir + '/result.txt'

    csv_dir = root_dir + 'xigua_url.txt'

    with open(csv_dir) as f:
        for line in f.readlines():
            url = line.split('\t')[1]
            file = os.path.join(down_dir, url.split('/')[-1].replace('\n', '') + ".jpg")
            lines.append([file, url])

    #csv_dir = "/mnt/cephfs_wj/vc/wangxiyu/data/video_vulgar/test/vulgar_test.csv"


    # count2 = 0
    # csv_file = csv.reader(open(csv_dir, "r"))



    # for line in csv_file:
    #     lines.append(line[0])
    #
    # print 'num: ', len(lines)

    print len(lines)

    for line in lines:
        process(line)

    # p = mp.Pool(1)
    # p.map(process, lines)
    # p.close()
    # p.join()

    print("suss!!!")
