'''
Module containing the logic for solving alphametic puzzles.
'''
from typing import Optional, Tuple
import itertools
def is_alphametic(S1: str, S2: str, S3: str) -> Optional[Tuple[int, int, int]]:
    '''
    Check if the given strings can be mapped to digits such that N1 + N2 = N3.
    '''
    if len(S1) != len(S2) or len(S2) != len(S3):
        return None
    unique_chars = set(S1 + S2 + S3)
    if len(unique_chars) > 10:
        return None
    for digits in itertools.permutations(range(10), len(unique_chars)):
        char_to_digit = dict(zip(unique_chars, digits))
        # Check for leading zeros
        leading_chars = {S1[0], S2[0], S3[0]}  # Collect all leading characters
        if any(char_to_digit[char] == 0 for char in leading_chars if char in char_to_digit):
            continue
        N1 = int(''.join(str(char_to_digit[c]) for c in S1))
        N2 = int(''.join(str(char_to_digit[c]) for c in S2))
        N3 = int(''.join(str(char_to_digit[c]) for c in S3))
        if N1 + N2 == N3:
            return (N1, N2, N3)
    return None