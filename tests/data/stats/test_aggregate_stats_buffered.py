from skmultiflow.data.stats.aggregate_stats_buffered import StdDev, Median, Mean
from skmultiflow.data.buffer import QuantityBasedBuffer
import numpy as np


def test_aggregate_stats_buffered_stddev():
    buffer = QuantityBasedBuffer(5)
    stddev = StdDev(buffer)
    values = [1, 1.1, 2, 3, 4, 5, -1.5, 10]
    buf = []
    for i in range(len(values)):
        buf.append(values[i])
        assert np.isclose(stddev.register_value(values[i]), np.std(np.array(buf[-5:])))


def test_aggregate_stats_buffered_median():
    buffer = QuantityBasedBuffer(5)
    median = Median(buffer)
    values = [1, 2, 3, 4, 5, 4]
    correct_results = [1, 1.5, 2, 2.5, 3, 4]
    for i in range(len(values)):
        assert np.isclose(median.register_value(values[i]), correct_results[i])


def test_aggregate_stats_buffered_mean():
    buffer = QuantityBasedBuffer(5)
    mean = Mean(buffer)
    values = [1, 2, 3, 4, 5, -1.5]
    correct_results = [1, 1.5, 2, 2.5, 3, 2.5]
    for i in range(len(values)):
        assert np.isclose(mean.register_value(values[i]), correct_results[i])




