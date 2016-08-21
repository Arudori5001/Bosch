#coding:utf-8

class Prediction:
    def __init__(self, record, predicted_label):
        self.__record = record
        self.__predicted_label = predicted_label
    
    def get_record(self):
        return self.__record
    
    def get_predicted_label(self):
        return self.__predicted_label
