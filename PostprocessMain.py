#coding:utf-8

import click

from PredictionCollection import PredictionCollection
from PostProcessor import PostProcessor

@click.command()
@click.argument("prediction_file")
@click.argument("submission_file")
def main(prediction_file, submission_file):
    prediction_collection = PredictionCollection.load(prediction_file)
    postprocessor = PostProcessor()
    postprocessor.write_submission_file(prediction_collection, submission_file)

if __name__ == '__main__':
    main()
