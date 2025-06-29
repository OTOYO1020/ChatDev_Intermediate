'''
Contains the function to perform the ball swapping logic.
'''
from typing import List
def perform_swaps(N: int, Q: int, operations: List[int]) -> List[int]:
    balls = list(range(1, N + 1))  # Initialize balls
    for i in range(Q):
        x_i = operations[i]
        index = balls.index(x_i)  # Find the index of the ball
        if index < N - 1:  # If not the rightmost ball
            swap(balls, index, index + 1)  # Swap with the right ball
        else:  # If it is the rightmost ball
            swap(balls, index, index - 1)  # Swap with the left ball
    return balls
def swap(balls: List[int], index1: int, index2: int):
    balls[index1], balls[index2] = balls[index2], balls[index1]  # Swap the balls