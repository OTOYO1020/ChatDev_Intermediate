'''
Main application file for calculating the lost integer.
'''
import sys
from utils import validate_input  # Ensure to import the validate_input function
def calculate_lost_integer(N, A):
    '''
    Calculates the lost integer based on the expected and actual sums.
    '''
    expected_sum = (N + 1) * (N + 2) // 2
    actual_sum = sum(A)
    lost_integer = expected_sum - actual_sum
    return lost_integer
if __name__ == "__main__":
    # Read input from standard input
    n_input = sys.stdin.readline().strip()
    a_input = sys.stdin.readline().strip()
    # Validate input
    is_valid, A = validate_input(n_input, a_input)
    if not is_valid:
        sys.exit(1)  # Exit if input is invalid
    N = int(n_input)
    # Calculate and print the lost integer
    lost_integer = calculate_lost_integer(N, A)
    print(lost_integer)