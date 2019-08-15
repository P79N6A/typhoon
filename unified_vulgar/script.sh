#!/bin/bash
THIS_DIR="$( cd "$( dirname "$0" )" && pwd )"
# source $THIS_DIR/../download_latest_mxnet.sh
# To run on Arnold
cd $THIS_DIR

if [ -z $ARNOLD_OUTPUT ]; then
  ARNOLD_OUTPUT=$THIS_DIR/models
fi
MODELS_DIR=$ARNOLD_OUTPUT
if [ ! -d $MODELS_DIR ]; then
  mkdir $MODELS_DIR
fi
echo "MODELS_DIR" $MODELS_DIR

python train_fit.py "$@"