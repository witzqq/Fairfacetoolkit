#!/bin/bash

if [ ! -d "logs" ]; then
    mkdir logs
fi

if [ ! -d "ckpt" ]; then
    mkdir ckpt
fi

export CUDA_VISIBLE_DEVICES='0,1'
python -u -m torch.distributed.launch --nproc_per_node=2 --nnodes=1 ./tasks/cifp/train_cifp.py > logs/$(date +%F-%H-%M-%S).log 2>&1