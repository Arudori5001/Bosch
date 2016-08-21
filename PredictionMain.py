#coding;utf-8

import click

from Dataset import Dataset
from Model import Model

@click.command()
@click.argument("dataset_file")
@click.argument("model_file")
@click.argument("prediction_file")
def main(dataset_file,model_file,prediction_file):
    dataset = Dataset.load(dataset_file)
    model = Model.load(model_file)
    
    prediction_collection = model.predict(dataset)
    prediction_collection.save(prediction_file)
    

if __name__ == "__main__":
    main()
