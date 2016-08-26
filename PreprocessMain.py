#coding:utf-8

import click

from Configuration import Configuration
from DatabaseManager import DatabaseManager
from Preprocessor import Preprocessor

@click.command()
def main():
    host = "localhost"
    db_name = "bosch"
    username = "root"
    passward = ""
    config = Configuration(
        train_num=20,
        valid_num=20,
        test_num=1e5,
        raw_train_table_name="train_numeric", raw_test_table_name="test_numeric",
        processed_train_table_name="valid_processed", processed_valid_table_name="valid_processed", processed_test_table_name="test_processed"
    )

    manager = DatabaseManager(config, host=host, db_name=db_name, username=username, passward=passward)
    preprocessor = Preprocessor(manager)
    preprocessor.preprocess()


if __name__ == "__main__":
    main()
