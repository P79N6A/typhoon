#encoding: utf-8
import argparse
import logging
import os
import mxnet as mx
from config import config
from data.data_muth_rec import FileIter
from init import init_resnet
from symbol.symbol_resnet import resnet
from symbol.symbol_se_resnet import se_resnet
from symbol.symbol_unet import get_u_net
from solver_image import Solver
import shutil



n_class = config.num_cls
# model_dir = './model'
# logs_dir = './log'

model_dir = config.save_models
logs_dir = config.save_logs

save_models = config.save_models
save_logs = config.save_logs

def main(args):
    print(mx.__path__)
    print(mx.__version__)

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    ctx = [mx.gpu(int(i)) for i in args.gpus.split(',') if i.strip()]

    formatter = logging.Formatter('%(asctime)s - %(message)s')
    console = logging.StreamHandler()
    console.setFormatter(formatter)
    logger.addHandler(console)

    # save log file
    if not os.path.exists("./log"):
        os.mkdir("./log")
    hdlr = logging.FileHandler('./log/log-{}.log'.format(args.model))
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr)
    # print args messages

    logging.info(args)

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
    elif args.model_type == 'unet':
        model_symbol = get_u_net(num_class=n_class)

    model_prefix = os.path.join(save_models, args.prefix)
    model_save = os.path.join(model_dir, args.model)

    print "save_model: ", model_save

    _, old_args, old_auxs = mx.model.load_checkpoint(model_prefix, args.epoch)
    new_args, new_auxs = init_resnet(model_symbol, old_args, old_auxs,
                                     batch_size=args.batch_size, is_update=args.resume)
    train_dataiter = FileIter(
        data_dir=os.path.join(config.data_dir, args.train_file),
        rgb_mean=(0, 0, 0),
        class_num=n_class,
        is_train=1,
        batch_size=args.batch_size)

    val_dataiter = FileIter(
        data_dir=os.path.join(config.data_dir, args.val_file),
        rgb_mean=(0, 0, 0),
        class_num=n_class,
        is_train=2,
        batch_size=args.batch_size)

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
    # save model
    parser.add_argument('--model', default='se_resnet-50_4-28',
                        help='The type of model.')
    # load model name
    parser.add_argument('--prefix', default='se_resnet-50_4-28_face',
                        help='The prefix(include path) of model with mxnet format.')
    # load model epoch
    parser.add_argument('--epoch', type=int, default=54,
                        help='The epoch number of model. eg. 125, 0')
    # total_epoch
    parser.add_argument('--total_epoch', type=int, default=100,
                        help='training.total_epoch')
    # begin_epoch
    parser.add_argument('--begin_epoch', type=int, default=0,
                        help='training.begin_epoch')

    parser.add_argument('--train_file', type=str, default='face',
                        help='train_file_rec')

    parser.add_argument('--val_file', type=str, default='val',
                        help='val_file_rec')

    # model_type
    parser.add_argument('--model_type', default="se_resnet-50",
                        help='the init type of model')
    # batch_size
    parser.add_argument('--batch_size', type=int, default=2,
                        help='batch_size')
    # gpu
    parser.add_argument('--gpus', type=str, default="2,3",
                        help='gpu')
    # learning_rate
    parser.add_argument('--lr', type=float, default=0.01,
                        help='learning_rate')
    # momentum
    parser.add_argument('--momentum', type=float, default=0.9,
                        help='momentum')
    # wd
    parser.add_argument('--wd', type=float, default=0.0005,
                        help='wd')
    # loss_type
    parser.add_argument('--loss', type=str, default='softmax',
                        help='loss_type')

    # resume
    parser.add_argument('--resume', type=str, default=True,
                        help='true means continue training.')

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
    #save(args)
    print "train suss!!!"