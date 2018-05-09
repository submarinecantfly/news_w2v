import os
import os.path as osp
import numpy as np
from time import strftime, localtime
from easydict import EasyDict as edict
import yaml

__C = edict()
cfg = __C

__C.stop_words_path = 'logs/stop_words_ch.txt'
__C.words_path = 'logs/yuliao.txt'
__C.model_output_path = 'model/train_w2v.model'
__C.train_df_path = 'data/train_data.csv'
__C.test_df_path = 'data/test_data.csv'
__C.top20_path = 'output/top.csv'

#w2v模型训练参数

__C.train_size = 150
__C.train_window = 3
__C.train_min_count = 3
__C.train_workers = 3
