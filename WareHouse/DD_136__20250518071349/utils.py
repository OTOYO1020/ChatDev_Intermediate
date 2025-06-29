'''
Utility functions for input validation and counting children.
'''
from typing import List
def validate_input(S: str) -> bool:
    """
    Validates the input string S.
    Ensures that its length is between 2 and 100,000,
    starts with 'R', and ends with 'L'.
    """
    return 2 <= len(S) <= 100000 and S[0] == 'R' and S[-1] == 'L'
def count_children(S: str) -> List[int]:
    """
    Counts the number of children on each square based on the input string S.
    Each character 'R' moves a child to the right, and 'L' moves a child to the left.
    """
    N = len(S)
    children_count = [1] * N  # Initialize with 1 child on each square
    for i in range(N):
        if S[i] == 'R' and i + 1 < N:
            children_count[i + 1] += 1  # Move child to the right
        elif S[i] == 'L' and i - 1 >= 0:
            children_count[i - 1] += 1  # Move child to the left
    return children_count