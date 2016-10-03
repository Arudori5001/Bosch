#coding:utf-8

import configparser


class PreprocessConfiguration:
    def __init__(self,
                 raw_train_table_name,raw_test_table_name,
                 processed_train_table_name,processed_test_table_name,
                 processed_train_id_table_name, processed_valid_id_table_name,
                 label_relation_table_name):
        self.__raw_train_table_name = raw_train_table_name
        self.__raw_test_table_name = raw_test_table_name
        self.__processed_train_table_name = processed_train_table_name
        self.__processed_test_table_name = processed_test_table_name
        self.__processed_train_id_table_name = processed_train_id_table_name
        self.__processed_valid_id_table_name = processed_valid_id_table_name
        self.__label_relation_table_name = label_relation_table_name


    def get_raw_train_table_name(self):
        return self.__raw_train_table_name


    def get_raw_test_table_name(self):
        return self.__raw_test_table_name


    def get_processed_train_table_name(self):
        return self.__processed_train_table_name


    def get_processed_test_table_name(self):
        return self.__processed_test_table_name


    def get_processed_train_id_table_name(self):
        return self.__processed_train_id_table_name


    def get_processed_valid_id_table_name(self):
        return self.__processed_valid_id_table_name


    def get_label_relation_table_name(self):
        return self.__label_relation_table_name