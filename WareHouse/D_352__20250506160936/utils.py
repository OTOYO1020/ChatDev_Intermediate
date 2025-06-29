'''
Utility functions for the minimum distance calculator.
'''
def is_consecutive(subsequence, K):
    '''
    Check if the given subsequence can be rearranged to form a consecutive integer sequence.
    '''
    if len(subsequence) != K or len(set(subsequence)) != K:  # Check for duplicates and length
        return False
    max_val = max(subsequence)
    min_val = min(subsequence)
    return (max_val - min_val == K - 1)