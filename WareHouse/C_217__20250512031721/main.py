'''
Main application file for the Permutation Calculator.
Handles input and output for the permutation calculation.
'''
from permutation import find_permutation, validate_input
def main():
    '''
    Main function to handle input and output for the permutation calculation.
    Prompts the user for input values and validates them before processing.
    '''
    try:
        N = int(input("Enter N: "))
        if N < 1:
            print("Invalid input: N must be greater than 0.")
            return
        P = list(map(int, input("Enter P (space-separated): ").split()))
        if not P:
            print("Invalid input: P cannot be empty.")
            return
        is_valid, error_message = validate_input(N, P)
        if is_valid:
            Q = find_permutation(N, P)
            print("Result:", ' '.join(map(str, Q)))
        else:
            print("Invalid input:", error_message)
    except ValueError:
        print("Please enter valid integers.")
if __name__ == "__main__":
    main()