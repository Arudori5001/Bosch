#coding:utf-8

class Sampler:
    def __init__(self, databasemanager):
        self.__database_manager = databasemanager


    def __get_database_maneger(self):
        return self.__database_manager


    def random_sample(self, train_num, valid_num):
        manager = self.__get_database_maneger()
        config = manager.get_configuration()

        manager.truncate(config.get_processed_train_id_table_name())
        manager.truncate(config.get_processed_valid_id_table_name())
        manager.random_sample(train_num,valid_num)