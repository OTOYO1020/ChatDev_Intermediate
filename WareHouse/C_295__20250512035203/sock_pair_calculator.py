'''
This module contains the SockPairCalculator class that provides methods
to calculate the maximum number of pairs of socks from a list of colors.
'''
from typing import List
from collections import Counter
class SockPairCalculator:
    def max_pairs(self, N: int, A: List[int]) -> int:
        """
        Calculate the maximum number of pairs of socks that can be formed.
        :param N: The number of socks
        :param A: List of sock colors
        :return: The maximum number of pairs
        """
        # Count the frequency of each sock color
        color_count = Counter(A)
        # Calculate the number of pairs
        total_pairs = sum(count // 2 for count in color_count.values())
        return total_pairs
    def validate_input(self, N: int, A: List[int]) -> bool:
        """
        Validate the input values.
        :param N: The number of socks
        :param A: List of sock colors
        :return: True if valid, False otherwise
        """
        if N < 1 or N > 500000 or len(A) != N:
            return False
        if any(not isinstance(color, int) or color < 1 for color in A):
            return False
        return True