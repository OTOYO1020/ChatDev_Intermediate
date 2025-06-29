'''
Main entry point for the application.
'''
from calculator import calculate_sum_of_products
def main():
    # Example input, replace with actual input handling as needed
    X = input("Enter X (string of digits): ")
    N = int(input("Enter N (length of X): "))
    if len(X) != N or '0' in X:
        raise ValueError("Invalid input: X must be of length N and contain no '0' digits.")
    result = calculate_sum_of_products(X, N)
    print(f"Result: {result}")
if __name__ == "__main__":
    main()