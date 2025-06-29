'''
Module to find the k-th occurrence of numbers in a sequence.
'''
from typing import List, Tuple
def find_kth_occurrence(N: int, A: List[int], Q: int, queries: List[Tuple[int, int]]) -> List[int]:
    if N == 0:  # Handle the case where A is empty
        return [-1] * Q  # Return -1 for each query since there are no occurrences
    occurrences = {}
    # Record occurrences of each number
    for index, number in enumerate(A):
        if number not in occurrences:
            occurrences[number] = []
        occurrences[number].append(index)
    results = []
    for x, k in queries:
        if x in occurrences and len(occurrences[x]) >= k:
            results.append(occurrences[x][k - 1])  # k is 1-based index
        else:
            results.append(-1)
    return results