#coding;utf-8

import abc

class ISavable(object):
    __metaclass__ = abc.ABCMeta
    
    @staticmethod
    @abc.abstractmethod
    def save(self, filename):
        raise NotImplementedError()
    
    @abc.abstractmethod
    def load(self, filename):
        raise NotImplementedError()
