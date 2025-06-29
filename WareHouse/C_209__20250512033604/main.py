'''
Main application file for the sequence counter.
'''
from sequence_counter import count_sequences
def main():
    try:
        # Read input from standard input
        n = int(input("Enter N: "))
        c = list(map(int, input("Enter C (comma-separated): ").split(',')))
        # Validate input
        if not validate_input(n, c):
            raise ValueError("Invalid input. Please ensure N matches the length of C and all values are positive integers.")
        # Calculate the number of valid sequences
        result = count_sequences(n, c)
        print(f"Number of valid sequences: {result}")
    except ValueError as ve:
        print(f"Input Error: {str(ve)}")
    except Exception as e:
        print(f"Unexpected Error: {str(e)}")
def validate_input(n, c):
    return len(c) == n and all(x > 0 for x in c)
if __name__ == "__main__":
    main()