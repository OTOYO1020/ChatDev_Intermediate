'''
Main application file for the product computation.
'''
from utils import validate_A, validate_B
def compute_product(A, B):
    '''
    Computes the product of A and B, truncating the result to an integer.
    '''
    product = A * B
    result = int(product)  # Truncate the product
    return result
def main():
    while True:
        try:
            A_input = input("Enter integer A (0 to 10^15): ")
            A = int(A_input)  # Move the conversion here
            B_input = input("Enter float B (0.00 to 9.99): ")
            if not validate_A(A):
                raise ValueError("A must be between 0 and 10^15 inclusive.")
            if not validate_B(B_input):  # Pass the string directly
                raise ValueError("B must be a float between 0 (inclusive) and 10 (exclusive) with exactly two decimal places.")
            B = float(B_input)  # Convert to float after validation
            result = compute_product(A, B)
            print(f"Result: {result}")
            break  # Exit the loop if inputs are valid
        except ValueError as e:
            print(f"Input Error: {e}")
if __name__ == "__main__":
    main()