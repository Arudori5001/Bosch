#coding:utf-8

import cPickle
import numpy as np

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
            
            
    def get_ids(self):
        return np.array([p.get_record().get_id() for p in self.get_predictions()])


    def get_input_matrix(self):
        return np.array([p.get_record().get_input_vector() for p in self.get_predictions()])


    def get_labels(self):
        return np.array([p.get_record().get_label() for p in self.get_predictions()])


    def get_predicted_labels(self):
        return np.array([p.get_predicted_label() for p in self.get_predictions()])
