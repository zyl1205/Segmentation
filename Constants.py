import os
import shutil

Image_size = (448, 448)
ROOT = '/home/zhouyilong/github/CE-Net-master/dataset/DRIVE'
BATCHSIZE_PER_CARD = 8
TOTAL_EPOCH = 150
INITAL_EPOCH_LOSS = 10000
NUM_EARLY_STOP = 20
NUM_UPDATE_LR = 10

BINARY_CLASS = 2