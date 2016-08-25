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
        return np.array([p.get_id() for p in self.get_predictions()])


    def get_actual_labels(self):
        return np.array([p.get_actual_label() for p in self.get_predictions()])


    def get_predicted_labels(self):
        return np.array([p.get_predicted_label() for p in self.get_predictions()])
    
    
    def __get_tp_num(self):
        actual_trues = (self.get_actual_labels() == 1)
        predicted_trues = (self.get_predicted_labels() == 1)
        return np.count_nonzero(np.logical_and(actual_trues, predicted_trues))
    
    
    def __get_fp_num(self):
        actual_falses = (self.get_actual_labels() == 0)
        predicted_trues = (self.get_predicted_labels() == 1)
        return np.count_nonzero(np.logical_and(actual_falses, predicted_trues))
    
    
    def __get_tn_num(self):
        actual_falses = (self.get_actual_labels() == 0)
        predicted_falses = (self.get_predicted_labels() == 0)
        return np.count_nonzero(np.logical_and(actual_falses, predicted_falses))
    
    
    def __get_fn_num(self):
        actual_trues = (self.get_actual_labels() == 1)
        predicted_falses = (self.get_predicted_labels() == 0)
        return np.count_nonzero(np.logical_and(actual_trues, predicted_falses))
    
    
    def get_accuracy(self):
        tp = self.__get_tp_num()
        fp = self.__get_fp_num()
        tn = self.__get_tn_num()
        fn = self.__get_fn_num()
        
        return float(tp + tn) / (tp + fp + tn + fn)
    
    
    """
    @summary: calcrate Matthew Correlation Coefficient(MCC)
    """
    def get_mcc(self):
        tp = self.__get_tp_num()
        fp = self.__get_fp_num()
        tn = self.__get_tn_num()
        fn = self.__get_fn_num()
        
        return float(tp * tn - fp * fn) / np.sqrt((tp + fp)*(tp + fn)*(tn + fp)*(tn + fn))
        
