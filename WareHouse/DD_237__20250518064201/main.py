'''
Main application file for the sequence generator.
'''
from sequence import final_sequence
def main():
    try:
        n = input("Enter N: ")
        s = input("Enter S (string of L and R): ")
        # Check if N is a positive integer
        if not n.isdigit() or int(n) < 1:
            raise ValueError("N must be a positive integer.")
        n = int(n)
        # Validate the string S
        if n > 0 and len(s) == 0:  # Check for empty input when N is greater than 0
            raise ValueError("S cannot be empty when N is greater than 0.")
        if len(s) != n or not all(c in 'LR' for c in s):
            raise ValueError("Invalid input values. Ensure S is a string of length N containing only 'L' and 'R'.")
        result = final_sequence(n, s)
        print(f"Result: {result}")
    except ValueError as e:
        print(f"Input Error: {str(e)}")
    except Exception as e:
        print(f"Unexpected Error: {str(e)}")
if __name__ == "__main__":
    main()