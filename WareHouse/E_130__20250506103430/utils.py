'''
Utility functions for subsequence counting.
'''
def count_subsequences(sequence):
    '''
    Count the number of subsequences for each unique integer in the sequence.
    Parameters:
    sequence (list): A list of integers for which to count subsequences.
    Returns:
    dict: A dictionary with integers as keys and the number of subsequences as values.
    '''
    from collections import Counter
    MOD = 10**9 + 7
    if not sequence:  # Check for empty sequence
        return {}
    count = Counter(sequence)
    subsequences_count = {}
    for x in count:
        # Calculate the number of subsequences using modular exponentiation
        if count[x] > 0:
            subsequences_count[x] = (pow(2, count[x], MOD) - 1) % MOD
        else:
            subsequences_count[x] = 0  # Handle case where count[x] is 0
    return subsequences_count
def calculate_total_pairs(subseq_count_S, subseq_count_T):
    '''
    Calculate the total number of matching subsequence pairs from two subsequence counts.
    Parameters:
    subseq_count_S (dict): A dictionary of subsequences counts from sequence S.
    subseq_count_T (dict): A dictionary of subsequences counts from sequence T.
    Returns:
    int: The total number of matching subsequence pairs modulo 10^9 + 7.
    '''
    total_pairs = 0
    MOD = 10**9 + 7
    for x in subseq_count_S:
        if x in subseq_count_T:
            # Correctly use the subsequences counts
            total_pairs += (subseq_count_S[x] * subseq_count_T[x]) % MOD
            total_pairs %= MOD  # Ensure total_pairs remains within the MOD limit
    return total_pairs