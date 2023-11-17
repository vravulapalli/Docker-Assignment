# test.py

import pytest
from sparse_recommender import SparseMatrix

@pytest.fixture
def matrix():
    matrix = SparseMatrix()
    matrix.set(0, 0, 1)
    matrix.set(1, 1, 2)
    matrix.set(2, 2, 3)

    return matrix

def test_set_and_get(matrix):
    assert matrix.get(0, 0) == 1
    assert matrix.get(1, 1) == 2
    assert matrix.get(2, 2) == 3
    assert matrix.get(0, 1) == 0  # Non-existent element should return 0


def test_recommend(matrix):
    user_vector = [1, 0, 2]
    recommendations = matrix.recommend(user_vector)
    # Replace the expected recommendations with your actual expected recommendations
    expected_recommendations = [2, 0, 1]
    assert recommendations == expected_recommendations

def test_add_movie(matrix):
    other_matrix = SparseMatrix()
    other_matrix.set(0, 0, 2)
    other_matrix.set(1, 1, 2)
    other_matrix.set(2, 2, 2)

    result_matrix = matrix.add_movie(other_matrix)
    assert result_matrix.get(0, 0) == 3
    assert result_matrix.get(1, 1) == 4
    assert result_matrix.get(2, 2) == 5

def test_invalid_matrix_dimensions():
    test_invalid_matrix = SparseMatrix()
    test_invalid_user_vector = [1, 0]  # User vector with mismatched dimensions (should raise an error)
    with pytest.raises(ValueError):
        test_invalid_matrix.recommend(test_invalid_user_vector)

def test_negative_row_index():
    test_invalid_matrix = SparseMatrix()
    with pytest.raises(ValueError):
        test_invalid_matrix.set(-1, 0, 5)  # Attempting to set a negative row index should raise an error

def test_negative_column_index():
    test_invalid_matrix = SparseMatrix()
    with pytest.raises(ValueError):
        test_invalid_matrix.set(0, -1, 5)  # Attempting to set a negative column index should raise an error

def test_get_negative_column_index():
    test_invalid_matrix = SparseMatrix()
    with pytest.raises(ValueError):
        test_invalid_matrix.get(0, -1)  # Attempting to get a negative column index should raise an error

if __name__ == "__main__":
    pytest.main()
