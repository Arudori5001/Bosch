#coding:utf-8

import click
import configparser
import logging
import logging.config

from LabeledMysqlDataset import LabeledMysqlDataset
from SvmModel import SvmModel

@click.command()
@click.argument("model_file")
def main(model_file):
    logging.config.fileConfig("LogSetting.ini")
    logger = logging.getLogger(__name__)
    logger.info("start : " + __file__)

    setting_parser = configparser.ConfigParser()
    setting_parser.read("setting.ini")
    host = setting_parser.get("database", "host_name")
    db_name = setting_parser.get("database", "db_name")
    username = setting_parser.get("database", "user_name")
    passward = setting_parser.get("database", "password")
    train_table_name = setting_parser.get("database", "processed_train_table")
    train_id_table_name = setting_parser.get("database", "processed_train_id_table")
    valid_id_table_name = setting_parser.get("database", "processed_valid_id_table")


    chunksize = 10 ** 6
    
    train_dataset = LabeledMysqlDataset(host=host, db_name=db_name, username=username, passward=passward, table_name=train_table_name, id_table_name=train_id_table_name, chunksize=chunksize)
    valid_dataset = LabeledMysqlDataset(host=host, db_name=db_name, username=username, passward=passward, table_name=train_table_name, id_table_name=valid_id_table_name, chunksize=chunksize)
    model = SvmModel()
    model.learn(train_dataset, valid_dataset)
    model.save(model_file)
    train_dataset.dispose()
    valid_dataset.dispose()

    logger.info("end : " + __file__)
    
if __name__ == "__main__":
    main()
