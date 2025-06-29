'''
Main application file for the K-th Product Calculator.
'''
from kth_product import find_kth_product
def main():
    '''
    Main function to handle input and output for the K-th product calculation.
    '''
    try:
        N = int(input("Enter N: "))
        K = int(input("Enter K: "))
        # Validate that N and K are positive integers
        if N <= 0:
            raise ValueError("N must be a positive integer.")
        if K <= 0:
            raise ValueError("K must be a positive integer.")
        A_input = input("Enter list A (comma-separated): ")
        # Validate that A_input is not empty
        if not A_input.strip():
            raise ValueError("List A cannot be empty.")
        try:
            A = list(map(int, (x.strip() for x in A_input.split(','))))  # Updated line to handle whitespace
        except ValueError:
            raise ValueError("All elements in A must be valid integers.")
        if len(A) != N:
            raise ValueError("Length of A must be equal to N.")
        # Check for uniqueness of elements in A
        if len(A) != len(set(A)):
            raise ValueError("All elements in A must be unique.")
        result = find_kth_product(N, K, A)
        print(f"K-th Product: {result}")
    except ValueError as e:
        print(f"Input Error: {e}")
if __name__ == "__main__":
    main()