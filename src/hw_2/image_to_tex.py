import ast
import subprocess

from hw_1.ast_visualizer import GraphConstructorVisitor
import imgkit
import pdfcrowd

from hw_2.matrix_to_tex import convert_matrix_to_tex


def tex_with_image(image_path: str) -> str:
    return f'''
\\documentclass{{article}}
\\usepackage{{graphicx}}
\\usepackage{{amsmath}}
\\begin{{document}}
\\includegraphics[scale=0.3]{{{image_path}}}
\\end{{document}}'''


def get_image_from_hw1():
    with open('../hw_1/top_fibonacci_numbers.py') as f:
        fibonacci_content = f.read()
    function_ast = ast.parse(fibonacci_content).body[0]
    visitor = GraphConstructorVisitor()

    visitor.visit(function_ast)
    visitor.graph.show('artifacts/ast.html')
    # imgkit needs wkhtmltopdf to generate jpg from html, it doesn't generate graph somehow(
    # imgkit.from_file('artifacts/ast.html', 'artifacts/ast.png')

    # I ve used pdfcrowd API to do it instead
    client = pdfcrowd.HtmlToImageClient('demo', 'ce544b6ea52a5621fb9d55f8b542d14d')
    client.setOutputFormat('png')
    client.convertFileToFile('artifacts/ast.html', 'artifacts/ast.png')

def main():
    get_image_from_hw1()
    tex_content = tex_with_image('artifacts/ast.png')
    matrix_tex = convert_matrix_to_tex([[1, 2],
                                        [3, 4]])
    tex_lines = tex_content.split('\n')
    tex_content = '\n'.join(tex_lines[:-1]) + '\n$' + matrix_tex + '$\n' + tex_lines[-1]
    with open('artifacts/ast.tex', 'w') as f:
        f.write(tex_content)
    proc = subprocess.Popen(['pdflatex', '--output-directory=artifacts/', 'artifacts/ast.tex'])
    proc.communicate()


if __name__ == '__main__':
    main()
