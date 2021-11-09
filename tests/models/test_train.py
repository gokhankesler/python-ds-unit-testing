# Declare the test class
import pytest
import numpy as np

from src.models.train import split_into_training_and_testing_sets


# pytest tests/models/test_train.py::TestSplitIntoTrainingAndTestingSets
# Declare the test class
class TestSplitIntoTrainingAndTestingSets(object):
    # Fill in with the correct mandatory argument
    # pytest tests/models/test_train.py::TestSplitIntoTrainingAndTestingSets::test_on_one_row
    @pytest.mark.xfail
    def test_on_one_row(self):
        test_argument = np.array([[1382.0, 390167.0]])
        with pytest.raises(ValueError) as exc_info:
            split_into_training_and_testing_sets(test_argument)
        expected_error_msg = "Argument data_array must have at least 2 rows, it actually has just 1"
        assert exc_info.match(expected_error_msg)

    def test_on_six_rows(self):
        example_argument = np.array([[2081.0, 314942.0], [1059.0, 186606.0],
                                     [1148.0, 206186.0], [1506.0, 248419.0],
                                     [1210.0, 214114.0], [1697.0, 277794.0]]
                                    )
        # Fill in with training array's expected number of rows
        expected_training_array_num_rows = 4
        # Fill in with testing array's expected number of rows
        expected_testing_array_num_rows = 2
        actual = split_into_training_and_testing_sets(example_argument)
        # Write the assert statement checking training array's number of rows
        assert actual[0].shape[
                   0] == expected_training_array_num_rows, "The actual number of rows in the    " \
                                                           "training array is not {}".format(
            expected_training_array_num_rows)
        # Write the assert statement checking testing array's number of rows
        assert actual[1].shape[
                   0] == expected_testing_array_num_rows, "The actual number of rows in the testing " \
                                                          " array is not {}".format(
            expected_testing_array_num_rows)


# Add a reason for the expected failure
@pytest.mark.xfail(reason="Using TDD, model_test() has not yet been implemented")
class TestModelTest(object):
    def test_on_linear_data(self):
        test_input = np.array([[1.0, 3.0], [2.0, 5.0], [3.0, 7.0]])
        expected = 1.0
        actual = model_test(test_input, 2.0, 1.0)
        message = "model_test({0}) should return {1}, but it actually returned {2}".format(test_input, expected, actual)
        assert actual == pytest.approx(expected), message

    def test_on_one_dimensional_array(self):
        test_input = np.array([1.0, 2.0, 3.0, 4.0])
        with pytest.raises(ValueError) as exc_info:
            model_test(test_input, 1.0, 1.0)
