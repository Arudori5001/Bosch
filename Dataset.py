#coding:utf-8

import numpy as np
import MySQLdb

from IDisposable import IDisposable
from Record import Record

class Dataset(IDisposable):
    def __init__(self, is_test, host, db_name, username, passward, table_name, chunksize):
        self.__is_test = is_test
        self.__table_name = table_name
        self.__dbhost = MySQLdb.connect(host=host,db=db_name,user=username,passwd=passward,charset="utf8")
        self.__chunksize = chunksize


    def __get_db_host(self):
        return self.__dbhost
    
    
    def __get_table_name(self):
        return self.__table_name
    
    
    def __get_is_test(self):
        return self.__is_test
    
    
    def __get_chunksize(self):
        return self.__chunksize
    
    
    def __get_table(self, offset, num):
        cursor =  self.__get_db_host().cursor()
        query = "select * from {0} limit {1} offset {2}".format(self.__get_table_name(), num, offset)
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        
        result = np.array(result)
        return result
            
    
    def __get_records(self, offset, num):
        table = self.__get_table(offset, num)
        records = None
        if self.__get_is_test():
            records = np.array([Record(id=row[0],input_vector=row[1:],label=None) for row in table])
        else:
            records = np.array([Record(id=row[0],input_vector=row[1:-1],label=row[-1]) for row in table])
        return records
    
    
    def __get_records_num(self):
        cursor =  self.__get_db_host().cursor()
        query = "select count(*) from {0}".format(self.__get_table_name())
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        
        return result[0][0]
    
    
    def get_record_chunks_generator(self):
        chunksize = self.__get_chunksize()
        records_num = self.__get_records_num()
        
        for offset in range(0,records_num,chunksize):
            yield self.__get_records(offset, chunksize)
    
    
    def get_ids(self, records):
        return np.array([r.get_id() for r in records])
        

    def get_input_matrix(self, records):
        return np.array([r.get_input_vector() for r in records])

    
    def get_labels(self, records):
        return np.array([r.get_label() for r in records])
        
    
    def dispose(self):
        self.__get_db_host().close()
