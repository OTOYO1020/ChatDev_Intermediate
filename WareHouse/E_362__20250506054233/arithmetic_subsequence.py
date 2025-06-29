'''
Module for counting arithmetic subsequences in a given sequence.
'''
from collections import defaultdict
from itertools import combinations
class ArithmeticSubsequence:
    MODULO = 998244353
    @staticmethod
    def count_arithmetic_subsequences(A):
        """
        Count the number of arithmetic subsequences of all lengths from 1 to N.
        Args:
            A (list): A list of integers representing the sequence.
        Returns:
            list: A list containing the count of arithmetic subsequences for each length k.
        """
        N = len(A)
        results = [0] * N  # Initialize results for lengths 1 to N
        for k in range(1, N + 1):
            count = 0
            if k == 1:
                count = N  # Every single element is an arithmetic subsequence of length 1
            else:
                for subseq in combinations(A, k):
                    if ArithmeticSubsequence.is_arithmetic(subseq):
                        count += 1
            results[k - 1] = count % ArithmeticSubsequence.MODULO
        return results
    @staticmethod
    def is_arithmetic(subseq):
        """
        Check if a given subsequence forms an arithmetic sequence.
        Args:
            subseq (tuple): A tuple representing the subsequence.
        Returns:
            bool: True if the subsequence is arithmetic, False otherwise.
        """
        if len(subseq) < 2:
            return True
        common_diff = subseq[1] - subseq[0]
        for i in range(1, len(subseq) - 1):
            if subseq[i + 1] - subseq[i] != common_diff:
                return False
        return True