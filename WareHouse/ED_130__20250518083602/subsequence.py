'''
Module containing functions to count subsequence pairs.
'''
from collections import defaultdict
from typing import List, Dict
MOD = 10**9 + 7
def subsequence_count(sequence: List[int]) -> Dict[int, int]:
    '''
    Count occurrences of each integer in the subsequence and return their counts.
    '''
    count = defaultdict(int)
    for num in sequence:
        count[num] += 1
    return count
def count_subsequence_pairs(S: List[int], T: List[int]) -> int:
    '''
    Count the number of valid subsequence pairs from sequences S and T.
    '''
    count_S = subsequence_count(S)
    count_T = subsequence_count(T)
    total_pairs = 0
    for num in count_S:
        if num in count_T:
            # Calculate the number of distinct non-empty subsequences
            subseq_count_S = (pow(2, count_S[num], MOD) - 1) % MOD  # Non-empty subsequences from S
            subseq_count_T = (pow(2, count_T[num], MOD) - 1) % MOD  # Non-empty subsequences from T
            # Multiply the counts of non-empty subsequences
            total_pairs += (subseq_count_S * subseq_count_T) % MOD
            total_pairs %= MOD
            # Ensure to account for distinct subsequences formed by indices
            # This part is already handled by the way we count subsequences above.
    return total_pairs