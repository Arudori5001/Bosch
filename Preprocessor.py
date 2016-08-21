#coding:utf-8

import numpy as np

from Dataset import Dataset
from Record import Record

class Preprocessor:
    def __init__(self, configuration):
        self.__configuration = configuration
        
        
    def __get_configuration(self):
        return self.__configuration
    
    
    def preprocess(self, train_raw_dataset, test_raw_dataset):
        train_raw_dataset.fill_missing(0)
        test_raw_dataset.fill_missing(0)
        
    
    def get_train_dataset(self, train_raw_dataset):
        config = self.__get_configuration()
        
        train_raw_records = train_raw_dataset.get_records()
        train_processed_records = train_raw_records[:config.get_train_num()]
        train_processed_records = np.array([Record.create_from_raw_record(raw_record) for raw_record in train_processed_records])
        train_processed_dataset = Dataset(train_processed_records)
        return train_processed_dataset
    
    
    def get_valid_dataset(self, train_raw_dataset):
        config = self.__get_configuration()
        
        train_raw_records = train_raw_dataset.get_records()
        valid_processed_records = train_raw_records[config.get_train_num() : config.get_train_num() + config.get_valid_num()]
        valid_processed_records = np.array([Record.create_from_raw_record(raw_record) for raw_record in valid_processed_records])
        valid_processed_dataset = Dataset(valid_processed_records)
        return valid_processed_dataset
    
    
    def get_test_dataset(self, test_raw_dataset):
        config = self.__get_configuration()
        
        test_raw_records = test_raw_dataset.get_records()
        test_processed_records = test_raw_records[:config.get_test_num()]
        test_processed_records = np.array([Record.create_from_raw_record(raw_record) for raw_record in test_processed_records])
        test_processed_dataset = Dataset(test_processed_records)
        return test_processed_dataset
        
