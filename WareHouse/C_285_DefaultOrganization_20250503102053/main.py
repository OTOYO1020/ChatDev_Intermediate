'''
Main application file for the problem ID index calculator.
'''
import sys
import re  # Import the regular expression module
from utils import calculate_total_ids, calculate_index_of_problem_id
def main():
    problem_id = input("Enter Problem ID: ").strip()
    if not problem_id:
        print("Input Error: Please enter a valid Problem ID.")
        return
    # Validate that the input consists only of uppercase letters
    if not re.match("^[A-Z]+$", problem_id):
        print("Input Error: Problem ID must consist of uppercase letters only (A-Z).")
        return
    # Check for maximum length
    if len(problem_id) > 10:  # Example limit
        print("Input Error: Problem ID must not exceed 10 characters.")
        return
    try:
        index = calculate_index_of_problem_id(problem_id)
        print(f"Index of Problem ID: {index}")
    except Exception as e:
        print(f"Calculation Error: {str(e)}")
if __name__ == "__main__":
    main()