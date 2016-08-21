#coding:utf-8

import click

from Dataset import Dataset
from SvmModel import SvmModel

@click.command()
@click.argument("train_dataset_file")
@click.argument("valid_dataset_file")
@click.argument("model_file")
def main(train_dataset_file, valid_dataset_file, model_file):
    train_dataset = Dataset.load(train_dataset_file)
    valid_dataset = Dataset.load(valid_dataset_file)
    model = SvmModel()
    model.learn(train_dataset, valid_dataset)
    model.save(model_file)
    
if __name__ == "__main__":
    main()
