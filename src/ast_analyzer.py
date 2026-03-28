import ast


class CodeAnalyzer(ast.NodeVisitor):
    """
    Visits nodes of AST to understand code structure
    """

    def __init__(self):
        self.functions = []
        self.loops = []
        self.imports = []

    def visit_FunctionDef(self, node):
        self.functions.append(node.name)
        self.generic_visit(node)

    def visit_For(self, node):
        self.loops.append("for loop")
        self.generic_visit(node)

    def visit_While(self, node):
        self.loops.append("while loop")
        self.generic_visit(node)

    def visit_Import(self, node):
        for alias in node.names:
            self.imports.append(alias.name)
        self.generic_visit(node)

    def visit_ImportFrom(self, node):
        self.imports.append(node.module)
        self.generic_visit(node)