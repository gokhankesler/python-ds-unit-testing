import numpy as np
import pytest
import os


def get_data_as_numpy_array(clean_data_file_path, num_columns):
    result = np.empty((0, num_columns))
    with open(clean_data_file_path, "r") as f:
        rows = f.readlines()
        for row_num in range(len(rows)):
            try:
                row = np.array([rows[row_num].rstrip("\n").split("\t")], dtype=float)
            except ValueError:
                raise ValueError("Line {0} of {1} is badly formatted".format(row_num + 1, clean_data_file_path))
            else:
                if row.shape != (1, num_columns):
                    raise ValueError("Line {0} of {1} does not have {2} columns".format(row_num + 1, clean_data_file_path, num_columns))
            result = np.append(result, row, axis=0)
    return result


# Add a decorator to make this function a fixture
@pytest.fixture
def clean_data_file():
    file_path = "clean_data_file.txt"
    with open(file_path, "w") as f:
        f.write("201\t305671\n7892\t298140\n501\t738293\n")
    yield file_path
    os.remove(file_path)

@pytest.fixture
# Add the correct argument so that this fixture can chain with the tmpdir fixture
def empty_file(tmpdir):
    # Use the appropriate method to create an empty file in the temporary directory
    file_path = tmpdir.join("empty.txt")
    open(file_path, "w").close()
    yield file_path