#encoding: utf-8
import numpy as np
from mxnet.io import DataIter
from mxnet.io import DataBatch
import mxnet as mx
import random
import cv2
from skimage import transform
import os
import multiprocessing as mp
import time


class FileIter(DataIter):

    def __init__(self, data_dirs,
                 rgb_mean=(0, 0, 0),

                 data_name="data",
                 label_name="softmax_label",

                 batch_size=2,
                 is_train=1,
                 class_num=2,
                 shape=(3, 224, 224),
                 process_num=20):

        super(FileIter, self).__init__()
        #  tile or other
        self.mode = 'tile'
        self.is_train = is_train
        self.batch_size = batch_size
        self.mean = np.array(rgb_mean)  # (R, G, B)
        self.shape = shape

        self.data_name = data_name
        self.label_name = label_name

        self.imgs_queue = mp.Queue(maxsize=100)
        self.lines_queue = mp.Queue()

        self.cursor_batch = -1
        self.class_num = class_num
        self.process_num = process_num

        self.imgrecs = [mx.recordio.MXIndexedRecordIO(data_dir + ".idx", data_dir + ".rec", 'r')
                        for data_dir in data_dirs]

        self.img_idxs = [list(imgrec.keys) for imgrec in self.imgrecs]

        self.img_ids = [0 for _ in data_dirs]
        self.flags = range(len(self.imgrecs))

        self.num = sum([len(img_idx) for img_idx in self.img_idxs])

        self.lines = self.get_lis()
        print 'batch_num', len(self.lines)
        print 'batch_size', len(self.lines[0])

        if self.is_train == 1:
            print('train_total', self.num)
        elif self.is_train == 2:
            print('val_total', self.num)
        else:
            print('test_total', self.num)

        self.reset()


    def get_lis(self):
        batchs_lis = []
        for i in range(self.num/self.batch_size):
            batch = []
            for _ in range(self.batch_size):
                while True:
                    idx = np.random.choice(self.flags)
                    if len(self.img_idxs[idx]) > self.img_ids[idx]:
                        break
                    else:
                        self.flags.remove(idx)
                batch.append([idx,  self.img_idxs[idx][self.img_ids[idx]]])
                self.img_ids[idx] += 1
            batchs_lis.append(batch)
        return batchs_lis


    def get_batchs(self, integer):
        imgs = np.zeros((self.batch_size, 3, 224, 224))
        labels = np.zeros((self.batch_size,))

        while True:
            start = time.time()
            if not self.lines_queue.full():

                start = time.time()
                batch_lis = self.lines_queue.get(block=True)
                print "put_data_time: ", time.time() - start

                for i, id in enumerate(batch_lis):
                    try:
                        flag = id[0]
                        img_id = id[1]
                        imgrec = self.imgrecs[flag]

                        s = imgrec.read_idx(img_id)
                        header, img = mx.recordio.unpack(s)

                        img = cv2.imdecode(np.array(bytearray(img)), cv2.IMREAD_COLOR)
                        img = self.process(img)
                        label = header.label

                        imgs[i] = img
                        labels[i] = label
                    except Exception as e:
                        print str(repr(e))

                data = mx.nd.array(imgs)
                label = mx.nd.array(labels)

                self.imgs_queue.put([data, label], block=True)
            print "put_data_time: ", time.time() - start


    def reset(self):
        self.cursor_batch = -1
        random.shuffle(self.lines)

        for img_idx in self.lines:
            random.shuffle(img_idx)
        for i, line in enumerate(self.lines):
            self.lines_queue.put(line)

        pws = [mp.Process(target=self.get_batchs, args=(i * 100,)) for i in range(self.process_num)]

        for pw in pws:
            pw.daemon = True
            pw.start()


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
            data = cv2.resize(data, (shape[2], shape[1]))

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
        try:
            if self.iter_next():
                data, label = self.imgs_queue.get(block=True)
                return DataBatch(data=[data], label=[label], pad=self.getpad(), index=self.getindex())
            else:
                raise StopIteration
        except Exception as ex:
            print str(ex)


if __name__ == "__main__":

    val_list = ['f0d3f2be-1aef-46f4-82a3-81e6b58407cd',
                'f0d3f2be-1aef-46f4-82a3-81e6b58407cd',
                '1558240e-c77c-4920-b7c6-1b0d15c4c35c',
                '7e1ba7df-6061-4a97-94f7-0c1ea6a09611']

    data_dir = '/mnt/cephfs_wj/vc/common/rhea/datasets/'
    vals = []

    print 'start'

    for train in val_list:
        train_dir = os.path.join(data_dir, train)
        for file_name in os.listdir(train_dir):
            if file_name.endswith('.rec'):
                file_dir = os.path.join(train_dir, file_name.split('.')[0])
                vals.append(file_dir)

    print "rec_num: ", len(vals)

    val_dataiter = FileIter(
        data_dirs=vals,
        class_num=2,
        is_train=1,
        batch_size=512,
        process_num=3)

    while True:
        start = time.time()
        batch = val_dataiter.next()
        end = time.time()
        print "time: ", end - start