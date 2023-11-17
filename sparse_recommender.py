# sparse_recommender.py

class SparseMatrix:
    def __init__(self):
        self.matrix = {}  # Use a dictionary to store non-zero elements
        self.number_rows = 0
        self.number_columns = 0

    def set(self, row, col, value):
        if row < 0 or col < 0:
            raise ValueError("Row and column indices must be non-negative")

        # Set the value at (row, col) to value
        if row not in self.matrix:
            self.matrix[row] = {}
        self.matrix[row][col] = value

        # Update the dimensions if necessary
        self.number_rows = max(self.number_rows, row + 1)
        self.number_columns = max(self.number_columns, col + 1)



    def get(self, row, col):
        if row < 0 or col < 0:
            raise ValueError("indices of Row and column  must be non-negative")
        # Returns the value at (row, col)
        if row in self.matrix and col in self.matrix[row]:
            return self.matrix[row][col]
        return 0

    def recommend(self, vector):
        if len(vector) != self.number_columns:
            raise ValueError("User vector dimensions do not match the matrix columns")
        recommendations = [0] * self.number_rows

        self.Helper(recommendations, vector)
        # Sort recommendations in descending order and return the indices
        sorted_indices = sorted(range(len(recommendations)), key=lambda i: recommendations[i], reverse=True)


        return sorted_indices

    def Helper(self, recommendations, vector):
        for row in range(self.number_rows):
            matrix_dot_product = 0
            for col in range(self.number_columns):
                matrix_dot_product += self.get(row, col) * vector[col]
            recommendations[row] = matrix_dot_product

    def add_movie(self, matrix):
        result_matrix = SparseMatrix()

        for row in set(self.matrix) | set(matrix.matrix):
            for col in set(self.matrix.get(row, {})) | set(matrix.matrix.get(row, {})):
                result_matrix.set(row, col, self.get(row, col) + matrix.get(row, col))
        return result_matrix

    def to_dense(self):
        # Your to_dense method logic here
        dense_matrix = [[0 for _ in range(self.number_columns)] for _ in range(self.number_rows)]

        for row in range(self.number_rows):
            for col in range(self.number_columns):
                dense_matrix[row][col] = self.get(row, col)
        return dense_matrix
