'''
Utility functions for calculating the maximum product of two integers formed by permuting the digits of a given integer.
'''
from itertools import permutations
def max_product_of_separated_integers(N: int) -> int:
    '''
    Calculates the maximum product of two positive integers formed by permuting the digits of N.
    '''
    digits = str(N)
    max_product = 0
    # Generate all unique permutations of the digits
    unique_permutations = set(permutations(digits))
    for perm in unique_permutations:
        perm_str = ''.join(perm)
        # Split the permutation into two non-empty parts
        for i in range(1, len(perm_str)):
            part1 = perm_str[:i]
            part2 = perm_str[i:]
            # Check for valid integers (no leading zeros and not zero)
            if (part1[0] != '0' and part2[0] != '0' and 
                len(part1) > 0 and len(part2) > 0):
                num1 = int(part1)
                num2 = int(part2)
                product = num1 * num2
                max_product = max(max_product, product)
    return max_product