#coding:utf-8

import click

from Configuration import Configuration
from RawDataset import RawDataset
from Preprocessor import Preprocessor

@click.command()
@click.argument("train_raw_file", nargs=1)
@click.argument("test_raw_file", nargs=1)
@click.argument("train_file", nargs=1)
@click.argument("valid_file", nargs=1)
@click.argument("test_file", nargs=1)
def main(train_raw_file,test_raw_file,train_file,valid_file,test_file):
    config = Configuration(
                           train_num=10,
                           valid_num=10,
                           test_num=10)
    
    train_raw_dataset = RawDataset()
    train_raw_dataset.load(train_raw_file, is_test=False, max_records=config.get_train_num()+config.get_valid_num())
    test_raw_dataset = RawDataset()
    test_raw_dataset.load(test_raw_file, is_test=True, max_records=config.get_test_num())
    
    preprocessor = Preprocessor(config)
    preprocessor.preprocess(train_raw_dataset, test_raw_dataset)
    train_dataset = preprocessor.get_train_dataset(train_raw_dataset)
    train_dataset.save(train_file)
    valid_dataset = preprocessor.get_valid_dataset(train_raw_dataset)
    valid_dataset.save(valid_file)
    test_dataset = preprocessor.get_test_dataset(test_raw_dataset)
    test_dataset.save(test_file)


if __name__ == "__main__":
    main()
