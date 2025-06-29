'''
Module for counting triangles from stick lengths.
'''
from typing import List
def count_triangles(N: int, L: List[int]) -> int:
    '''
    Count the number of triangles that can be formed from the given stick lengths.
    Parameters:
    N (int): The number of sticks.
    L (List[int]): The list of stick lengths.
    Returns:
    int: The count of valid triangles that can be formed.
    '''
    if N < 3:
        return 0  # No triangle can be formed with less than 3 sticks
    count = 0
    L.sort()  # Sort the list to make the triangle inequality checks easier
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            k = j + 1  # Start k just after j
            while k < N and L[i] + L[j] > L[k]:
                k += 1
            count += k - j - 1  # Count valid triangles with sticks i, j, and all valid k
    return count