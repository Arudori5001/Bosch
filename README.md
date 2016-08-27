Templete for machine learning
=====

# Requirements
## Python libraries
* click 6.6
* numpy 1.11.1
* MySQL-python 1.2.5

## Others
* Python 2.7.10
* MySQL 5.7.14


# Usage

## Preprocess
```shell
python PreprocessMain.py
```

## Training
```shell
python TrainingMain.py MODEL_FILE
```
`MODEL_FILE` : the output file path for model

## Make prediction
```shell
python PredictionMain.py TABLE_NAME IS_TEST MODEL_FILE PREDICTION_FILE
```
`TABLE_NAME` : the name of MySQL table you want to make prediction
`IS_TEST` : the boolean value (True/False) representing whether or not the table is the for the test data
`MODEL_FILE` : the model file path you want to use
`PREDICTION_FILE` : the output file path for prediction

## Evaluation
```shell
python EvaluationMain.py PREDICTION_FILE
```
`PREDICTION_FILE` : the file path of the prediction you want to evaluate

## Postprocess
```shell
python PostprocessMain.py PREDICTION_FILE SUBMISSION_FILE
```
`PREDICTION_FILE` : the file path of the prediction you want to make submission file
`SUBSSION_FILE` : the output file path for submission