'''
Contains the logic for finding the maximum length of repeated substrings in a given string.
'''
def max_length_repeated_substring(S: str) -> int:
    N = len(S)
    if N < 2:  # Check for empty string or single character
        return 0
    max_len = 0
    for length in range(1, N):  # Iterate over all possible lengths
        for l1 in range(N - length + 1):  # Starting position for the first substring
            substring = S[l1:l1 + length]
            for l2 in range(l1 + length, N - length + 1):  # Ensure l2 starts after l1 + length
                if substring == S[l2:l2 + length]:  # Compare substrings
                    max_len = max(max_len, length)  # Update max_len if a match is found
    return max_len