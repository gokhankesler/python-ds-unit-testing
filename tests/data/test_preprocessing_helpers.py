# Import the function convert_to_int()
import pytest
import sys

from src.data.preprocessing_helpers import convert_to_int, row_to_list


# pytest tests/data/test_preprocessing_helpers.py::TestRowToList
# Declare the TestRowToList test class
class TestRowToList(object):
    def test_on_normal_argument_1(self):
        actual = row_to_list("123\t4,567\n")
        # Fill in with the expected return value for the argument "123\t4,567\n"
        expected = ["123", "4,567"]
        assert actual == expected, "Expected: {0}, Actual: {1}".format(expected, actual)

    def test_on_normal_argument_2(self):
        actual = row_to_list("1,059\t186,606\n")
        expected = ["1,059", "186,606"]
        # Write the assert statement along with a failure message
        assert actual == expected, "Expected: {0}, Actual: {1}".format(expected, actual)


# pytest tests/data/test_preprocessing_helpers.py::TestConvertToInt
# Declare the TestRowToList test class
class TestConvertToInt(object):

    # Complete the unit test name by adding a prefix
    def test_on_string_with_one_comma(self):
        test_argument = "2,081"
        expected = 2081
        actual = convert_to_int(test_argument)
        # Format the string with the actual return value
        message = "convert_to_int('2,081') should return the int 2081, but it actually returned {0}".format(actual)
        # Write the assert statement which prints message on failure
        assert actual == expected, message

    def test_on_no_tab_no_missing_value(self):  # (0, 0) boundary value
        # Assign actual to the return value for the argument "123\n"
        actual = row_to_list("123\n")
        assert actual is None, "Expected: None, Actual: {0}".format(actual)

    @pytest.mark.xfail
    def test_on_one_tab_with_missing_value(self):  # (1, 1) boundary value
        actual = row_to_list("\t4,567\n")
        # Format the failure message
        assert actual is None, "Expected: None, Actual: {0}".format(actual)

    def test_on_two_tabs_no_missing_value(self):  # (2, 0) boundary value
        actual = row_to_list("123\t4,567\t89\n")
        # Complete the assert statement
        assert actual is None, "Expected: None, Actual: {0}".format(actual)

    def test_with_no_comma(self):
        actual = convert_to_int("756")
        # Complete the assert statement
        assert actual == 756, "Expected: 756, Actual: {0}".format(actual)

    @pytest.mark.skipif(sys.version_info > (2, 7), reason="requires Python 2.7")
    def test_with_no_comma(self):
        """Only runs on python 2.7 or lower"""
        test_argument = "756"
        expected = 756
        actual = convert_to_int(test_argument)
        message = unicode("Expected: 2081, Actual:{}".format(actual))
        assert actual == expected, message

    def test_with_one_comma(self):
        actual = convert_to_int("2,081")
        # Complete the assert statement
        assert actual == 2081, "Expected: 2081, Actual: {0}".format(actual)

    def test_with_two_commas(self):
        actual = convert_to_int("1,034,891")
        # Complete the assert statement
        assert actual == 1034891, "Expected: 1034891, Actual: {0}".format(actual)

    # Give a name to the test for an argument with missing comma
    def test_on_string_with_missing_comma(self):
        actual = convert_to_int("178100,301")
        assert actual is None, "Expected: None, Actual: {0}".format(actual)

    def test_on_string_with_incorrectly_placed_comma(self):
        # Assign to the actual return value for the argument "12,72,891"
        actual = convert_to_int("12,72,891")
        assert actual is None, "Expected: None, Actual: {0}".format(actual)

    def test_on_float_valued_string(self):
        actual = convert_to_int("23,816.92")
        # Complete the assert statement
        assert actual is None, "Expected: None, Actual: {0}".format(actual)
