#coding:utf-8

import abc

class IDisposable:
    __metaclass__ = abc.ABCMeta
    
    @staticmethod
    def dispose():
        raise NotImplementedError()
