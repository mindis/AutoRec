# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals

import tensorflow as tf
from abc import ABCMeta, abstractmethod
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

def data_load(dataset= "movielens",dataset_path = None, col_names = None, dtype=None, used_col_names=None, test_size=0.1 ):
    if dataset == "movielens":
        X, y = data_load_movielens(dataset_path, col_names, used_col_names, dtype )
    else:
        raise ValueError("Embedding_dim should be a string")
    train_X, train_y, val_X, val_y = data_spilt(X, y, test_size)
    return train_X, train_y, val_X, val_y



def data_load_movielens( dataset_path, col_names, used_col_names = None, dtype=None ):
    if used_col_names == None:
        used_col_names = col_names
    pd_data = pd.read_csv( dataset_path, sep = "::", header = None,names = col_names, dtype = dtype )
    pd_data = pd_data[ used_col_names ]
    X = pd_data.iloc[::,:-1].values
    y = pd_data.iloc[::, -1].values
    return X, y


def data_spilt( X, y, test_size = 0.1 ):
    train_X, val_X, train_y, val_y = train_test_split(X, y, test_size=test_size, random_state=0)
    return train_X, train_y, val_X, val_y


if __name__ == "__main__":
     data_load( dataset= "movielens", dataset_path ="./examples/datasets/ml-1m/ratings.dat", col_names = ["user_id", "item_id", "rating", "timestamp"], used_col_names = ["user_id", "item_id", "rating"] ,dtype={"user_id":np.int32, "item_id":np.int32, "rating":np.float32, "timestamp":np.int32}  )




