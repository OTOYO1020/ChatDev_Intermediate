'''
Main application file for the MaxProjects application.
'''
from calculator import max_projects
def main():
    # Read input values
    N = int(input("Enter the number of departments (N): "))
    K = int(input("Enter the group size (K): "))
    A = list(map(int, input("Enter the number of employees in each department (comma-separated): ").split(',')))
    # Validate input
    if len(A) != N:
        raise ValueError("The number of departments must match N.")
    # Calculate the maximum number of projects
    result = max_projects(N, K, A)
    # Display the result
    print(f"Maximum Projects: {result}")
if __name__ == "__main__":
    main()