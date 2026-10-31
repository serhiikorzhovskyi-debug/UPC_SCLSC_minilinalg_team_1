from mini_linalg.core import Matrix, Vector


def test_vector_creation():
    vector = Vector([1.0, 2.0])
    assert list(vector.data) == [1.0, 2.0]


def test_matrix_creation():
    matrix = Matrix([[1.0, 2.0], [3.0, 4.0]])
    assert [list(row) for row in matrix.data] == [[1.0, 2.0], [3.0, 4.0]]
