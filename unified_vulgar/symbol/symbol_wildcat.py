#
import mxnet as mx

def residual_unit(data, num_filter, stride, dim_match, name, bottle_neck=True,
                  bn_mom=0.9, workspace=512, memonger=False):
    """Return ResNet Unit symbol for building ResNet
    Parameters
    ----------
    data : str
        Input data
    num_filter : int
        Number of output channels
    bnf : int
        Bottle neck channels factor with regard to num_filter
    stride : tupe
        Stride used in convolution
    dim_match : Boolen
        True means channel number between input and output is the same, otherwise means differ
    name : str
        Base name of the operators
    workspace : int
        Workspace used in convolution operator
    """
    if bottle_neck:
        # the same as https://github.com/facebook/fb.resnet.torch#notes, a bit difference with origin paper
        bn1 = mx.sym.BatchNorm(data=data, fix_gamma=False, eps=2e-5, momentum=bn_mom, name=name + '_bn1')
        act1 = mx.sym.Activation(data=bn1, act_type='relu', name=name + '_relu1')
        conv1 = mx.sym.Convolution(data=act1, num_filter=int(num_filter*0.25), kernel=(1,1), stride=(1,1), pad=(0,0),
                                      no_bias=True, workspace=workspace, name=name + '_conv1')
        bn2 = mx.sym.BatchNorm(data=conv1, fix_gamma=False, eps=2e-5, momentum=bn_mom, name=name + '_bn2')
        act2 = mx.sym.Activation(data=bn2, act_type='relu', name=name + '_relu2')
        conv2 = mx.sym.Convolution(data=act2, num_filter=int(num_filter*0.25), kernel=(3,3), stride=stride, pad=(1,1),
                                      no_bias=True, workspace=workspace, name=name + '_conv2')
        bn3 = mx.sym.BatchNorm(data=conv2, fix_gamma=False, eps=2e-5, momentum=bn_mom, name=name + '_bn3')
        act3 = mx.sym.Activation(data=bn3, act_type='relu', name=name + '_relu3')
        conv3 = mx.sym.Convolution(data=act3, num_filter=num_filter, kernel=(1,1), stride=(1,1), pad=(0,0), no_bias=True,
                                   workspace=workspace, name=name + '_conv3')
        if dim_match:
            shortcut = data
        else:
            shortcut = mx.sym.Convolution(data=act1, num_filter=num_filter, kernel=(1,1), stride=stride, no_bias=True,
                                            workspace=workspace, name=name+'_sc')
        if memonger:
            shortcut._set_attr(mirror_stage='True')
        return conv3 + shortcut
    else:
        bn1 = mx.sym.BatchNorm(data=data, fix_gamma=False, momentum=bn_mom, eps=2e-5, name=name + '_bn1')
        act1 = mx.sym.Activation(data=bn1, act_type='relu', name=name + '_relu1')
        conv1 = mx.sym.Convolution(data=act1, num_filter=num_filter, kernel=(3,3), stride=stride, pad=(1,1),
                                      no_bias=True, workspace=workspace, name=name + '_conv1')
        bn2 = mx.sym.BatchNorm(data=conv1, fix_gamma=False, momentum=bn_mom, eps=2e-5, name=name + '_bn2')
        act2 = mx.sym.Activation(data=bn2, act_type='relu', name=name + '_relu2')
        conv2 = mx.sym.Convolution(data=act2, num_filter=num_filter, kernel=(3,3), stride=(1,1), pad=(1,1),
                                      no_bias=True, workspace=workspace, name=name + '_conv2')
        if dim_match:
            shortcut = data
        else:
            shortcut = mx.sym.Convolution(data=act1, num_filter=num_filter, kernel=(1,1), stride=stride, no_bias=True,
                                            workspace=workspace, name=name+'_sc')
        if memonger:
            shortcut._set_attr(mirror_stage='True')
        return conv2 + shortcut


