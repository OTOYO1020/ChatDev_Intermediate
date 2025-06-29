import math
def is_matching_with_key_change(self, subsequence, B):
    '''
    Check if a subsequence matches with key change.
    Args:
        subsequence (list): Subsequence of A
        B (list): Sequence B
    Returns:
        bool: True if the subsequence matches with key change, False otherwise
    '''
    if len(subsequence) != len(B):
        return False
    for i in range(len(subsequence)):
        if B[i] == 0:
            if subsequence[i] != 0:
                return False
        else:
            key_change = subsequence[i] / B[i]
            if not math.isclose(subsequence[i], B[i] * key_change):
                return False
    return True