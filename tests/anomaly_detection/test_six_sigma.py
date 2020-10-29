from skmultiflow.anomaly_detection.six_sigma import SixSigma
import numpy as np


def test_six_sigma(test_path):
    stream = [[[6, 3, 4], 0],
              [[7, 2, 3], 0],
              [[3, 3, 5], 0],
              [[15, 4, 4.5], 1],
              [[1, 5, 5.5], 0]]

    learner = SixSigma(time_window=2)

    y_pred = []  #array of predictions
    for element in stream:
        X = element[0]
        y = element[1]
        y_pred.append(learner.predict(X))
        learner.fit(X, y)

    expected_predictions = [None, None, 0, 1, 0]
    assert np.alltrue(y_pred == expected_predictions)
