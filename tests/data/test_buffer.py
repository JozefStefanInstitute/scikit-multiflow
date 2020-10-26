from skmultiflow.data.buffer import QuantityBasedBuffer, TimeBasedBuffer
import numpy as np
from datetime import datetime, timedelta


def test_quantity_based_buffer():
    buffer = QuantityBasedBuffer(5)
    buffer_simulator = []
    for i in range(7):
        buffer_simulator.append(i)
        np.testing.assert_array_equal(buffer.register_value(i), buffer_simulator[-5:])


def test_time_based_buffer():
    buffer = TimeBasedBuffer(timedelta(hours=3))

    np.testing.assert_array_equal(buffer.register_value((datetime(2020, 10, 1, 12), 1)), [1])
    np.testing.assert_array_equal(buffer.register_value((datetime(2020, 10, 1, 13), 2)), [1, 2])
    np.testing.assert_array_equal(buffer.register_value((datetime(2020, 10, 1, 11), 3)), [3, 1, 2])
    np.testing.assert_array_equal(buffer.register_value((datetime(2020, 10, 1, 14), 4)), [3, 1, 2, 4])
    np.testing.assert_array_equal(buffer.register_value((datetime(2020, 10, 1, 14, 30), 5)), [1, 2, 4, 5])
    np.testing.assert_array_equal(buffer.register_value((datetime(2020, 10, 1, 20), 6)), [6])
    np.testing.assert_array_equal(buffer.register_value((datetime(2020, 10, 1, 8), 7)), [6])