def resnet(data, units, num_stage, filter_list, data_type='imagenet', bottle_neck=True,
           bn_mom=0.9, workspace=512, memonger=False):
    """Return ResNet symbol of cifar10 and imagenet
    Parameters
    ----------
    units : list
        Number of units in each stage
    num_stage : int
        Number of stage
    filter_list : list
        Channel size of each stage
    num_class : int
        Ouput size of symbol
    dataset : str
        Dataset type, only cifar10 and imagenet supports
    workspace : int
        Workspace used in convolution operator
    """
    num_unit = len(units)
    assert(num_unit == num_stage)

    data = mx.sym.BatchNorm(data=data, fix_gamma=True, eps=2e-5, momentum=bn_mom, name='bn_data')
    if data_type == 'cifar10':
        body = mx.sym.Convolution(data=data, num_filter=filter_list[0], kernel=(3, 3), stride=(1,1), pad=(1, 1),
                                  no_bias=True, name="conv0", workspace=workspace)
    elif data_type == 'imagenet':
        body = mx.sym.Convolution(data=data, num_filter=filter_list[0], kernel=(7, 7), stride=(2, 2), pad=(3, 3),
                                  no_bias=True, name="conv0", workspace=workspace)
        body = mx.sym.BatchNorm(data=body, fix_gamma=False, eps=2e-5, momentum=bn_mom, name='bn0')
        body = mx.sym.Activation(data=body, act_type='relu', name='relu0')
        body = mx.symbol.Pooling(data=body, kernel=(3, 3), stride=(2, 2), pad=(1, 1), pool_type='max')
    else:
         raise ValueError("do not support {} yet".format(data_type))
    steps = []
    for i in range(num_stage):
        body = residual_unit(body, filter_list[i+1], (1 if i == 0 else 2, 1 if i == 0 else 2), False,
                             name='stage%d_unit%d' % (i + 1, 1), bottle_neck=bottle_neck, workspace=workspace,
                             memonger=memonger)
        for j in range(units[i]-1):
            body = residual_unit(body, filter_list[i+1], (1, 1), True, name='stage%d_unit%d' % (i + 1, j + 2),
                                 bottle_neck=bottle_neck, workspace=workspace, memonger=memonger)
        steps.append(body)
    return steps


def get_symbol_wildcat(depth, num_class=2, M=8, k_max=1, k_min=1, alpha=0.6, loss_type='softmax'):
    if depth == 18:
        units = [2, 2, 2, 2]
    elif depth == 34:
        units = [3, 4, 6, 3]
    elif depth == 50:
        units = [3, 4, 6, 3]
    elif depth == 101:
        units = [3, 4, 23, 3]
    elif depth == 152:
        units = [3, 8, 36, 3]
    elif depth == 200:
        units = [3, 24, 36, 3]
    elif depth == 269:
        units = [3, 30, 48, 8]

    if depth <= 50:
        filter_list = [64, 64, 128, 256, 512]
    else:
        filter_list = [64, 256, 512, 1024, 2048]

    data = mx.sym.Variable(name='data')
    label = mx.sym.Variable(name='softmax')

    steps = resnet(data=data, units=units, num_stage=4, filter_list=filter_list)

    step = steps[-1]

    body = mx.sym.Convolution(data=step, num_filter=num_class*M, kernel=(1, 1), stride=(1, 1), pad=(0, 0), name="conv1*1", workspace=512) # ->(batch, num_class*M, h/32, w/32)

    # Class-wise pooling ->(batch, num_class, h/32, w/32)
    body = mx.symbol.reshape(body, (0, num_class, M, 0, 0))
    body = mx.symbol.sum(body, axis=2) / M

    # Spatial pooling ->(batch, num_class, h/32, w/32)
    body = mx.symbol.reshape(body, (0, num_class, -1))

    body_max = mx.symbol.sort(body, axis=2, is_ascend=0)
    body_min = mx.symbol.sort(body, axis=2, is_ascend=1)

    body_max = mx.symbol.slice_axis(body_max, axis=2, begin=0, end=k_max)
    body_min = mx.symbol.slice_axis(body_min, axis=2, begin=0, end=k_min)
    body = mx.symbol.sum(body_max, axis=2) / k_max + alpha * mx.symbol.sum(body_min, axis=2) / k_min

    if loss_type == 'softmax':
        pred_loss = mx.symbol.SoftmaxOutput(data=body, label=label, name='softmax_loss')
    return pred_loss


if __name__ == '__main__':
    net = get_symbol_wildcat(101, num_class=2, loss_type='softmax')
