import ast

def parse_python_code(code):
    """
    Parse student Python code using AST
    """
    try:
        tree = ast.parse(code)
        return tree

    except SyntaxError as e:
        return f"Syntax Error: {e}"