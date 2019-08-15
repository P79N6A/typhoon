from easydict import EasyDict as edict
import os
import numpy as np

config = edict()
config.num_cls = 2

config.mean = np.array([123.68, 116.28, 103.53])
config.std = np.array([58.395, 57.12, 57.375])

config.root = '/mnt/cephfs_wj/vc'

config.root_dir = os.path.join(config.root, 'wangxiyu/pro/mxnet/fk_img_lab')
config.data_dir = os.path.join(config.root, 'wangxiyu/data/fk_img_lab/rec')

config.save_models = os.path.join(config.root, 'wangxiyu/pro/mxnet/models/fk')
config.save_logs = os.path.join(config.root, 'wangxiyu/pro/mxnet/logs/fk')

