'''
Main application file for the subsequence length calculator.
'''
import sys
from utils import max_subsequence_length
def main():
    '''
    Main function to handle input and output for the subsequence length calculation.
    '''
    try:
        # Reading input from standard input
        N = int(input("Enter the length of the sequence (N): "))
        D = int(input("Enter the maximum allowed absolute difference (D): "))
        A_input = input("Enter the sequence of integers separated by commas (e.g., 1,2,3 without spaces): ")
        # Convert input string to a list of integers with validation
        A = []
        for x in A_input.split(','):
            try:
                A.append(int(x.strip()))
            except ValueError:
                raise ValueError(f"Invalid integer value: '{x.strip()}'")
        if len(A) != N:
            raise ValueError("The length of the sequence does not match N.")
        max_length = max_subsequence_length(N, D, A)
        print(f"Max Subsequence Length: {max_length}")
    except ValueError as e:
        print(f"Input Error: {str(e)}", file=sys.stderr)
    except Exception as e:
        print(f"Unexpected Error: {str(e)}", file=sys.stderr)
if __name__ == "__main__":
    main()