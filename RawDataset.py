#coding:utf-8

import numpy as np
import os
from RawRecord import RawRecord

class RawDataset:
	def get_records(self):
		return self.__records
	
	
	def __set_records(self,value):
		self.__records = value


	def load(self, data_file, is_test, max_records):
		whole_data = np.genfromtxt(data_file, delimiter=",", skip_header=1, max_rows=max_records)
		ids = whole_data[:,0]
		input_matrix = None
		labels = None
		records = None
		if is_test:
			input_matrix = whole_data[:,1:]
			records = np.array([RawRecord(id=i,input_vector=v,label=None) for i,v in zip(ids, input_matrix)])
		else:
			input_matrix = whole_data[:,1:-1]
			labels = whole_data[:,-1]
			records = np.array([RawRecord(id=i,input_vector=v,label=l) for i,v,l in zip(ids, input_matrix, labels)])
		self.__set_records(records)
			


	def get_normalize_parameters(self):
		raise NotImplementedError()

	
	def normalize(self, mu, sigma):
		raise NotImplementedError()

	
	def remove_all_same_factor(self):
		raise NotImplementedError()
	
	
	def get_input_matrix(self):
		return np.array([r.get_input_vector() for r in self.get_records()])
	
	
	def set_input_matrix(self, value):
		for r,v in zip(self.get_records(), value):
			r.set_input_vector(v)
	
	
	def get_labels(self):
		raise NotImplementedError()
	
	
	def fill_missing(self, value):
		mat = self.get_input_matrix()
		mat[np.isnan(mat)] = value
		self.set_input_matrix(mat)
