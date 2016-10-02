#coding:utf-8

import click
import configparser

from PreprocessConfiguration import PreprocessConfiguration
from DatabaseManager import DatabaseManager
from Preprocessor import Preprocessor

@click.command()
def main():
    setting_parser = configparser.ConfigParser()
    setting_parser.read("setting.ini")
    host = setting_parser.get("database", "host_name")
    db_name = setting_parser.get("database", "db_name")
    username = setting_parser.get("database", "user_name")
    passward = setting_parser.get("database", "password")
    raw_train_table_name = setting_parser.get("database", "raw_train_table")
    raw_test_table_name = setting_parser.get("database", "raw_test_table")
    processed_train_table_name = setting_parser.get("database", "processed_train_table")
    processed_test_table_name = setting_parser.get("database", "processed_test_table")
    processed_train_id_table_name = setting_parser.get("database", "processed_train_id_table")
    processed_valid_id_table_name = setting_parser.get("database", "processed_valid_id_table")

    config = PreprocessConfiguration(
        raw_train_table_name=raw_train_table_name, raw_test_table_name=raw_test_table_name,
        processed_train_table_name=processed_train_table_name, processed_test_table_name=processed_test_table_name,
        processed_train_id_table_name=processed_train_id_table_name, processed_valid_id_table_name=processed_valid_id_table_name
    )

    manager = DatabaseManager(config, host=host, db_name=db_name, username=username, passward=passward)
    preprocessor = Preprocessor(manager)
    preprocessor.preprocess()


if __name__ == "__main__":
    main()
