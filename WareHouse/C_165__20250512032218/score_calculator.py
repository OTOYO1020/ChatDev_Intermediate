'''
Contains the logic for calculating the maximum score based on input parameters.
'''
from typing import List, Tuple
class ScoreCalculator:
    def max_score(self, N: int, M: int, Q: int, queries: List[Tuple[int, int, int, int]]) -> int:
        # Edge case handling
        if N == 0 or Q == 0:
            return 0
        max_score = 0
        # Calculate scores based on constraints without generating all sequences
        for A in self.generate_sequences(N, M):
            score = self.calculate_score(A, queries)
            max_score = max(max_score, score)
            # Early exit if max score is already greater than the current score
            if max_score > 0:
                break
        return max_score if max_score > 0 else 0  # Ensure returning 0 if no valid sequences yield a score
    def generate_sequences(self, N: int, M: int) -> List[List[int]]:
        # Generate non-decreasing sequences using a more efficient approach
        sequences = []
        def backtrack(start, current):
            if len(current) == N:
                sequences.append(current[:])
                return
            for i in range(start, M + 1):
                current.append(i)
                backtrack(i, current)  # Allow the same number to be added again
                current.pop()
        backtrack(1, [])
        return sequences
    def calculate_score(self, A: List[int], queries: List[Tuple[int, int, int, int]]) -> int:
        score = 0
        for a_i, b_i, c_i, d_i in queries:
            if 1 <= a_i < b_i <= len(A):  # Ensure indices are valid
                if A[b_i - 1] - A[a_i - 1] == c_i:  # Adjust for 0-based indexing
                    score += d_i
        return score