#coding:utf-8

import numpy as np

from MysqlDataset import MysqlDataset
from Record import Record

class LabeledMysqlDataset(MysqlDataset):

    def __init__(self, host, db_name, username, passward, table_name, id_table_name, chunksize):
        super.__init__(host, db_name, username, passward, table_name, chunksize)
        self.__id_table_name = id_table_name


    def __get_id_table_name(self):
        return self.__id_table_name


    def __get_table(self, offset, num):
        cursor =  self.__get_db_host().cursor()
        query = """select t.* from (select Id from {0} limit {1} offset {2}) as i, {3} as t
            where i.Id = t.Id;
        """.format(self.__get_id_table_name(), num, offset, self.__get_table_name())
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()

        result = np.array(result)
        return result


    def __get_records_with_range(self, offset, num):
        table = self.__get_table(offset, num)
        records = np.array([Record(id=row[0],input_vector=row[1:-1],label=row[-1]) for row in table])
        return records


    def __get_records_num(self):
        cursor =  self.__get_db_host().cursor()
        query = "select count(*) from {0}".format(self.__get_id_table_name())
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()

        return result[0][0]