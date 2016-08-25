#coding:utf-8

import click

from Dataset import Dataset
from SvmModel import SvmModel

@click.command()
@click.argument("model_file")
def main(model_file):
    host = "localhost"
    db_name = "bosch"
    username = "root"
    passward = ""
    train_table_name = "train_processed"
    valid_table_name = "valid_processed"
    chunksize = 10
    
    train_dataset = Dataset(is_test=False,host=host,db_name=db_name,username=username,passward=passward,table_name=train_table_name,chunksize=chunksize)
    valid_dataset = Dataset(is_test=False,host=host,db_name=db_name,username=username,passward=passward,table_name=valid_table_name,chunksize=chunksize)
    model = SvmModel()
    model.learn(train_dataset, valid_dataset)
    model.save(model_file)
    train_dataset.dispose()
    valid_dataset.dispose()
    
if __name__ == "__main__":
    main()
