'''
Module containing the function to count the ways to pick balls from bags.
'''
from typing import List
def countWays(N: int, L: List[int], A: List[List[int]], X: int) -> int:
    '''
    Counts the number of ways to pick balls from bags such that their product equals X.
    Parameters:
    N (int): Number of bags.
    L (List[int]): List of counts of balls in each bag.
    A (List[List[int]]): List of lists containing the integers on the balls.
    X (int): Target product.
    Returns:
    int: Number of valid combinations.
    '''
    # Early exit if X is less than 1
    if X < 1:
        return 0
    # Check if there are any zeros in the bags
    has_zero = any(0 in bag for bag in A)
    if X == 0:
        return 1 if has_zero else 0  # Return 1 if there's at least one zero in the bags
    memo = {}
    def backtrack(bag_index, current_product):
        if (bag_index, current_product) in memo:
            return memo[(bag_index, current_product)]
        if bag_index == N:
            return 1 if current_product == X else 0
        if current_product > X:
            return 0  # Early exit if current product exceeds X
        count = 0
        for ball in A[bag_index]:
            if ball == 0:
                continue  # Skip further processing for this bag since product is now zero
            new_product = current_product
            while new_product <= X:
                count += backtrack(bag_index + 1, new_product)
                if new_product > X // ball:  # Prevent overflow and unnecessary calculations
                    break
                new_product *= ball  # Multiply by the same ball to consider multiple selections
        count += backtrack(bag_index + 1, current_product)  # Skip current bag
        memo[(bag_index, current_product)] = count
        return count
    return backtrack(0, 1)  # Start with the first bag and product of 1