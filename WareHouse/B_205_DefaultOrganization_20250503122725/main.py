'''
Main application file for the permutation checker.
'''
from utils import is_permutation
def main():
    '''
    Main function to read input and check for permutations.
    '''
    try:
        # Read the integer N from standard input
        n = int(input())
        # Handle the case where n is 0
        if n == 0:
            sequence_input = input().split()
            if len(sequence_input) == 0:
                print("YES")
            else:
                print("NO")
            return
        # Read the sequence of integers A from standard input
        sequence_input = input().split()
        # Validate that all inputs are integers
        sequence = []
        for item in sequence_input:
            try:
                sequence.append(int(item))
            except ValueError:
                print(f"Input Error: '{item}' is not a valid integer.")
                return
        # Check if the length of the sequence matches N
        if len(sequence) != n:
            print("Input Error: The number of integers provided does not match N.")
            return
        # Check if the sequence is a permutation
        result = is_permutation(n, sequence)
        # Print the result
        if result:
            print("YES")
        else:
            print("NO")
    except ValueError:
        print("Input Error: Please enter a valid integer for N.")
if __name__ == "__main__":
    main()