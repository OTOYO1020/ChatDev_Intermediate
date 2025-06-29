'''
Logic file containing the function to determine survivors in the game.
'''
from typing import List
def determine_survivors(N: int, K: int, Q: int, A: List[int]) -> List[int]:
    '''
    Determines the indices of players who have scores greater than 0 after processing answers.
    Parameters:
    N (int): Number of players.
    K (int): Initial score for each player.
    Q (int): Number of answers.
    A (List[int]): List of indices of players who answered correctly.
    Returns:
    List[int]: List of indices of surviving players.
    '''
    # Validate the input list A
    if any(answer < 0 or answer >= N for answer in A):
        raise ValueError("All answers must be valid indices between 0 and N-1.")
    scores = [K] * N  # Initialize scores for all players
    # Decrement scores for players who did not answer correctly
    for answer in A:
        for i in range(N):
            if i != answer:  # Decrement score for all except the one who answered correctly
                scores[i] -= 1  # Decrement by 1 for each incorrect answer
    # Collect indices of survivors
    survivors = [i for i in range(N) if scores[i] > 0]  
    return survivors