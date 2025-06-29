'''
Main application file for the inverse calculator.
'''
from calculator import calculate_inverse
def main():
    try:
        n = int(input("Enter the number of positive integers (N): "))
        sequence = list(map(int, input("Enter the sequence of positive integers (space-separated): ").split()))
        # Check if the number of integers matches N
        if len(sequence) != n:
            raise ValueError("The number of integers does not match N.")
        # Check if all integers are positive
        if any(num <= 0 for num in sequence):
            raise ValueError("All integers must be positive.")
        result = calculate_inverse(sequence)
        print(f"Result: {result}")
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
if __name__ == "__main__":
    main()