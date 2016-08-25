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
        for chunk in train_dataset.get_record_chunks_generator():
            input_matrix = train_dataset.get_input_matrix(chunk)
            labels = train_dataset.get_labels(chunk)
            self.__get_classifier().fit(input_matrix, labels)
        
        
    def predict(self, dataset):
        predictions = []
        for chunk in dataset.get_record_chunks_generator():
            ids = dataset.get_ids(chunk)
            input_matrix = dataset.get_input_matrix(chunk)
            actual_labels = dataset.get_labels(chunk)
            predicted_labels = self.__get_classifier().predict(input_matrix)
            
            for i,(id,a,p) in enumerate(zip(ids,actual_labels,predicted_labels)):
                prediction = Prediction(id=id,actual_label=a,predicted_label=p)
                predictions.append(prediction)
            
        prediction_collection = PredictionCollection(predictions)
        return prediction_collection
    
    
    def valid(self, dataset):
        raise NotImplementedError()
