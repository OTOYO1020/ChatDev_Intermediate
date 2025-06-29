'''
Main application file for the valid divisions calculator.
'''
import sys
from calculator import count_valid_divisions
def main():
    '''
    Main function to handle input and output for the valid divisions calculator.
    '''
    try:
        N = int(input("Enter N (length of sequence): "))
        if N < 0:
            raise ValueError("N must be a non-negative integer.")
        K = int(input("Enter K (target sum): "))
        A = list(map(int, input("Enter A (space-separated integers): ").split()))
        if len(A) != N:
            raise ValueError("Length of A must be equal to N.")
        result = count_valid_divisions(N, K, A)
        print(f"Valid divisions count: {result}")
    except ValueError as e:
        print(f"Input Error: {str(e)}", file=sys.stderr)
if __name__ == "__main__":
    main()