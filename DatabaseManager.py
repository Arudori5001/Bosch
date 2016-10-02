# coding:utf-8

import MySQLdb


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
        pos_table_name = "pos_ids"
        neg_table_name = "neg_ids"
        half_records_num = (train_num + valid_num) / 2
        db_host = self.__get_db_host()

        cursor =  db_host.cursor()
        create_table_query = """
            create table {0}
            (Id int(11) unsigned NOT NULL primary key);
            """
        cursor.execute(create_table_query.format(pos_table_name))
        cursor.execute(create_table_query.format(neg_table_name))

        prepare_ids_query = """
            insert into {0}
                select Id from {1} where Response = {2} order by rand() limit {3};
            """
        cursor.execute(prepare_ids_query.format(pos_table_name,
                                           config.get_raw_train_table_name(),
                                           1,
                                           half_records_num))
        cursor.execute(prepare_ids_query.format(neg_table_name,
                                           config.get_raw_train_table_name(),
                                           0,
                                           half_records_num))

        insert_query = """
            insert into {0}
                select Id from {1} limit {2} offset {3};
        """
        cursor.execute(insert_query.format(config.get_processed_train_id_table_name(),
                                           pos_table_name,
                                           train_num / 2,
                                           0))
        cursor.execute(insert_query.format(config.get_processed_train_id_table_name(),
                                           neg_table_name,
                                           train_num / 2,
                                           0))
        cursor.execute(insert_query.format(config.get_processed_valid_id_table_name(),
                                           pos_table_name,
                                           valid_num / 2,
                                           train_num / 2))
        cursor.execute(insert_query.format(config.get_processed_valid_id_table_name(),
                                           neg_table_name,
                                           valid_num / 2,
                                           train_num / 2))

        drop_table_query = """
            drop table {0};
        """
        cursor.execute(drop_table_query.format(pos_table_name))
        cursor.execute(drop_table_query.format(neg_table_name))

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


    def normalize(self):
        raise NotImplementedError()


    def remove_all_same_attributes(self):
        raise NotImplementedError()




