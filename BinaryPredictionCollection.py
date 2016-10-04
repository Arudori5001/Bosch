#coding:utf-8

import numpy as np

from ClassificaitonPredictionCollection import ClassificationPredictionCollection

class BinaryPredictionCollection(ClassificationPredictionCollection):

    def __init__(self,predictions):
        super(BinaryPredictionCollection,self).__init__(predictions)

    def get_accuracy(self):
        tp = self.get_confusion_matrix()[1,1]
        fp = self.get_confusion_matrix()[0,1]
        tn = self.get_confusion_matrix()[0,0]
        fn = self.get_confusion_matrix()[1,0]

        return float(tp + tn) / (tp + fp + tn + fn)

    def get_mcc(self):
        """
        @summary: calculate Matthew Correlation Coefficient(MCC)
        """
        tp = self.get_confusion_matrix()[1,1]
        fp = self.get_confusion_matrix()[0,1]
        tn = self.get_confusion_matrix()[0,0]
        fn = self.get_confusion_matrix()[1,0]

        return float(tp * tn - fp * fn) / np.sqrt((tp + fp) * (tp + fn) * (tn + fp) * (tn + fn))