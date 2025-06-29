'''
Main application file for the Sum Calculator using standard input and output.
'''
from utils import validate_input
def main():
    while True:
        try:
            A = int(input("Enter a positive integer for A (e.g., 2): "))
            X = int(input("Enter a non-negative integer for X (e.g., 3): "))
            M = int(input("Enter a positive integer for M (e.g., 5): "))
            break  # Exit loop if inputs are valid
        except ValueError:
            print("Error: Please enter valid integers for A, X, and M.")
    # Validate inputs
    if not validate_input(A, X, M):
        print("Error: A must be a positive integer, X must be a non-negative integer, and M must be a positive integer.")
        return
    result = 0
    if A == 1:
        result = X % M
    else:
        current_term = 1
        for i in range(X):
            result = (result + current_term) % M
            current_term = (current_term * A) % M
    print(f"Result: {result}")
if __name__ == "__main__":
    main()