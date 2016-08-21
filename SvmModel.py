#codinf:utf-8

import numpy as np
from sklearn import svm

from Model import Model
from Prediction import Prediction
from PredictionCollection import PredictionCollection


class SvmModel(Model):
    def __init__(self):
        self.__classifier = svm.SVC()
    
    
    def __get_classifier(self):
        return self.__classifier
    
    
    def learn(self, train_dataset, valid_dataset):
        input_matrix = train_dataset.get_input_matrix()
        labels = train_dataset.get_labels()
        
        self.__get_classifier().fit(input_matrix, labels)
        
        
    def predict(self, dataset):
        records = dataset.get_records()
        input_matrix = dataset.get_input_matrix()
        predicted_labels = self.__get_classifier().predict(input_matrix)
        predictions = np.array([Prediction(record=r,predicted_label=l) for r,l in zip(records, predicted_labels)])
        prediction_collection = PredictionCollection(predictions)
        return prediction_collection
    
    
    def valid(self, dataset):
        raise NotImplementedError()
