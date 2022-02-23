import numpy as np


class MatrixNotMatchingShapesException(Exception):
    pass


class Matrix:
    def __init__(self, value):
        self.value = np.asarray(value)
        self.shape = self.value.shape

    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise NotImplementedError('Trying to add not Matrix object')
        if self.shape != other.shape:
            raise MatrixNotMatchingShapesException(f'{self.shape} != {other.shape}')
        result = np.zeros(self.shape)
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                result[i][j] = self.value[i][j] + other.value[i][j]
        return Matrix(result)

    def __mul__(self, other):
        if not isinstance(other, Matrix):
            raise NotImplementedError('Trying to multiply with not Matrix object')
        if self.shape != other.shape:
            raise MatrixNotMatchingShapesException(f'{self.shape} != {other.shape}')
        result = np.zeros(self.shape)
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                result[i][j] = self.value[i][j] * other.value[i][j]
        return Matrix(result)

    def __matmul__(self, other):
        if not isinstance(other, Matrix):
            raise NotImplementedError('Trying to multiply with not Matrix object')
        if self.shape[1] != other.shape[0]:
            raise MatrixNotMatchingShapesException(f'{self.shape[1]} != {other.shape[0]}')
        result = np.zeros((self.shape[0], other.shape[1]))
        for i in range(self.shape[0]):
            for j in range(other.shape[1]):
                for k in range(other.shape[0]):
                    result[i][j] += self.value[i][k] * other.value[k][j]
        return Matrix(result)


def main():
    np.random.seed(0)

    a = Matrix(np.random.randint(0, 10, (10, 10)))
    b = Matrix(np.random.randint(0, 10, (10, 10)))

    for matrix, op_str in [(a + b, '+'), (a * b, '*'), (a @ b, '@')]:
        matrix_str = '\n'.join([' '.join(map(str, row)) for row in matrix.value])
        with open(f'artifacts/easy/matrix{op_str}.txt', 'w') as f:
            f.write(matrix_str)


if __name__ == '__main__':
    main()
