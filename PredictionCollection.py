#coding:utf-8

from ISavable import ISavable

class PredictionCollection(ISavable):
    def __init__(self, predictions):
        self.__predictions = predictions
    
    
    def get_predictions(self):
        return self.__predictions
    
    
    @staticmethod
    def load(filepath):
        obj = None
        with open(filepath, "rb") as f:
            obj = cPickle.load(f)
        return obj
    
    
    def save(self, filepath):
        with open(filepath, "wb") as f:
            cPickle.dump(self, f)
