# anomaly detection using six sigma

import numpy as np
import statistics as st
from skmultiflow.data.source.array_data_source import ArrayDataSource
from skmultiflow.data.generator.from_array_generator import FromArrayGenerator


my_array = np.array([[10,0],[4,0],[240,1],[2,0],[16,0],[12,0],[300,1],[4.5,0]])
my_stream = FromArrayGenerator(my_array)
number_of_samples = 0


true_positives = 0
detected_anomalies = 0

while number_of_samples < len(my_array):
    X, y = my_stream.next_sample()

    number_of_samples += 1


print(f'{number_of_samples} samples analyzed')

