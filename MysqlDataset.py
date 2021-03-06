# coding:utf-8

import abc
import numpy as np
import MySQLdb

from AbstractDataset import AbstarctDataset
from IDisposable import IDisposable


class MysqlDataset(AbstarctDataset,IDisposable):
    __metaclass__ = abc.ABCMeta

    def __init__(self, host, db_name, username, passward, table_name, chunksize):
        self.__table_name = table_name
        self.__dbhost = MySQLdb.connect(host=host, db=db_name, user=username, passwd=passward, charset="utf8")
        self.__chunksize = chunksize

    def get_db_host(self):
        return self.__dbhost

    def get_table_name(self):
        return self.__table_name

    def get_chunksize(self):
        return self.__chunksize

    @abc.abstractmethod
    def get_table(self, offset, num):
        raise NotImplementedError()

    @abc.abstractmethod
    def get_records_with_range(self, offset, num):
        raise NotImplementedError()

    @abc.abstractmethod
    def get_records_num(self):
        raise NotImplementedError()

    def get_records(self):
        num = self.get_records_num()
        return self.get_records_with_range(0,num)

    def get_record_chunks_generator(self):
        chunksize = self.get_chunksize()
        records_num = self.get_records_num()

        for offset in range(0, records_num, chunksize):
            yield self.get_records_with_range(offset, chunksize)

    def get_ids_from_chunk(self, chunk):
        return np.array([r.get_id() for r in chunk])

    def get_input_matrix_from_chunk(self, chunk):
        return np.array([r.get_input_vector() for r in chunk])

    def get_labels_from_chunk(self, chunk):
        return np.array([r.get_label() for r in chunk])

    def dispose(self):
        self.get_db_host().close()
