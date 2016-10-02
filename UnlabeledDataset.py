# coding:utf-8

import numpy as np

from AbstractDataset import AbstarctDataset
from Record import Record

class UnlabeledDataset(AbstarctDataset):

    def __init__(self, host, db_name, username, passward, table_name, chunksize):
        super.__init__(host, db_name, username, passward, table_name, chunksize)

    def __get_table(self, offset, num):
        cursor =  self.__get_db_host().cursor()
        query = """select * from {0} limit {1} offset {2}""".format(self.__get_table_name(), num, offset)
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()

        result = np.array(result)
        return result


    def __get_records(self, offset, num):
        table = self.__get_table(offset, num)
        records = np.array([Record(id=row[0],input_vector=row[1:],label=None) for row in table])
        return records


    def __get_records_num(self):
        cursor =  self.__get_db_host().cursor()
        query = "select count(*) from {0}".format(self.__get_table_name())
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()

        return result[0][0]