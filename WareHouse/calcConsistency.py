import ast
import os
from sentence_transformers import SentenceTransformer, util

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
    directory = "./1"  # Specify the directory containing the Python files
    requirement_description = "Develop a hit and blow game that randomly generates three-digit numbers with different digits and predicts the number. The user inputs a three-digit number, and if both the number and the digit position are the same, it is a hit, and if only the number is the same but the digit position is different, it is a blow, and output the number. The number of times the user can try (life) is set to seven, and the number of remaining lives is displayed. If the user answers correctly halfway through, end the game as if they answered correctly. If the input numbers contain the same digit or a number other than three digits is entered, it is considered an incorrect input and the user is asked to enter it again. In addition, do not reduce the number of lives in that case."

    consistency_score = calculate_consistency_score_with_requirements(directory, requirement_description)
    print(f"Consistency Score with Provided Requirement: {consistency_score:.2f}")
