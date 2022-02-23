from src.hw_3.matrix import Matrix


def matrix_to_str(matrix: Matrix) -> str:
    return '\n'.join([' '.join(map(str, row)) for row in matrix._value])


class WriteToFileMixin:
    def write_to_file(self, filename):
        matrix_str = matrix_to_str(self)
        with open(filename, 'w') as f:
            f.write(matrix_str)


class ReprMixin:
    def __repr__(self):
        return matrix_to_str(self)


class StrMixin:
    def __str__(self):
        if self.shape[0] < 5 and self.shape[1] < 5:
            return matrix_to_str(self)
        else:
            return f'Matrix(shape={self.shape})'


class PropertyMixin:
    @property
    def shape(self):
        return self._shape
