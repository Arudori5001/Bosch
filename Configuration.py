#coding:utf-8

class Configuration:
    def __init__(self,
                 train_num,
                 valid_num,
                 test_num):
        self.__train_num = train_num
        self.__valid_num = valid_num
        self.__test_num = test_num
        
        
    def get_train_num(self):
        return self.__train_num
    
    
    def get_valid_num(self):
        return self.__valid_num
    
    
    def get_test_num(self):
        return self.__test_num
