# using six sigma to determine the standard deviation of data

#import statistics as stat
import numpy as np
import matplotlib.pyplot as plt

class SixSigma ():

    def __init__(self,time_window=2):

        self.time_window = time_window
        self.buffer = []


    def fit (self,X,y):
        self.buffer.append(X)
        self.buffer = self.buffer[-self.time_window:]
        #print(buffer)

    def predict (self,X,element):

        if len(self.buffer) < self.time_window:
            print(f'element {element} y_pred None')
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
                print(f'element {element}')
                print(f'array {feature_array}')
                print(f'mean {average}')
                print(f' sigma {sigma}')
                if abs(X[j]) > abs(average) + 3*abs(sigma):
                    prediction = 1
                    print(f'y_pred {prediction}')
                    j+=1
                    break
                    #return 1
                else:
                    prediction = 0
                    print(f'y_pred {prediction}')
                    j += 1
        return prediction




        #print(X)
        #print(buffer)
        #for element in X:
           # for column in buffer:
       # average = np.mean(buffer)
        #sigma = np.std(buffer)





    #print(my_array1)
'''c = []
b = []
i = 0
j = 0
while i < len(buffer):
    b.append(buffer[i][0])
    i+=1
print(b)
while j < len(b):
    c.append(b[j][0])
    j+=1
print(c)
#plt.show()

    #b = [10,14,24,2,16,12,30]
    #print(stat.pstdev(b))'''