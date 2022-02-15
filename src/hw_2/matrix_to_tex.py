def convert_matrix_to_tex(matrix: list[list]) -> str:
    matrix_body = '\\\\\n'.join([' & '.join([str(element) for element in row]) for row in matrix])
    return '\\begin{matrix}\n' \
           f'{matrix_body}\n' \
           '\\end{matrix}'


def main():
    example_tex = convert_matrix_to_tex([[1, 2],
                                         [3, 4]])
    with open('artifacts/matrix.tex', 'w') as f:
        f.write(example_tex)


if __name__ == '__main__':
    main()
