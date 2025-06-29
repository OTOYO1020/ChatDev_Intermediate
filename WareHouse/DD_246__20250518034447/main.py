'''
Main application file for finding the smallest integer X
that can be expressed in the form X = a^3 + a^2 * b + a * b^2 + b^3.
'''
from utils import is_valid_input, check_pairs
def find_smallest_integer(N):
    if not is_valid_input(N):
        raise ValueError("Input must be between 0 and 10^18.")
    X = N
    while True:
        if check_pairs(X):
            return X
        X += 1
if __name__ == "__main__":
    N = int(input("Enter an integer N (0 <= N <= 10^18): "))
    try:
        result = find_smallest_integer(N)
        print(f"The smallest integer X is: {result}")
    except ValueError as e:
        print(f"Input Error: {str(e)}")