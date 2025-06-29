'''
Module containing the function to calculate the maximum score in the game.
'''
from typing import List
def max_score(N: int, K: int, C: List[int], P: List[int]) -> int:
    '''
    Calculates the maximum score based on the number of squares, maximum moves,
    scores on squares, and permutation of squares.
    '''
    max_score = 0
    for i in range(N):  # Iterate through each square
        current_score = 0
        current_position = i  # Start from 0-based index
        visited = set()  # Set for tracking visited squares
        cycle_scores = []
        moves_remaining = K
        while moves_remaining > 0:
            if current_position in visited:
                # Cycle detected
                cycle_start_index = cycle_scores.index(C[current_position])
                cycle_score = sum(cycle_scores[cycle_start_index:])
                cycle_length = len(cycle_scores) - cycle_start_index
                # Calculate how many full cycles can be performed
                full_cycles = moves_remaining // cycle_length
                current_score += full_cycles * cycle_score
                moves_remaining -= full_cycles * cycle_length
                break
            visited.add(current_position)  # Mark the current position as visited
            cycle_scores.append(C[current_position])  # Append score of the current square
            current_score += C[current_position]       # Update current score
            current_position = P[current_position]      # Use P directly as it is now 0-based
            moves_remaining -= 1
        # Update max_score with the maximum value found
        max_score = max(max_score, current_score)
    return max_score