'''
Main application file for the Permutation Finder.
'''
import sys
from permutation import find_previous_permutation
def main():
    '''
    Main function to handle input and output for the permutation finder.
    '''
    try:
        # Read input from standard input
        input_data = sys.stdin.read().strip().splitlines()
        N = int(input_data[0])
        K = int(input_data[1])
        P = list(map(int, input_data[2].split(',')))
        # Call the function to find the previous permutation
        result = find_previous_permutation(N, P, K)
        # Print the result
        print(result)
    except Exception as e:
        print(f"Input Error: {str(e)}")
if __name__ == "__main__":
    main()