'''
Module for calculating the number of valid pairs (i, j) where i * j is a perfect square.
'''
import math
def count_perfect_square_pairs(n):
    count = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if is_perfect_square(i * j):  # Check if the product i * j is a perfect square
                count += 1
    return count
def is_perfect_square(x):
    root = int(math.isqrt(x))
    return root * root == x