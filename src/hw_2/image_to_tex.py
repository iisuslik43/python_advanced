import ast
import subprocess

from hw_1.ast_visualizer import GraphConstructorVisitor
import imgkit


def tex_with_image(image_path: str) -> str:
    return f'''
\\documentclass{{article}}
\\usepackage{{graphicx}}
\\begin{{document}}
\\includegraphics{{{image_path}}}
\\end{{document}}
'''


def get_image_from_hw1():
    with open('../hw_1/top_fibonacci_numbers.py') as f:
        fibonacci_content = f.read()
    function_ast = ast.parse(fibonacci_content).body[0]
    visitor = GraphConstructorVisitor()

    visitor.visit(function_ast)
    visitor.graph.show('artifacts/ast.html')
    # imgkit needs wkhtmltopdf to generate jpg from html, it doesn't generate graph somehow((
    imgkit.from_file('artifacts/ast.html', 'artifacts/ast.png')


def main():
    get_image_from_hw1()
    tex_content = tex_with_image('artifacts/ast.png')
    with open('artifacts/ast.tex', 'w') as f:
        f.write(tex_content)
    proc = subprocess.Popen(['pdflatex', '--output-directory=artifacts/', 'artifacts/ast.tex'])
    proc.communicate()


if __name__ == '__main__':
    main()
