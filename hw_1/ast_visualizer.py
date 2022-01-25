import ast
from pyvis.network import Network


NODE_COLOR = {
    ast.Name: 'red',
    ast.Constant: 'black',
    ast.BinOp: 'orange',
    ast.UnaryOp: 'green',
    ast.Subscript: 'grey',
    ast.Call: 'pink'
}


class GraphConstructorVisitor(ast.NodeVisitor):
    def __init__(self):
        self.dfs_stack = []
        self.graph = Network('800px', '1500px')
        self.cur_id = 0

    def generic_visit(self, ast_node):
        node_name = type(ast_node).__name__
        content = ast.unparse(ast_node)

        # Some nodes like "Load" doesn't show a lot of information
        if content == "":
            super(self.__class__, self).generic_visit(ast_node)
            return

        parent_id = None
        if len(self.dfs_stack) != 0:
            parent_id = self.dfs_stack[-1]

        node_id = self.cur_id
        self.dfs_stack.append(node_id)
        self.graph.add_node(node_id, label=node_name)
        if parent_id is not None:
            self.graph.add_edge(node_id, parent_id)
        self.cur_id += 1

        super(self.__class__, self).generic_visit(ast_node)

        graph_node = self.graph.get_node(node_id)
        # if we are on the ast leaf
        if self.cur_id == node_id + 1:
            graph_node['label'] += f' "{content}"'
        elif 'op' in ast_node.__dict__:
            graph_node['label'] += f' "{type(ast_node.op).__name__}"'
        elif 'name' in ast_node.__dict__:
            graph_node['label'] += f' "{ast_node.name}"'
        elif 'attr' in ast_node.__dict__:
            graph_node['label'] += f' "{ast_node.attr}"'

        if type(ast_node) in NODE_COLOR:
            graph_node['color'] = NODE_COLOR[type(ast_node)]

        self.dfs_stack.pop()


if __name__ == '__main__':
    with open('top_fibonacci_numbers.py') as f:
        fibonacci_content = f.read()
    function_ast = ast.parse(fibonacci_content).body[0]
    visitor = GraphConstructorVisitor()

    visitor.visit(function_ast)
    visitor.graph.show('artifacts/ast.html')
