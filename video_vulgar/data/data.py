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

        self.pid_dirs, self.number = self.get_pid_dirs(self.root_dir, self.is_train)

        self.cursor_batch = -1
        self.class_num = class_num

        self.flags = range(len(self.pid_dirs))

        self.generator = lambda x: self.get_data(x)
        self.recs = map(self.generator, self.pid_dirs)

        print("!!!", type(self.recs))

        if self.is_train == 1:
            print('train_num: ', self.number)
        elif self.is_train == 2:
            print('val_num: ', self.number)


    def get_pid_dirs(self, data_dir, is_train):
        pids = []
        number = 0
        if is_train == 1:
            textDir = os.path.join(data_dir, 'train.csv')
        elif is_train == 2:
            textDir = os.path.join(data_dir, 'val.csv')
        else:
            textDir = os.path.join(data_dir, 'test.csv')
        csv_file = csv.reader(open(textDir, "r"))
        for line in csv_file:
            dir_recs = line[0]
            csv_file = csv.reader(open(os.path.join(dir_recs, 'uri_labels.txt'), "r"))
            number += sum(1 for _ in csv_file)
            for dir in os.listdir(dir_recs):
                if dir.endswith('.rec'):
                    pids.append(os.path.join(dir_recs, dir))
        return pids, number


    def get_data(self, path):
        dataiter = mx.io.ImageRecordIter(
            path_imgrec=path,
            data_shape=(3, 224, 224),
            batch_size=self.batch_size,
            rand_crop=True if self.is_train == 1 else False,
            rand_mirror=True if self.is_train == 1 else False,
            shuffle=True,
            preprocess_threads=5,
            prefetch_buffer=20)
        return dataiter


    @property
    def provide_data(self):
        """The name and shape of data provided by this iterator"""
        return [(self.data_name, (self.batch_size, 3, 224, 224))]


    @property
    def provide_label(self):
        """The name and shape of label provided by this iterator"""
        return [(self.label_name, (self.batch_size, ))]


    def get_batch_size(self):
        return self.batch_size


    def reset(self):
        for rec in self.recs:
            rec.reset()
        self.flags = range(len(self.pid_dirs))


    def next(self):
        while self.flags:
            idx = np.random.choice(self.flags)
            try:
                 batch = self.recs[idx].next()
                 return batch
            except StopIteration:
                self.flags.remove(idx)
                if not self.flags:
                    raise StopIteration
                continue
            break
