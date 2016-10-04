#coding:utf-8

from Prediction import Prediction

class ClassificationPrediction(Prediction):

    def __init__(self, id, actual_label, predicted_label, score):
        super(ClassificationPrediction,self).__init__(id, actual_label, predicted_label)
        self.__score = score


    def get_score(self):
        return self.__score