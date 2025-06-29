'''
Contains functions to calculate the minimum window width for fitting words into lines.
'''
from typing import List
def min_window_width(N: int, M: int, L: List[int]) -> int:
    def can_fit_in_lines(W: int, M: int, L: List[int]) -> bool:
        """
        Check if the words can fit within M lines given a maximum width W.
        Args:
        W (int): The maximum width of a line.
        M (int): The maximum number of lines allowed.
        L (List[int]): A list of integers representing the widths of the words.
        Returns:
        bool: True if the words fit within the specified number of lines, False otherwise.
        """
        current_line_width = 0
        line_count = 1
        for width in L:
            if current_line_width + width > W:
                line_count += 1
                current_line_width = width  # Start new line with the current word
                if line_count > M:
                    return False
            else:
                if current_line_width > 0:  # Only add space if it's not the first word in the line
                    current_line_width += 1  # Account for space between words
                current_line_width += width
        return True
    left = max(L)
    right = sum(L) + (N - 1)
    while left < right:
        mid = (left + right) // 2
        if can_fit_in_lines(mid, M, L):
            right = mid
        else:
            left = mid + 1
    return left