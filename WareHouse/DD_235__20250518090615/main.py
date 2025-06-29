'''
Main entry point for the Min Operations application.
'''
import sys
from operations import min_operations
def main():
    '''
    Main function to handle standard input and output for the Min Operations application.
    '''
    try:
        a = int(input("Enter a (2 <= a < 10^6): "))
        N = int(input("Enter N (2 <= N < 10^6): "))
        if not (2 <= a < 10**6) or not (2 <= N < 10**6):
            raise ValueError("Input values are out of bounds.")
        operations_count = min_operations(a, N)
        print(f"Minimum operations: {operations_count}")
    except ValueError as e:
        print(f"Input Error: {str(e)}", file=sys.stderr)
if __name__ == "__main__":
    main()