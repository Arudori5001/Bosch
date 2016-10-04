#coding:utf-8

import click

from PredictionCollection import PredictionCollection

@click.command()
@click.argument("prediction_file")
def main(prediction_file):
    prediction_collection = PredictionCollection.load(prediction_file)
    print("confision matrix:\n{}".format(prediction_collection.get_confusion_matrix()))
    print("acc:\t{}".format(prediction_collection.get_accuracy()))
    

if __name__ == "__main__":
    main()
