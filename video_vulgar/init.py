#encoding: utf-8
import mxnet as mx
import sys
import logging
sys.path.append('..')
from symbol.symbol_resnet import resnet
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def init_resnet(net_symbol, old_args, old_auxs, batch_size=1, is_update='False'):
    args = old_args.copy()
    auxs = old_auxs.copy()
    no_inits = ['data', 'softmax_label']

    if bool(is_update):
        # arg:参数
        # aux:bn层，每个batch 均值、标准差
        arg_names = net_symbol.list_arguments()
        aux_names = net_symbol.list_auxiliary_states()
        arg_shapes, _, aux_shapes = net_symbol.infer_shape(data=(batch_size, 3, 512, 512), softmax_label=(batch_size, ))

        # 正态分布，均值为0
        init_internal = mx.init.Normal(sigma=0.01)
        #
        init = mx.init.Xavier(factor_type="in", rnd_type='gaussian', magnitude=2)

        for k, v in zip(arg_names, arg_shapes):
            if k not in no_inits and (k not in args.keys() or args[k].shape != v):
                # print k
                args[k] = mx.nd.zeros(shape=v)
                if not k.endswith('bias'):
                    init_internal(k, args[k])

        for k, v in zip(aux_names, aux_shapes):
            if k not in no_inits and (k not in args.keys() or args[k].shape != v):
                # print k
                auxs[k] = mx.nd.zeros(shape=v)
                init(k, auxs[k])
    return args, auxs

if __name__ == '__main__':

    net = resnet(units=[3, 4, 6, 3], num_stage=4, num_class=2, filter_list=[64, 256, 512, 1024, 2048])
    model_prefix = './model/resnet-50'
    epoch = 0
    _, arg_params, aux_params = mx.model.load_checkpoint(model_prefix, epoch)

    new_params, new_params = init_resnet(net, arg_params, aux_params, is_update=True)
