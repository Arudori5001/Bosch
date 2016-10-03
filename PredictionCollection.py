# coding:utf-8

import cPickle
import numpy as np
from sklearn.metrics import confusion_matrix

from ISavable import ISavable


class PredictionCollection(ISavable):

    def __init__(self, predictions):
        self.__predictions = predictions

    def get_predictions(self):
        return self.__predictions

    @staticmethod
    def load(filepath):
        obj = None
        with open(filepath, "rb") as f:
            obj = cPickle.load(f)
        return obj

    def save(self, filepath):
        with open(filepath, "wb") as f:
            cPickle.dump(self, f)

    def get_ids(self):
        return np.array([p.get_id() for p in self.get_predictions()])

    def get_actual_labels(self):
        return np.array([p.get_actual_label() for p in self.get_predictions()])

    def get_predicted_labels(self):
        return np.array([p.get_predicted_label() for p in self.get_predictions()])

    def get_confusion_matrix(self):
        actuals = self.get_actual_labels()
        predicteds = self.get_predicted_labels()
        label_kinds = self.get_label_kinds()

        return confusion_matrix(actuals, predicteds, labels=label_kinds)

    def get_label_kinds(self):
        seen = set()
        label_kinds = sorted([x for x in self.get_actual_labels() if x not in seen and not seen.add(x)])
        return label_kinds
