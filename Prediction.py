#coding:utf-8

class Prediction:
    def __init__(self, id, actual_label, predicted_label):
        self.__id = id
        self.__actual_label = actual_label
        self.__predicted_label = predicted_label
    
    
    def get_id(self):
        return self.__id
    
    
    def get_actual_label(self):
        return self.__actual_label
        
    
    def get_predicted_label(self):
        return self.__predicted_label
