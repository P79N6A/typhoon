import numpy as np
import os
from mxnet.io import DataIter
from mxnet.io import DataBatch
import mxnet as mx
from PIL import Image
import random
import csv

class FileIter(DataIter):
    def __init__(self, root_dir,
                 rgb_mean=(0, 0, 0),

                 data_name="data",
                 label_name="softmax_label",

                 batch_size=2,
                 is_train=1,
                 class_num=10):

        super(FileIter, self).__init__()
        #  tile or other
        self.mode = 'tile'
        self.is_train = is_train
        self.batch_size = batch_size
        self.root_dir = root_dir
        self.mean = np.array(rgb_mean)  # (R, G, B)

        self.data_name = data_name
        self.label_name = label_name

        self.pid_dirs = self.get_pid_dirs(self.root_dir, self.is_train)

        self.cursor_batch = -1
        self.num = len(self.pid_dirs)
        self.class_num = class_num

        self.imgs = np.zeros((self.batch_size, 3, 224, 224))
        self.signatures = np.zeros((self.batch_size, 50, 300))
        self.nicknames = np.zeros((self.batch_size, 50, 300))
        self.labels = np.zeros((self.batch_size,))
        if self.is_train == 1:
            print('train_num: ', self.num)
        elif self.is_train == 2:
            print('val_num: ', self.num)

    def get_pid_dirs(self, data_dir, is_train):
        pids = []

        if is_train == 1:
            textDir = os.path.join(data_dir, 'train224.csv')
        elif is_train == 2:
            textDir = os.path.join(data_dir, 'val224.csv')
        else:
            textDir = os.path.join(data_dir, 'test.csv')

        csv_file = csv.reader(open(textDir, "r"))

        for line in csv_file:
            pid = line[0]
            label = line[1]
            npy_dir = line[2]

            pids.append([pid, label, npy_dir])
        return pids


    @property
    def provide_data(self):
        """The name and shape of data provided by this iterator"""
        return [(self.data_name, (self.batch_size, 3, 224, 224)),
                (self.avatar, (self.batch_size, 50, 300)),
                (self.nickname, (self.batch_size, 50, 300))]

    @property
    def provide_label(self):
        """The name and shape of label provided by this iterator"""
        return [(self.label_name, (self.batch_size, ))]


    def get_batch_size(self):
        return self.batch_size

    def reset(self):
        self.cursor_batch = -1
        random.shuffle(self.pid_dirs)

    def iter_next(self):
        self.cursor_batch += 1
        if (self.cursor_batch+1) * self.batch_size <= self.num + self.getpad():
            return True
        else:
            return False

    def get_data_label(self):
        try:
            for i in range(self.batch_size):
                currer = int(i + self.batch_size * self.cursor_batch)
                npy = np.load(self.pid_dirs[currer][2])
                if currer < self.num:
                    self.imgs[i] = npy.item()['avatar_img']
                    self.signatures[i] = npy.item()['signature']
                    self.nicknames[i] = npy.item()['nickname']
                    self.labels[i] = self.pid_dirs[currer][1]
        except Exception as e:
            print('Error:', e)

        data = [mx.nd.array(self.imgs), mx.nd.array(self.signatures), mx.nd.array(self.nicknames)]
        label = [mx.nd.array(self.labels)]
        return data, label

    def getpad(self):
        if self.num % self.batch_size == 0:
            return 0
        return self.batch_size - self.num % self.batch_size

    def getindex(self):
        return self.cursor_batch

    def next(self):
        if self.iter_next():
            data, label = self.get_data_label()
            return DataBatch(data=data, label=label, pad=self.getpad(), index=self.getindex())
        else:
            raise StopIteration
