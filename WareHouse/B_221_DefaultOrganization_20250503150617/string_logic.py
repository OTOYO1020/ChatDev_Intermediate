'''
Contains the logic to determine if one string can be made equal to another
by swapping adjacent characters.
'''
def can_swap_to_equal(S, T):
    if len(S) != len(T) or len(S) < 2 or len(S) > 100:
        return False
    if not all('a' <= char <= 'z' for char in S) or not all('a' <= char <= 'z' for char in T):
        return False
    if S == T:
        return True  # Early exit if strings are already equal
    # Check for adjacent swaps only if S is not equal to T
    for i in range(len(S) - 1):
        # Swap S[i] and S[i+1] and check if it equals T
        swapped_S = list(S)
        swapped_S[i], swapped_S[i + 1] = swapped_S[i + 1], swapped_S[i]
        if ''.join(swapped_S) == T:
            return True
    return False