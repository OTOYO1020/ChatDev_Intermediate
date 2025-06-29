'''
Utility file for finding the maximum length of non-overlapping substrings.
'''
class SubstringFinder:
    def __init__(self, s):
        self.s = s
    def max_non_overlapping_length(self):
        max_length = 0
        n = len(self.s)
        for length in range(1, n // 2 + 1):
            seen_substrings = {}  # Store the last index of each substring
            for l1 in range(n - length + 1):
                substring = self.s[l1:l1 + length]
                if substring in seen_substrings:
                    # Check for non-overlapping condition
                    if l1 >= seen_substrings[substring] + length:
                        max_length = length  # Update max_length if valid non-overlapping found
                # Only update the last index if it's the first occurrence or non-overlapping
                if substring not in seen_substrings or l1 >= seen_substrings[substring] + length:
                    seen_substrings[substring] = l1  # Update the last index of the substring
        return max_length