# coding:utf-8

import abc
import numpy as np


class BaseDataset:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_records(self):
        raise NotImplementedError()

    def get_ids(self, records):
        return np.array([r.get_id() for r in self.get_records()])

    def get_input_matrix(self, records):
        return np.array([r.get_input_vector() for r in self.get_records()])

    def get_labels(self, records):
        return np.array([r.get_label() for r in self.get_records()])
