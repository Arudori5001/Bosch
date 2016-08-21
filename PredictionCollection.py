#coding:utf-8

from ISavable import ISavable

class PredictionCollection(ISavable):
    def __init__(self, predictions):
        self.__predictions = predictions
    
    
    def get_predictions(self):
        return self.__predictions
    
    
    def save(self, filename):
        raise NotImplementedError()
    
    
    def load(self, filename):
        raise NotImplementedError()
