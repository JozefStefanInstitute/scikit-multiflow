from skmultiflow.data.stats.aggregate_stats_infinite import StdDev, Median, Mean
import numpy as np
from mockito import mock, when, verify
from tdigest import TDigest


# def test_aggregate_stats_infinite_stddev():


def test_aggregate_stats_infinite_median():
    median = Median()
    median.tdigest = mock(spec=TDigest)
    for i in [1, 2, 3, 4, 5, 1, 10]:
        median.register_value(i)

    verify(median.tdigest, times=7).update(...)
    verify(median.tdigest, times=7).percentile(50)


def test_aggregate_stats_infinite_mean():
    mean = Mean()
    mean.tdigest = mock(spec=TDigest)
    for i in [1, 2, 3, 4, 5, 1, 10]:
        mean.register_value(i)

    verify(mean.tdigest, times=7).update(...)
    verify(mean.tdigest, times=7).trimmed_mean(1, 99)



