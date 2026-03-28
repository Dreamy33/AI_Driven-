import ast
from parser import parse_python_code
from ast_analyzer import CodeAnalyzer


def preprocess_code(code):
    tree = ast.parse(code)
    formatted_code = ast.unparse(tree)
    return formatted_code


def main():

    print("\n===== AI Code Analyzer (Milestone 1) =====\n")

    student_code = input("Paste your Python code:\n\n")

    tree = parse_python_code(student_code)

    if isinstance(tree, str):
        print(tree)
        return

    analyzer = CodeAnalyzer()
    analyzer.visit(tree)

    formatted_code = preprocess_code(student_code)

    print("\n--- Code Structure ---")
    print("Functions Found:", analyzer.functions)
    print("Loops Found:", analyzer.loops)
    print("Imports Found:", analyzer.imports)

    print("\n--- Code Successfully Parsed ---")
    print("Code formatting completed.")


if __name__ == "__main__":
    main()