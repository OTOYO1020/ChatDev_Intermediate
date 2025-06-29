'''
Module for calculating the maximum valid subsequence length from a string based on given queries.
'''
class SubsequenceCalculator:
    def __init__(self, string):
        self.string = string
    def max_valid_subsequence_length(self, queries):
        max_length = 0
        for L, R in queries:
            # Validate the range of L and R before slicing
            if L < 1 or R < 1 or L > len(self.string) or R > len(self.string) or L > R:
                print(f"Invalid query: L={L}, R={R}. Must satisfy 1 <= L <= R <= {len(self.string)}. Skipping.")
                continue  # Skip invalid queries
            T = self.string[L-1:R]  # Adjust for 0-based indexing
            # Check if T is empty after slicing
            if len(T) == 0:
                print(f"Empty substring for query: L={L}, R={R}. Skipping.")
                continue  # Skip if T is empty
            # Check if the length of T is not odd
            if len(T) % 2 != 1:
                print(f"Substring length is not odd for query: L={L}, R={R}. Skipping.")
                continue  # Skip if length is not odd
            # Count occurrences of '1', '2', and '/'
            count_1 = T.count('1')
            count_2 = T.count('2')
            count_slash = T.count('/')
            # Check if the counts meet the requirements for a valid subsequence
            if (count_1 >= (len(T) - 1) // 2 and 
                count_2 >= (len(T) - 1) // 2 and 
                count_slash > 0):
                valid_length = count_1 + count_2 + 1
                max_length = max(max_length, valid_length)
        # Ensure that if no valid subsequence was found, we return 0
        return max_length if max_length > 0 else 0