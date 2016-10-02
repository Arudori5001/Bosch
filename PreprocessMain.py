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

    config = PreprocessConfiguration(
        train_num=2000,
        valid_num=2000,
        test_num=1e5,
        raw_train_table_name="train_numeric", raw_test_table_name="test_numeric",
        processed_train_table_name="valid_processed", processed_valid_table_name="valid_processed", processed_test_table_name="test_processed"
    )

    manager = DatabaseManager(config, host=host, db_name=db_name, username=username, passward=passward)
    preprocessor = Preprocessor(manager)
    preprocessor.preprocess()
    

if __name__ == "__main__":
    main()
