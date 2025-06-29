'''
Main application file for the integer average subset counter.
'''
import sys
from subset_counter import SubsetCounter
def main():
    '''
    Main function to read input and calculate the number of valid subsets.
    '''
    try:
        # Read the integer N from standard input
        N = int(input("Enter the length of the sequence (N): "))  # Prompt for input
        if N < 1 or N > 20:  # Limit N to a reasonable size
            raise ValueError("N must be between 1 and 20.")
        # Read the sequence of positive integers A from standard input
        A = list(map(int, input(f"Enter {N} positive integers separated by spaces: ").split()))  # Prompt for input
        if len(A) != N:
            raise ValueError("Length of sequence does not match N.")
        if any(x <= 0 for x in A):  # Ensure all integers are positive
            raise ValueError("All integers in the sequence must be positive.")
        counter = SubsetCounter()
        result = counter.count_integer_averages(N, A)
        print(result)  # Print the final result
    except ValueError as e:
        print(f"Input Error: {e}", file=sys.stderr)
    except Exception as e:
        print(f"Unexpected Error: {e}", file=sys.stderr)
if __name__ == "__main__":
    main()