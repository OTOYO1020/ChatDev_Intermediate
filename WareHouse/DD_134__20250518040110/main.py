'''
Main application file for the Good Set Checker.
'''
from typing import List
from good_set import is_good_set
def main():
    # Input parsing
    input_data = input("Enter N and the list (0s and 1s) separated by spaces: ").strip().split()
    N = int(input_data[0])
    a = list(map(int, input_data[1:N+1]))
    # Check for good set
    result = is_good_set(N, a)
    if result is not None:
        print(f"Good set exists: {result}")
    else:
        print("No good set exists.")
if __name__ == "__main__":
    main()