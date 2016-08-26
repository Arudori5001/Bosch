#coding:utf-8

import datetime

class Preprocessor:
    def __init__(self, databasemanager):
        self.__database_manager = databasemanager
        
        
    def __get_database_maneger(self):
        return self.__database_manager
    
    
    def preprocess(self):
        manager = self.__get_database_maneger()
        config = manager.get_configuration()

        manager.truncate(config.get_processed_train_table_name())
        manager.truncate(config.get_processed_valid_table_name())
        manager.truncate(config.get_processed_test_table_name())

        manager.pick_up_randomly_from_raw_train()
        manager.copy(config.get_raw_test_table_name(), config.get_processed_test_table_name())
