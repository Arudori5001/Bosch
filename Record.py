#coding:utf-8

class Record:
    
    def __init__(self, id, input_vector, label):
        self.__id = id
        self.__input_vector = input_vector
        self.__label = label
        
        
    @staticmethod
    def create_from_raw_record(raw_record):
        return Record(id=raw_record.get_id(), input_vector=raw_record.get_input_vector(), label=raw_record.get_label())
        
        
    def get_id(self):
        return self.__id
        
        
    def get_input_vector(self):
        return self.__input_vector
    
    
    def get_label(self):
        return self.__label
