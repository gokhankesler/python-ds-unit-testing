import numpy as np
import pytest
from src.features.as_numpy import get_data_as_numpy_array
import sys


# pytest tests/features/test_as_numpy.py::TestGetDataAsNumpyArray
@pytest.mark.xfail
class TestGetDataAsNumpyArray(object):
# Pass the correct argument so that the test can use the fixture
    def test_on_clean_file(clean_data_file):
        expected = np.array([[201.0, 305671.0], [7892.0, 298140.0], [501.0, 738293.0]])
        # Pass the clean data file path yielded by the fixture as the first argument
        actual = get_data_as_numpy_array(clean_data_file, 2)
        assert actual == pytest.approx(expected), "Expected: {0}, Actual: {1}".format(expected, actual)

    def test_on_empty_file(self, empty_file):
        expected = np.empty((0, 2))
        actual = get_data_as_numpy_array(empty_file, 2)
        assert actual == pytest.approx(expected), "Expected: {0}, Actual: {1}".format(expected, actual)

    # Mark as skipped if Python version is greater than 2.7
    @pytest.mark.skipif(sys.version_info > (2, 7), reason="Works only on Python 2.7 or lower")
    def test_on_clean_file(self):
        expected = np.array([[2081.0, 314942.0],
                             [1059.0, 186606.0],
                             [1148.0, 206186.0]
                             ]
                            )
        actual = get_data_as_numpy_array("example_clean_data.txt", num_columns=2)
        message = "Expected return value: {0}, Actual return value: {1}".format(expected, actual)
        assert actual == pytest.approx(expected), message

