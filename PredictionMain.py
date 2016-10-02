#coding;utf-8

import click
import configparser
import logging
import logging.config

from Model import Model
from LabeledDataset import LabeledDataset
from UnlabeledDataset import UnlabeledDataset

@click.command()
@click.argument("table_name")
@click.argument("id_table_name")
@click.argument("is_test",type=bool)
@click.argument("model_file")
@click.argument("prediction_file")
def main(table_name,id_table_name,is_test,model_file,prediction_file):
    logging.config.fileConfig("LogSetting.ini")
    logger = logging.getLogger(__name__)
    logger.info("start : " + __file__)

    setting_parser = configparser.ConfigParser()
    setting_parser.read("setting.ini")
    host = setting_parser.get("database", "host_name")
    db_name = setting_parser.get("database", "db_name")
    username = setting_parser.get("database", "user_name")
    passward = setting_parser.get("database", "password")

    chunksize = 10 ** 4

    dataset = None
    if is_test:
        dataset = UnlabeledDataset(host=host,db_name=db_name,username=username,passward=passward,table_name=table_name,chunksize=chunksize)
    else:
        dataset = LabeledDataset(host=host,db_name=db_name,username=username,passward=passward,table_name=table_name,id_table_name=id_table_name,chunksize=chunksize)

    model = Model.load(model_file)
    
    prediction_collection = model.predict(dataset)
    prediction_collection.save(prediction_file)

    logger.info("end : " + __file__)
    

if __name__ == "__main__":
    main()
