import numpy as np


class SixSigma ():

    '''Implementation of SixSigma method for anomaly detection.
    Six Sigma uses three standard deviations below the mean and three standard deviations
     above the mean to predict anomalies.

     Attributes:
         time_window : type int (default = 2)
                    'window size -> number of samples used for calculating the mean and standard deviation'

    Example shown in test_six_sigma.py
    '''


    def __init__(self,time_window=2):

        self.time_window = time_window
        self.buffer = []


    def fit (self,X,y):

        '''fit the model. Adjust buffer to obtain only the last time_window number of samples'''

        self.buffer.append(X)
        self.buffer = self.buffer[-self.time_window:]

    def predict (self,X):

        '''predict class for passed data.  '''

        if len(self.buffer) < self.time_window:
            return None
        else:
            j = 0
            while j < len(X):
                i = 0
                feature_array =[]
                while i < len(self.buffer):
                    feature_array.append(self.buffer[i][j])
                    i += 1
                average = np.mean(feature_array)
                sigma = np.std(feature_array)
                prediction = int(abs(X[j]) > abs(average) + 3 * abs(sigma))
                if prediction == 1:
                    break
                j+=1
        return prediction

