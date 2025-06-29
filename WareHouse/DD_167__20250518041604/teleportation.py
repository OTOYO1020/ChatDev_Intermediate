'''
Module containing the logic for teleportation simulation.
'''
from typing import List
def find_final_town(N: int, A: List[int], K: int) -> int:
    # Validate teleport destinations
    for destination in A:
        if destination < 1 or destination > N:
            raise ValueError(f"Teleport destination {destination} is out of bounds. It must be between 1 and {N}.")
    # Handle edge cases
    if K == 0:
        return 1  # If no teleportations, return starting town
    if N == 1:
        return 1  # If only one town, return that town regardless of K
    current_town = 1  # Starting from Town 1
    visited = {}
    steps = 0
    while steps < K:
        if current_town in visited:
            # Cycle detected
            cycle_length = steps - visited[current_town]
            remaining_steps = (K - steps) % cycle_length
            # Move to the town after the remaining steps in the cycle
            for _ in range(remaining_steps):
                current_town = A[current_town - 1]  # Adjusting for 0-indexing
            return current_town
        visited[current_town] = steps
        current_town = A[current_town - 1]  # Adjusting for 0-indexing
        steps += 1
    return current_town