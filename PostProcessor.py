#coding:utf-8

import numpy as np

class PostProcessor:
    def write_submission_file(self, prediction_collection, filename):
        ids = prediction_collection.get_ids()
        predicted_labels = prediction_collection.get_predicted_labels()
        
        submission_data = np.array([ids, predicted_labels]).transpose()
        header = "Id,Response"
        np.savetxt(filename, submission_data, fmt="%.0f", delimiter=",", header=header, comments="")
