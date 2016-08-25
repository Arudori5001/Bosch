#coding:utf-8

import abc

class IDisposable:
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def dispose(self):
        raise NotImplementedError()
