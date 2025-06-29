'''
Contains the logic for calculating the modulo of a given integer N.
'''
def calculate_modulo(n):
    if -10**18 <= n <= 10**18:
        # Calculate modulo and ensure non-negative result
        return (n % 998244353 + 998244353) % 998244353
    else:
        raise ValueError("Input must be within the range of -10^18 to 10^18.")