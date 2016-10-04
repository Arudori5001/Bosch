#coding:utf-8

import numpy as np

from ClassificaitonPredictionCollection import ClassificationPredictionCollection

class BinaryPredictionCollection(ClassificationPredictionCollection):

    def __init__(self,predictions):
        super(BinaryPredictionCollection,self).__init__(predictions)

    def get_mcc(self):
        """
        @summary: calculate Matthew Correlation Coefficient(MCC)
        """
        confusion_matrix = self.get_confusion_matrix()
        tp = confusion_matrix[1,1]
        fp = confusion_matrix[0,1]
        tn = confusion_matrix[0,0]
        fn = confusion_matrix[1,0]

        return float(tp * tn - fp * fn) / np.sqrt((tp + fp) * (tp + fn) * (tn + fp) * (tn + fn))