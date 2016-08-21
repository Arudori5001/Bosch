#coding:utf-8

import abc

from ISavable import ISavable
from _pyio import __metaclass__


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
    
    
    def load(self, filename):
        raise NotImplementedError()
    
    
    def save(self, filename):
        raise NotImplementedError()
