'''
Contains the logic for counting valid palindromic strings.
'''
from typing import List, Tuple
def count_palindromic_strings(T: int, test_cases: List[Tuple[int, str]]) -> List[int]:
    MOD = 998244353
    results = []
    for N, S in test_cases:
        if N > len(S):
            results.append(0)  # No valid palindromic strings if N is greater than length of S
            continue
        count = 0
        half_length = (N + 1) // 2
        # Generate valid palindromic strings
        for i in range(26 ** half_length):
            # Generate the first half of the palindrome
            first_half = []
            temp = i
            for j in range(half_length):
                first_half.append(chr((temp % 26) + ord('A')))
                temp //= 26
            # Create the full palindrome
            if N % 2 == 0:
                palindrome = ''.join(first_half + first_half[::-1])
            else:
                palindrome = ''.join(first_half + first_half[-2::-1])
            # Check if the generated palindrome is valid
            if palindrome <= S:
                count += 1
                count %= MOD
        results.append(count)
    return results