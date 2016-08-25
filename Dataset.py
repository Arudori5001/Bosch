#coding:utf-8

import numpy as np

from IDisposable import IDisposable

class Dataset(IDisposable):
    def __init__(self, host, db, user, passward):
        raise NotImplementedError()


    def get_input_matrix(self):
        raise NotImplementedError()

    
    def get_labels(self):
        raise NotImplementedError()
