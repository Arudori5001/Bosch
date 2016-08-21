#coding:utf-8

import click

from PredictionCollection import PredictionCollection

@click.command()
@click.argument("prediction_file")
def main(prediction_file):
    prediction_collection = PredictionCollection.load(prediction_file)
    acc = prediction_collection.get_accuracy()
    mcc = prediction_collection.get_mcc()
    print("acc : {}".format(acc))
    print("mcc : {}".format(mcc))
    

if __name__ == "__main__":
    main()
