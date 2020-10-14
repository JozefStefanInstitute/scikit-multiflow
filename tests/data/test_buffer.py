from skmultiflow.data.buffer import QuantityBasedBuffer
import numpy as np


def test_quantity_based_buffer(test_path):
    buffer = QuantityBasedBuffer(5)
    buffer_simulator = []
    for i in range(7):
        buffer_simulator.append(i)
        np.testing.assert_array_equal(buffer.register_value(i), buffer_simulator[-5:])

