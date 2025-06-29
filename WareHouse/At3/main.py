from typing import List
def count_matching_subsequences(A: List[int], B: List[int]) -> int:
    count = 0
    for i in range(len(A) - len(B) + 1):
        subsequence = A[i:i+len(B)]
        if all(a != 0 or b != 0 for a, b in zip(subsequence, B)):
            count += 1
    return count