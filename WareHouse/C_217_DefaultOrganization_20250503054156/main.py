'''
Main application file for the permutation calculator.
'''
from permutation import calculate_permutation
def is_valid_permutation(permutation, n):
    """
    Validate the permutation to ensure it contains unique values from 1 to N.
    Parameters:
    permutation (list): A list of integers representing the permutation.
    n (int): The expected length of the permutation.
    Returns:
    bool: True if valid, False otherwise.
    """
    if len(permutation) != n:
        return False
    if any(x < 1 or x > n for x in permutation):
        return False
    if len(set(permutation)) != n:
        return False
    return True
def main():
    try:
        # Read the integer N from standard input
        n = int(input())
        if n == 0:
            print('')  # Print an empty line for zero-length permutation
            return
        # Read the permutation P as an array of integers from standard input
        permutation_input = input()
        permutation = list(map(int, permutation_input.split()))
        # Validate the permutation
        if not is_valid_permutation(permutation, n):
            raise ValueError("The permutation must contain unique values from 1 to N.")
        # Calculate the resulting permutation
        result = calculate_permutation(permutation)
        # Print the resulting permutation Q as space-separated integers
        print(' '.join(map(str, result)))
    except ValueError as ve:
        print("Input Error:", str(ve))
    except Exception as e:
        print("Unexpected Error:", str(e))
if __name__ == "__main__":
    main()