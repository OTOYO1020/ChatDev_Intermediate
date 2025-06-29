'''
Main application file for the operations calculator.
'''
from operations import Operations
def main():
    try:
        a = int(input("Enter a (positive integer): "))
        N = int(input("Enter N (positive integer): "))
        if a <= 0 or N <= 0:
            raise ValueError("Both a and N must be positive integers.")
        operations = Operations(a, N)
        result = operations.perform_operations()
        print(f"Operations: {result}")
    except ValueError as e:
        print(f"Input Error: {str(e)}")
if __name__ == "__main__":
    main()