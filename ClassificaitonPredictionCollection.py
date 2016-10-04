# coding:utf-8

from sklearn.metrics import confusion_matrix

from PredictionCollection import PredictionCollection

class ClassificationPredictionCollection(PredictionCollection):

    def __init__(self,predictions):
        super(ClassificationPredictionCollection,self).__init__(predictions)

    def get_confusion_matrix(self):
        actuals = self.get_actual_labels()
        predicteds = self.get_predicted_labels()
        label_kinds = self.get_label_kinds()

        return confusion_matrix(actuals, predicteds, labels=label_kinds)

    def get_label_kinds(self):
        seen = set()
        label_kinds = sorted([x for x in self.get_actual_labels() if x not in seen and not seen.add(x)])
        return label_kinds