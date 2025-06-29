'''
Main application file for the command-line program to calculate minimum operations
to make '1's contiguous in a given string.
'''
from utils import count_min_operations
def main():
    try:
        N = int(input("Enter integer N: "))
        S = input("Enter string S: ")
        if len(S) != N:
            raise ValueError("Length of S must be equal to N.")
        min_operations = count_min_operations(N, S)
        print(f"Minimum operations: {min_operations}")
    except ValueError as e:
        print(f"Input Error: {str(e)}")
if __name__ == "__main__":
    main()