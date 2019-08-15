#encoding: utf-8
import numpy as np
from mxnet.io import DataIter
from mxnet.io import DataBatch
import mxnet as mx
import random
import cv2
from skimage import transform
import os
import time


class FileIter(DataIter):
    def __init__(self, data_dirs,
                 rgb_mean=(0, 0, 0),

                 data_name="data",
                 label_name="softmax",

                 batch_size=2,
                 is_train=1,
                 class_num=2,
                 shape=(3, 224, 224)):

        super(FileIter, self).__init__()
        #  tile or other
        self.mode = 'tile'
        self.is_train = is_train
        self.batch_size = batch_size
        self.mean = np.array(rgb_mean)  # (R, G, B)
        self.shape = shape

        self.data_name = data_name
        self.label_name = label_name

        self.imgrecs = [mx.recordio.MXIndexedRecordIO(data_dir + ".idx", data_dir + ".rec", 'r')
                        for data_dir in data_dirs]

        self.img_idxs = [list(imgrec.keys) for imgrec in self.imgrecs]
        print len(self.img_idxs)

        self.reset()

        self.cursor_batch = -1

        self.num = sum([len(img_idx) for img_idx in self.img_idxs])

        self.class_num = class_num

        self.imgs = np.zeros((self.batch_size, 3, 224, 224))
        self.labels = np.zeros((self.batch_size,))

        if self.is_train == 1:
            print('train_total', self.num)
        elif self.is_train == 2:
            print('val_total', self.num)
        else:
            print('test_total', self.num)

    def reset(self):
        self.cursor_batch = -1
        self.img_ids = [0 for _ in self.img_idxs]
        self.flags = range(len(self.imgrecs))
        for img_idx in self.img_idxs:
            random.shuffle(img_idx)
            print len(img_idx), img_idx[0:10]


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


    def iter_next(self):
        self.cursor_batch += 1
        if (self.cursor_batch+1) * self.batch_size < self.num + self.getpad():
            return True
        else:
            return False


    def get_data_label(self):
        i = 0
        while i < self.batch_size:
            img, label = self.get_img()
            if img is not None and label is not None:
                self.imgs[i] = img
                self.labels[i] = label
                i += 1

        data = [mx.nd.array(self.imgs)]
        label = [mx.nd.array(self.labels)]
        return data, label


    def get_img(self):
        img = None
        label = None
        try:
            while True:
                idx = np.random.choice(self.flags)
                if len(self.img_idxs[idx]) > self.img_ids[idx]:
                    break
                else:
                    self.flags.remove(idx)

            start = time.time()

            imgrec = self.imgrecs[idx]
            img_idx = self.img_idxs[idx]
            s = imgrec.read_idx(img_idx[self.img_ids[idx]])

            self.img_ids[idx] += 1

            header, img = mx.recordio.unpack(s)
            img = cv2.imdecode(np.array(bytearray(img)), cv2.IMREAD_COLOR)
            img = self.process(img)
            label = header.label

            end = time.time()

            #print "time_" + str(i), end - start, len(self.img_idxs[idx])

        except Exception as e:
            print str(repr(e))
        finally:
            return img, label


    def getpad(self):
        if self.num % self.batch_size == 0:
            return 0
        return self.batch_size - self.num % self.batch_size


    def getindex(self):
        return self.cursor_batch


    def process(self, data, thread=0.5):
        '''
        预处理
        :param data: (h, w, c)
        :return:
        '''

        shape = self.shape
        # 摆正位置，将横屏变为竖屏
        if data.shape[1] > data.shape[0]:
            data = np.transpose(data, (1, 0, 2))
        data = self.pad_image(data)

        if self.is_train == 1:

            if random.random() > thread:
                # 随机裁剪
                data = cv2.resize(data, (shape[2] + 32, shape[1] + 32))
                h_start = random.randint(0, 31)
                w_start = random.randint(0, 31)
                data = data[h_start:h_start + shape[1], w_start:w_start + shape[2]]
            else:
                data = cv2.resize(data, (shape[2], shape[1]))

            # 左右镜面
            if random.random() > thread:
                data = data[:, ::-1]

            # 上下镜面
            if random.random() > thread:
                data = data[::-1]

            # 高斯模糊
            if random.random() > thread:
                kernel_size = (5, 5)
                sigma = random.random() * 2
                data = cv2.GaussianBlur(data, kernel_size, sigma)

            # # 随机旋转
            # if random.random() > thread:
            #     angle = random.randint(0, 360)
            #     data = transform.rotate(data, angle)
            #     data = np.array(data, dtype='float32')

        else:
            data = cv2.resize(data, (shape[1], shape[2]))

        data = cv2.cvtColor(data, cv2.COLOR_BGR2RGB)
        data = np.transpose(data, (2, 0, 1))
        return data


    def pad_image(self, image):
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


    def next(self):
        if self.iter_next():
            data, label = self.get_data_label()
            return DataBatch(data=data, label=label, pad=self.getpad(), index=self.getindex())
        else:
            raise StopIteration


if __name__ == "__main__":

    val_list = ['2ea400a9-f7af-44cb-a62a-7aca7ceca3ab']
    data_dir = '/mnt/cephfs_hl/vc/common/rhea/datasets'
    vals = []

    print 'start'

    for train in val_list:
        train_dir = os.path.join(data_dir, train)
        for file_name in os.listdir(train_dir):
            if file_name.endswith('.rec'):
                file_dir = os.path.join(train_dir, file_name.split('.')[0])
                vals.append(file_dir)

    val_dataiter = FileIter(
        data_dirs=vals,
        class_num=2,
        is_train=1,
        batch_size=512)

    for i in range(10):
        while True:
            try:
                if val_dataiter.iter_next():
                    start = time.time()
                    batch = val_dataiter.next()
                    end = time.time()
                    print "time_" + str(i), end - start
                else:
                    break
            except Exception as e:
                print str(repr(e))
        val_dataiter.reset()