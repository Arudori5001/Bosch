#coding:utf-8

from Model import Model

class NeuralNetModel(Model):
    
    def learn(self, train_dataset, valid_dataset):
        raise NotImplementedError()
    
    
    def predict(self, dataset):
        raise NotImplementedError()
    
        
    def valid(self, dataset):
        raise NotImplementedError()
