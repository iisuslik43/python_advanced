import numpy as np
from src.hw_3.matrix_mixins import StrMixin, ReprMixin, WriteToFileMixin, PropertyMixin


class MatrixWithOps(np.lib.mixins.NDArrayOperatorsMixin,
                    WriteToFileMixin,
                    ReprMixin,
                    StrMixin,
                    PropertyMixin):

    def __init__(self, value):
        self._value = np.asarray(value)
        self._shape = self._value.shape

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        inputs = tuple(x._value if isinstance(x, MatrixWithOps) else x
                       for x in inputs)
        result = getattr(ufunc, method)(*inputs, **kwargs)

        if type(result) is tuple:
            return tuple(type(self)(x) for x in result)
        elif method == 'at':
            return None
        else:
            return type(self)(result)



def main():
    np.random.seed(0)

    a = MatrixWithOps(np.random.randint(0, 10, (10, 10)))
    b = MatrixWithOps(np.random.randint(0, 10, (10, 10)))

    for matrix, op_str in [(a + b, '+'), (a * b, '*'), (a @ b, '@')]:
        matrix.write_to_file(f'artifacts/medium/matrix{op_str}.txt')


if __name__ == '__main__':
    main()
