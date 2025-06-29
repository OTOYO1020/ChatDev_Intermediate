'''
Main application file for sorting a permutation from standard input.
'''
from permutation_sorter import PermutationSorter
def main():
    # Read the length of the permutation
    N = int(input("Enter the length of the permutation (N): "))
    # Read the permutation array
    A = list(map(int, input("Enter the permutation array (space-separated): ").split()))
    sorter = PermutationSorter(A)
    try:
        swap_count = sorter.sort()
        print("Total swaps performed:", swap_count)
    except ValueError as e:
        print(e)
if __name__ == "__main__":
    main()