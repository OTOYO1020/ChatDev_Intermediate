'''
Main application file for calculating expected values based on user input.
'''
from expected_value import expected_value
def main():
    try:
        # Input parsing
        input_data = input("Enter a list of integers (comma-separated): ")
        A = list(map(int, input_data.split(',')))
        K = int(input("Enter the index K (1-based): "))
        M = int(input("Enter the maximum integer value M: "))
        # Validate K
        if K < 1 or K > len(A):
            raise ValueError("K must be between 1 and the length of the list A.")
        # Validate M
        if M <= 0:
            raise ValueError("M must be a positive integer.")
        # Calculate expected value
        result = expected_value(A, K, M)
        print(f"Result: {result}")
    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
if __name__ == "__main__":
    main()