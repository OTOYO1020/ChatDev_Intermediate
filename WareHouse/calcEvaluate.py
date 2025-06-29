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
                    #print(f"Import issue in {filepath}: {import_error}")
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
def extract_requirements_from_code(filepath):
    """
    Extract pseudo-requirements from Python code by analyzing comments, docstrings, 
    function names, and class names.
    """
    requirements = []
    with open(filepath, "r", encoding="utf-8") as file:
        content = file.read()

    try:
        tree = ast.parse(content)
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                # Extract function names and docstrings
                docstring = ast.get_docstring(node)
                requirements.append(f"Function {node.name}: {docstring if docstring else 'No description provided'}")
            elif isinstance(node, ast.ClassDef):
                # Extract class names and docstrings
                docstring = ast.get_docstring(node)
                requirements.append(f"Class {node.name}: {docstring if docstring else 'No description provided'}")
    except SyntaxError as e:
        return f"Syntax Error: {e}"

    return "\n".join([req for req in requirements if req])

def calculate_consistency_score_with_requirements(directory, requirement_description):
    """
    Calculate the consistency score between the specified requirement description and
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
        return 100.0  # Assume perfect consistency if no files are available

    consistency_score = (total_similarity / total_files) * 100
    return consistency_score

if __name__ == "__main__":
    for i in range(4, 11):
        print({i})
        directory = f"./At{i}"
        requirement_description1 = "Preprocess Input Sequences : Please make sure that input/output and standard input/output are used. Parse the input sequences A and B, ensuring they meet the constraints 1≤M≤N≤5×105 and 0≤Ai,Bi≤5×105. (1≤M≤N≤5×1051 \leq M \leq N \leq 5 \times 10^5, 0≤Ai,Bi≤5×1050 \leq A_i, B_i \leq 5 \times 10^5) Identify and handle zeros in sequences A and B, replacing them with positive real numbers."
        requirement_description2 = "Generate Subsequence Candidates : Iterate through sequence A to extract all contiguous subsequences C of length M. Maintain computational efficiency, ensuring time complexity remains feasible for large inputs."
        requirement_description3 = "Transform Sequences : Scale subsequences C and sequence B by arbitrary positive real numbers to normalize their values for comparison. Handle cases where elements are zeros, ensuring the transformations remain valid."
        requirement_description4 = "Compare Transformed Sequences : For each subsequence C, check if there exists a scalar t that makes t×C identical to B. Ensure the comparison is robust and accounts for floating-point inaccuracies due to scaling."
        requirement_description5 = "Count Valid Matches : Count the number of starting indices i in A where subsequences C match B after transformations."

        completeness_score = calculate_completeness_score(directory)
        executability_score = calculate_executability_score(directory)    
        consistency_score1 = calculate_consistency_score_with_requirements(directory, requirement_description1)
        consistency_score2 = calculate_consistency_score_with_requirements(directory, requirement_description2)
        consistency_score3 = calculate_consistency_score_with_requirements(directory, requirement_description3)
        consistency_score4 = calculate_consistency_score_with_requirements(directory, requirement_description4)
        consistency_score5 = calculate_consistency_score_with_requirements(directory, requirement_description5)
        print(f"{completeness_score:.2f}")
        print(f"{executability_score:.2f}")
        print(f"{consistency_score1:.2f}")
        print(f"{consistency_score2:.2f}")
        print(f"{consistency_score3:.2f}")
        print(f"{consistency_score4:.2f}")
        print(f"{consistency_score5:.2f}")