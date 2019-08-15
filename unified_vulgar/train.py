#encoding: utf-8
import argparse
import logging
import os
import mxnet as mx
from config import config
from data.data_muth_recs_muth import FileIter
#from data.data_muth_recs import FileIter
from init import init_resnet
from symbol.symbol_resnet import resnet
from symbol.symbol_se_resnet import se_resnet
from solver import Solver
import shutil

def main(args):
    print(mx.__path__)
    print(mx.__version__)

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    model_dir = './model'
    log_dir = './log'


    ctx = [mx.gpu(int(i)) for i in args.gpus]

    formatter = logging.Formatter('%(asctime)s - %(message)s')
    console = logging.StreamHandler()
    console.setFormatter(formatter)
    logger.addHandler(console)

    # save log file
    if not os.path.exists(log_dir):
        os.mkdir(log_dir)
    hdlr = logging.FileHandler('./log/log-{}.log'.format(args.model))
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr)
    # print args messages

    logging.info(args)

    n_class = args.n_class

    if not os.path.exists(model_dir):
        os.mkdir(model_dir)

    if args.model_type == 'resnet-50':
        model_symbol = resnet(units=[3, 4, 6, 3], num_stage=4, loss_type=args.loss,
                              filter_list=[64, 256, 512, 1024, 2048], num_class=n_class)
    elif args.model_type == 'se_resnet-50':
        model_symbol = se_resnet(units=[3, 4, 6, 3], num_stage=4, loss_type=args.loss,
                                 filter_list=[64, 256, 512, 1024, 2048], num_class=n_class)
    elif args.model_type == 'resnet-101':
        model_symbol = resnet(units=[3, 4, 23, 3], num_stage=4, loss_type=args.loss,
                              filter_list=[64, 256, 512, 1024, 2048], num_class=n_class)
    elif args.model_type == 'se_resnet-101':
        model_symbol = se_resnet(units=[3, 4, 23, 3], num_stage=4, loss_type=args.loss,
                                 filter_list=[64, 256, 512, 1024, 2048], num_class=n_class)
    elif args.model_type == 'resnet-152':
        model_symbol = resnet(units=[3, 8, 36, 3], num_stage=4, loss_type=args.loss,
                              filter_list=[64, 256, 512, 1024, 2048], num_class=n_class)

    model_prefix = os.path.join(args.model_dir, args.prefix)
    model_save = os.path.join(model_dir, args.model)

    _, old_args, old_auxs = mx.model.load_checkpoint(model_prefix, args.epoch)
    new_args, new_auxs = init_resnet(model_symbol, old_args, old_auxs,
                                     batch_size=args.batch_size, is_update=args.resume)
    trains = []
    vals = []
    for train in args.train_list:
        train_dir = os.path.join(args.data_dir, train)
        for file_name in os.listdir(train_dir):
            if file_name.endswith('.rec'):
                file_dir = os.path.join(train_dir, file_name.split('.')[0])
                trains.append(file_dir)

    for train in args.val_list:
        train_dir = os.path.join(args.data_dir, train)
        for file_name in os.listdir(train_dir):
            if file_name.endswith('.rec'):
                file_dir = os.path.join(train_dir, file_name.split('.')[0])
                vals.append(file_dir)


    train_dataiter = FileIter(
        data_dirs=trains,
        class_num=n_class,
        is_train=1,
        batch_size=args.batch_size,
        process_num=20)

    val_dataiter = FileIter(
        data_dirs=vals,
        class_num=n_class,
        is_train=2,
        batch_size=args.batch_size,
        process_num=1)

    model = Solver(
        ctx=ctx,
        symbol=model_symbol,
        arg_params=new_args,
        aux_params=new_auxs,
        begin_epoch=args.begin_epoch,
        num_epoch=args.total_epoch,
        learning_rate=args.lr,
        momentum=args.momentum,
        wd=args.wd,

        model_prefix=model_prefix,
        batch_size=args.batch_size,
        n_class=n_class)

    model.fit(
        train_data=train_dataiter,
        eval_data=val_dataiter,
        batch_end_callback=mx.callback.Speedometer(args.batch_size, 10, auto_reset=False),
        epoch_end_callback=mx.callback.do_checkpoint(model_save))

