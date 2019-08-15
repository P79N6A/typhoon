import mxnet as mx
from symbol.symbol_resnet import resnet

sym = resnet(units=[3, 4, 6, 3], num_stage=4, filter_list=[64, 256, 512, 1024, 2048], num_class=2, batch_size=128)

model_prefix = "./model/resnet-50_fk_224"

_, arg_params, aux_params = mx.model.load_checkpoint(model_prefix, 5)
mod = mx.mod.Module(symbol=sym,
                    data_names=['data', 'avatar', 'nickname'],
                    label_names=['softmax_label'],
                    context=mx.gpu(0))
#mod = mx.mod.Module(symbol=sym, context=mx.gpu(0))
mod.bind(data_shapes=[('data', (1, 3, 224, 224)),
                      ('avatar', (1, 50, 300)),
                      ('nickname', (1, 50, 300))])


