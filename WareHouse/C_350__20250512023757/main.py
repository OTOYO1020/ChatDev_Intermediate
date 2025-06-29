'''
Main entry point for the Permutation Sorter application.
'''
from permutation_sorter import transform_permutation
def main():
    '''
    Handles input and output for the permutation sorter.
    '''
    try:
        # Read input from standard input
        N = int(input("Enter the size of the permutation (N): "))
        A = list(map(int, input("Enter the permutation (space-separated): ").split()))
        # Call the transformation function
        sorted_permutation = transform_permutation(N, A)
        # Print the sorted permutation
        print(f"Sorted Permutation: {sorted_permutation}")
    except ValueError as e:
        print(f"Input Error: {e}")
if __name__ == "__main__":
    main()