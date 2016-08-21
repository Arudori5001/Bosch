#coding:utf-8

import abc
import cPickle

from ISavable import ISavable


class Model(ISavable):
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def learn(self, train_dataset, valid_dataset):
        raise NotImplementedError()
    
    
    @abc.abstractmethod
    def predict(self, dataset):
        raise NotImplementedError()
    
    
    @abc.abstractmethod
    def valid(self, dataset):
        raise NotImplementedError()
    
    
    @staticmethod
    def load(filepath):
        obj = None
        with open(filepath, "rb") as f:
            obj = cPickle.load(f)
        return obj
    
    
    def save(self, filepath):
        with open(filepath, "wb") as f:
            cPickle.dump(self, f)
