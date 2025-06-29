import ast
import os
import importlib.util
from sentence_transformers import SentenceTransformer, util

def check_file_completeness(filepath):
    """
    Check the completeness of a Python file by ensuring all function and class definitions are implemented
    without placeholders or missing implementations.
    Returns the number of issues and the total number of definitions.
    """
    with open(filepath, "r", encoding="utf-8") as file:
        content = file.read()

    try:
        tree = ast.parse(content)
    except SyntaxError as e:
        return f"Syntax Error in {filepath}: {e}", 0, 0

    issues = 0
    total_definitions = 0

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            total_definitions += 1
            if not any(isinstance(child, (ast.Pass, ast.Expr)) for child in node.body):
                issues += 1

        elif isinstance(node, ast.ClassDef):
            total_definitions += 1
            class_body_issues = all(
                isinstance(child, (ast.Pass, ast.Expr)) for child in node.body
            )
            if class_body_issues:
                issues += 1

    return issues, total_definitions

def calculate_completeness_score(directory):
    """
    Calculate the completeness score for all Python files in a directory.
    Completeness score is the percentage of definitions without issues.
    """
    total_issues = 0
    total_definitions = 0

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                filepath = os.path.join(root, file)
                issues, definitions = check_file_completeness(filepath)
                total_issues += issues
                total_definitions += definitions

    if total_definitions == 0:
        return 100.0  # No definitions means no placeholders, so score is perfect

    completeness_score = ((total_definitions - total_issues) / total_definitions) * 100
    return completeness_score

def check_syntax(filepath):
    """
    Check if the Python file has syntax errors.
    """
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read()
        compile(content, filepath, "exec")
        return True, None
    except SyntaxError as e:
        return False, f"Syntax Error: {e}"

def check_imports(filepath):
    """
    Check if all imports in the Python file can be resolved.
    """
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read()
        for line in content.splitlines():
            if line.startswith("import ") or line.startswith("from "):
                try:
                    module_name = line.split()[1].split('.')[0]
                    if not importlib.util.find_spec(module_name):
                        return False, f"Missing module: {module_name}"
                except Exception as e:
                    return False, f"Error checking imports: {e}"
        return True, None
    except Exception as e:
        return False, f"Error reading file: {e}"

def calculate_executability_score(directory):
    """
    Calculate the executability score for all Python files in a directory.
    Executability score is the percentage of files without syntax or import issues.
    """
    total_files = 0
    executable_files = 0

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                total_files += 1
                filepath = os.path.join(root, file)
                syntax_ok, syntax_error = check_syntax(filepath)
                if not syntax_ok:
                    print(f"Syntax issue in {filepath}: {syntax_error}")
                    continue
                imports_ok, import_error = check_imports(filepath)
                if not imports_ok:
                    print(f"Import issue in {filepath}: {import_error}")
                    continue
                executable_files += 1

    if total_files == 0:
        return 100.0  # No files to check, assume perfect score

    executability_score = (executable_files / total_files) * 100
    return executability_score

def calculate_consistency_score(directory, requirement_description):
    """
    Calculate the consistency score between the requirement description and
    the generated Python code in the specified directory.
    """
    model = SentenceTransformer('all-MiniLM-L6-v2')
    req_embedding = model.encode(requirement_description, convert_to_tensor=True)

    total_files = 0
    total_similarity = 0.0

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                total_files += 1
                filepath = os.path.join(root, file)
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
                code_embedding = model.encode(content, convert_to_tensor=True)
                similarity = util.pytorch_cos_sim(req_embedding, code_embedding).item()
                total_similarity += similarity

    if total_files == 0:
        return 100.0  # No files to compare, assume perfect consistency

    consistency_score = (total_similarity / total_files) * 100
    return consistency_score

if __name__ == "__main__":
    directory = "./1"  # Specify the directory containing the Python files
    requirement_description = "The system should implement a Hit and Blow game with GUI and basic game logic."

    completeness_score = calculate_completeness_score(directory)
    executability_score = calculate_executability_score(directory)
    consistency_score = calculate_consistency_score(directory, requirement_description)

    print(f"Completeness Score: {completeness_score:.2f}%")
    print(f"Executability Score: {executability_score:.2f}%")
    print(f"Consistency Score: {consistency_score:.2f}%")
