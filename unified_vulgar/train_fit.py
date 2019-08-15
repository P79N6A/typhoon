#encoding: utf-8
import argparse
import logging
import os
import mxnet as mx
from data.data_muth_recs import FileIter
from init import init_resnet

from symbol.symbol_resnet import get_symbol_resnet
from symbol.symbol_se_resnet import get_symbol_se_resnet
from symbol.symbol_resnet_fpn import get_symbol_resnet_fpn
from symbol.symbol_resnet_gap import get_symbol_resnet_gap

from metrics.crossEntropy import CrossEntropy
from metrics.recall import Recall
from metrics.precision import Precision
from metrics.accuracy import Accuracy

def parse_args():
    parser = argparse.ArgumentParser(description='Convert vgg16 model to vgg16fc model.')

    # load model name
    parser.add_argument('--prefix', default='resnet101_5.27_no_pre_sgd')
    # load model epoch
    parser.add_argument('--epoch', type=int, default=21)
    # load data dir
    parser.add_argument('--data_dir', type=str, default='/mnt/cephfs_wj/vc/common/rhea/datasets/')
    # load train_list
    parser.add_argument('--train_list', nargs='*', default=['7e1ba7df-6061-4a97-94f7-0c1ea6a09611',
                                                            '83b27ca6-7f0e-412d-8189-f794238151fd',
                                                            '0d8c024c-a08d-4e31-b6e1-cc701ff9625b',
                                                            '580aa6d7-d19a-4176-9784-632a35a29574',
                                                            'b004490e-1008-4a3f-8eb8-bbd04956bdc6',
                                                            '1558240e-c77c-4920-b7c6-1b0d15c4c35c',
                                                            '82bf05d9-978b-402a-b131-7908585347d9',
                                                            '70e92529-6823-4a0f-af0e-a97dba765f79',
                                                            '731fe7ab-73dd-44bc-b6d8-45803a450909',
                                                            '06229020-bace-4f8f-860a-20da8237cae0',
                                                            '0c759f32-01ef-45c4-a931-7f9d695cfaa2'])
    # load val_list
    parser.add_argument('--val_list', nargs='*', default=['f0d3f2be-1aef-46f4-82a3-81e6b58407cd'])

    # save model name
    parser.add_argument('--model', type=str, default='resnet-101_6-14')

    # save model dir
    parser.add_argument('--model_dir', type=str, default='/mnt/cephfs_wj/vc/wangxiyu/pro/mxnet/models/unified_vulgar/')

    # save log dir
    parser.add_argument('--log_dir', type=str, default='/mnt/cephfs_wj/vc/wangxiyu/pro/mxnet/logs/unified_vulgar/')

    # total_epoch
    parser.add_argument('--total_epoch', type=int, default=100)
    # begin_epoch
    parser.add_argument('--begin_epoch', type=int, default=0)
    # model_type
    parser.add_argument('--model_type', type=str, default='resnet-101')
    # batch_size
    parser.add_argument('--batch_size', type=int, default=32)
    # gpu
    parser.add_argument('--gpus', nargs='*', default=['0', '1', '2', '3'])

    # n_class
    parser.add_argument('--n_class', type=int, default=2)
    # learning_rate
    parser.add_argument('--lr', type=float, default=0.001)
    # momentum
    parser.add_argument('--momentum', type=float, default=0.9)
    # wd
    parser.add_argument('--wd', type=float, default=0.0005)
    # loss_type
    parser.add_argument('--loss', type=str, default='softmax')
    # optimizer
    parser.add_argument('--optimizer', type=str, default='sgd')
    # resume
    parser.add_argument('--resume', type=str, default=True)

    args = parser.parse_args()
    return args

