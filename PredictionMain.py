#coding;utf-8

import click

from Dataset import Dataset
from Model import Model

@click.command()
@click.argument("table_name")
@click.argument("is_test",type=bool)
@click.argument("model_file")
@click.argument("prediction_file")
def main(table_name,is_test,model_file,prediction_file):
    host = "localhost"
    db_name = "bosch"
    username = "root"
    passward = ""
    chunksize = 10 ** 4
    
    dataset = Dataset(is_test=is_test,host=host,db_name=db_name,username=username,passward=passward,table_name=table_name,chunksize=chunksize)
    model = Model.load(model_file)
    
    prediction_collection = model.predict(dataset)
    prediction_collection.save(prediction_file)
    

if __name__ == "__main__":
    main()
