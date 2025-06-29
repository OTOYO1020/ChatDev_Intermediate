'''
Main application file for the project manager application.
'''
from utils import validate_input, calculate_max_projects
def main():
    # Read input values
    N = int(input("Enter the number of departments (N): "))
    K = int(input("Enter the number of employees required for each project (K): "))
    employees = list(map(int, input("Enter the number of employees in each department (comma-separated): ").split(',')))
    # Validate input
    if validate_input(N, K, employees):
        max_projects = calculate_max_projects(N, K, employees)
        print(f"Maximum number of projects that can be formed: {max_projects}")
    else:
        print("Invalid input. Please check your values.")
if __name__ == "__main__":
    main()