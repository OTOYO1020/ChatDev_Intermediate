'''
Main entry point for the valid integers counting application.
'''
from integer_counter import IntegerCounter  # Ensure this import is present
def main():
    '''
    Reads the input length and calculates the valid integers.
    '''
    counter = IntegerCounter()
    while True:
        try:
            n = int(input("Enter the length of integers (N): "))
            if n < 1:
                raise ValueError("N must be a positive integer.")
            result = counter.count_valid_integers(n)
            print(f"Count of valid integers of length {n}: {result}")
            break  # Exit the loop after successful input and processing
        except ValueError as e:
            print(f"Input Error: {str(e)}. Please enter a valid positive integer.")
if __name__ == "__main__":
    main()