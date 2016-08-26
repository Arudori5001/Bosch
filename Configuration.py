#coding:utf-8

class Configuration:
    def __init__(self,
                 train_num, valid_num, test_num,
                 raw_train_table_name,raw_test_table_name,
                 processed_train_table_name,processed_valid_table_name,processed_test_table_name):
        self.__train_num = train_num
        self.__valid_num = valid_num
        self.__test_num = test_num
        self.__raw_train_table_name = raw_train_table_name
        self.__raw_test_table_name = raw_test_table_name
        self.__processed_train_table_name = processed_train_table_name
        self.__processed_valid_table_name = processed_valid_table_name
        self.__processed_test_table_name = processed_test_table_name
        
        
    def get_train_num(self):
        return self.__train_num
    
    
    def get_valid_num(self):
        return self.__valid_num
    
    
    def get_test_num(self):
        return self.__test_num        return self.__test_num


    def get_raw_train_table_name(self):
        return self.__raw_train_table_name


    def get_raw_test_table_name(self):
        return self.__raw_test_table_name


    def get_processed_train_table_name(self):
        return self.__processed_train_table_name


    def get_processed_valid_table_name(self):
        return self.__processed_valid_table_name


    def get_processed_test_table_name(self):
        return self.__processed_test_table_name
