#coding:utf-8

import cPickle
import numpy as np

from ISavable import ISavable

class Dataset(ISavable):
    def __init__(self, records):
        self.__records = records
        
    
    def get_records(self):
        return self.__records
    
    
    @staticmethod
    def load(filepath):
        obj = None
        with open(filepath, "rb") as f:
            obj = cPickle.load(f)
        return obj
    
    
    def save(self, filepath):
        with open(filepath, "wb") as f:
            cPickle.dump(self, f)


    def get_input_matrix(self):
        return np.array([r.get_input_vector() for r in self.get_records()])

    
    def get_labels(self):
        return np.array([r.get_label() for r in self.get_records()])
