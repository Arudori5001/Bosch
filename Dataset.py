#coding:utf-8

import cPickle

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
