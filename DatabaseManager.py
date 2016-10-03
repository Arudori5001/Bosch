# coding:utf-8

import MySQLdb
import numpy as np

class DatabaseManager:

    def __init__(self,
                 configuration,
                 host, db_name, username, passward):
        self.__configuraiton = configuration
        self.__db_host = MySQLdb.connect(host=host,db=db_name,user=username,passwd=passward,charset="utf8")


    def get_configuration(self):
        return self.__configuraiton


    def __get_db_host(self):
        return self.__db_host


    def truncate(self,table_name):
        db_host = self.__get_db_host()
        cursor = db_host.cursor()
        query = "truncate table {0}".format(table_name)
        cursor.execute(query)
        db_host.commit()
        cursor.close()


    def random_sample(self, train_num, valid_num):
        config = self.get_configuration()
        db_host = self.__get_db_host()
        cursor =  db_host.cursor()
        categories = self.__get_label_names()
        categories_num = len(categories)
        single_category_train_num = train_num / categories_num
        single_category_valid_num = valid_num / categories_num

        insert_query = """
            insert into {0} select id from {1} where label = '{2}' limit {3} offset {4};
            """
        for cat in categories:
            cursor.execute(insert_query.format(config.get_processed_train_id_table_name(),
                                               config.get_raw_train_table_name(),
                                               cat,
                                               single_category_train_num,
                                               0))
        for cat in categories:
            cursor.execute(insert_query.format(config.get_processed_valid_id_table_name(),
                                               config.get_raw_train_table_name(),
                                               cat,
                                               single_category_valid_num,
                                               single_category_train_num))
        db_host.commit()
        cursor.close()


    def copy(self, source, dest):
        db_host = self.__get_db_host()
        cursor =  db_host.cursor()
        query = """
            insert into {0} select * from {1};
            """.format(dest, source)
        cursor.execute(query)
        db_host.commit()
        cursor.close()


    def __get_label_names(self):
        config = self.get_configuration()
        relation_table = config.get_label_relation_table_name()
        db_host = self.__get_db_host()
        cursor =  db_host.cursor()
        query = """
            select label_name from {0};
            """.format(relation_table)
        cursor.execute(query.format(config.get_label_relation_table_name()))
        result = cursor.fetchall()
        cursor.close()

        return np.array([r[0] for r in result])


    def normalize(self):
        raise NotImplementedError()


    def remove_all_same_attributes(self):
        raise NotImplementedError()




