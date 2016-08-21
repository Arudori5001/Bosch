#coding:utf-8


class RawRecord:
    def __init__(self,id,input_vector,label):
        self.__id = id
        self.__input_vector = input_vector
        self.__label = label


    def get_id(self):
        return self.__id


    def get_input_vector(self):
        return self.__input_vector
    
    
    def set_input_vector(self, value):
        self.__input_vector = value


    def get_label(self):
        return self.__label