def main(args):
    print(mx.__path__)
    print(mx.__version__)

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    model_dir = args.model_dir
    log_dir = args.log_dir

    ctx = [mx.gpu(int(i)) for i in args.gpus]

    formatter = logging.Formatter('%(asctime)s - %(message)s')
    console = logging.StreamHandler()
    console.setFormatter(formatter)
    logger.addHandler(console)

    # save log file
    if not os.path.exists(log_dir):
        os.mkdir(log_dir)
    hdlr = logging.FileHandler(os.path.join(log_dir, 'log-{}.log'.format(args.model)))
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr)

    logging.info(args)

    n_class = int(args.n_class)
    batch_size = args.batch_size

    if not os.path.exists(model_dir):
        os.mkdir(model_dir)

    model_type, depth = args.model_type.split('-')
    print model_type, depth
    if model_type == 'resnet':
        model_symbol = get_symbol_resnet(depth=int(depth), num_class=n_class, loss_type=args.loss)
    elif model_type == 'se_resnet':
        model_symbol = get_symbol_se_resnet(depth=int(depth), num_class=n_class, loss_type=args.loss)
    elif model_type == 'resnet_fpn':
        model_symbol = get_symbol_resnet_fpn(depth=int(depth), num_class=n_class, loss_type=args.loss)
    elif model_type == 'resnet_gap':
        model_symbol = get_symbol_resnet_gap(depth=int(depth), num_class=n_class, loss_type=args.loss)
    else:
        model_symbol = None

    model_prefix = os.path.join(args.model_dir, args.prefix)
    model_save = os.path.join(model_dir, args.model)

    old_symbol, old_args, old_auxs = mx.model.load_checkpoint(model_prefix, args.epoch)

    if model_symbol is None:
        model_symbol = old_symbol
        logging.info("load_symbol: " + args.prefix)
    else:
        logging.info("load_symbol: " + args.model_type)

    arg_params, aux_params = init_resnet(net_symbol=model_symbol,
                                         old_args=old_args,
                                         old_auxs=old_auxs,
                                         batch_size=args.batch_size,
                                         is_update=args.resume)

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

    logging.info("train_rec_num: " + str(len(trains)))
    logging.info("val_rec_num: " + str(len(vals)))

    train_dataiter = FileIter(
        data_dirs=trains,
        class_num=n_class,
        is_train=1,
        batch_size=batch_size)

    val_dataiter = FileIter(
        data_dirs=vals,
        class_num=n_class,
        is_train=2,
        batch_size=batch_size)

    metric = mx.metric.CompositeEvalMetric()
    metric.add(Accuracy())
    metric.add(Recall())
    metric.add(Precision())
    metric.add(CrossEntropy())

    lr_iters = [int(iepoch * 10000 / batch_size)
                for iepoch in range(1, args.total_epoch - args.begin_epoch)]
    lr_scheduler = mx.lr_scheduler.MultiFactorScheduler(lr_iters, 0.99)

    if args.optimizer == 'adam':
        optimizer_params = {'learning_rate': args.lr,
                            'lr_scheduler': lr_scheduler}
    elif args.optimizer == 'sgd':
        optimizer_params = {
            'lr_scheduler': lr_scheduler,
            'learning_rate': args.lr,
            'clip_gradient': 5,
            'momentum': 0.9,
            'wd': 0.0005}

    mod = mx.mod.Module(symbol=model_symbol,
                        context=ctx,
                        data_names=['data'],
                        label_names=['softmax'])
    logging.info("load_model success!")

    mod.fit(train_data=train_dataiter,
            eval_data=val_dataiter,
            begin_epoch=args.begin_epoch,
            num_epoch=args.total_epoch,
            batch_end_callback=mx.callback.Speedometer(batch_size, 10, auto_reset=True),
            epoch_end_callback=mx.callback.do_checkpoint(model_save),
            kvstore='device',
            optimizer=args.optimizer,
            optimizer_params=optimizer_params,
            eval_metric=metric,
            arg_params=arg_params,
            aux_params=aux_params,
            allow_missing=True)

if __name__ == "__main__":
    args = parse_args()
    main(args)
    print "train suss!!!"