#codinf:utf-8

from sklearn import svm

from Model import Model

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
        input_matrix = dataset.get_input_matrix()
        return self.__get_classifier().predict(input_matrix)
    
    
    def valid(self, dataset):
        raise NotImplementedError()