def parse_args():
    parser = argparse.ArgumentParser(description='Convert vgg16 model to vgg16fc model.')

    # load model name
    parser.add_argument('--prefix', default='resnet-50',
                        help='The prefix(include path) of model with mxnet format.')
    # load model epoch
    parser.add_argument('--epoch', type=int, default=0,
                        help='The epoch number of model. eg. 125, 0')

    # load data dir
    parser.add_argument('--data_dir', type=str, default='/mnt/cephfs_wj/vc/common/rhea/datasets/',
                        help='The epoch number of model. eg. 125, 0')
    # load train_list
    parser.add_argument('--train_list', nargs='*', default=['731fe7ab-73dd-44bc-b6d8-45803a450909',
                                                            '70e92529-6823-4a0f-af0e-a97dba765f79',
                                                            '82bf05d9-978b-402a-b131-7908585347d9',
                                                            '1558240e-c77c-4920-b7c6-1b0d15c4c35c',
                                                            'b004490e-1008-4a3f-8eb8-bbd04956bdc6',
                                                            '580aa6d7-d19a-4176-9784-632a35a29574',
                                                            '0d8c024c-a08d-4e31-b6e1-cc701ff9625b',
                                                            '83b27ca6-7f0e-412d-8189-f794238151fd',
                                                            '7e1ba7df-6061-4a97-94f7-0c1ea6a09611'],

                        help='The epoch number of model. eg. 125, 0')
    # load val_list
    parser.add_argument('--val_list', nargs='*', default=['f0d3f2be-1aef-46f4-82a3-81e6b58407cd'],
                        help='The epoch number of model. eg. 125, 0')

    # save model name
    parser.add_argument('--model', default='resnet-50_5-15',
                        help='The type of fcn-xs model.')
    # save model dir
    parser.add_argument('--model_dir', type=str, default='/mnt/cephfs_wj/vc/wangxiyu/pro/mxnet/models/unified_vulgar',
                        help='The epoch number of model. eg. 125, 0')

    # save log dir
    parser.add_argument('--log_dir', type=str, default='/mnt/cephfs_wj/vc/wangxiyu/pro/mxnet/logs/unified_vulgar')

    # total_epoch
    parser.add_argument('--total_epoch', type=int, default=4, help='training.total_epoch')
    # begin_epoch
    parser.add_argument('--begin_epoch', type=int, default=0, help='training.begin_epoch')
    # model_type
    parser.add_argument('--model_type', default="resnet-50", help='the init type of model')
    # batch_size
    parser.add_argument('--batch_size', type=int, default=16, help='batch_size')
    # gpu
    parser.add_argument('--gpus', nargs='*', default=['0', '1', '2', '3'], help='gpu')

    # n_class
    parser.add_argument('--n_class', type=int, default=2, help='n_class')
    # learning_rate
    parser.add_argument('--lr', type=float, default=0.001, help='learning_rate')
    # momentum
    parser.add_argument('--momentum', type=float, default=0.9, help='momentum')
    # wd
    parser.add_argument('--wd', type=float, default=0.0005, help='wd')
    # loss_type
    parser.add_argument('--loss', type=str, default='softmax', help='loss_type')
    # resume
    parser.add_argument('--resume', type=str, default=True, help='true means continue training.')

    args = parser.parse_args()
    return args


def save(args):
    print("start save models")
    for name in os.listdir(model_dir):
        if name.startswith(args.prefix):
            srcfile = os.path.join(model_dir, name)
            dstfile = os.path.join(save_models, name)
            mycopyfile(srcfile, dstfile)

    for name in os.listdir(logs_dir):
        if name.startswith(args.prefix):
            srcfile = os.path.join(logs_dir, name)
            dstfile = os.path.join(save_logs, name)
            mycopyfile(srcfile, dstfile)


def mycopyfile(srcfile, dstfile):
    if not os.path.isfile(srcfile):
        print "%s not exist!" % (srcfile)
    else:
        fpath, fname = os.path.split(dstfile)
        if not os.path.exists(fpath):
            os.makedirs(fpath)
        shutil.copyfile(srcfile, dstfile)
        print "copy %s -> %s" % (srcfile, dstfile)


if __name__ == "__main__":
    args = parse_args()
    main(args)
    save(args)
    print "train suss!!!"