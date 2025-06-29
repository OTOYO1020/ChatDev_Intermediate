'''
Contains the logic for die simulation and expected score calculation.
'''
import random
def simulate_die_throw():
    '''
    Simulates a die throw, returning a random integer between 1 and 6.
    '''
    return random.randint(1, 6)
def expected_score(N: int) -> float:
    '''
    Calculates the expected score based on the number of turns N.
    Parameters:
    N (int): The number of turns in the game.
    Returns:
    float: The expected score based on the game logic.
    '''
    if N == 1:
        return float(simulate_die_throw())
    # Initialize a list to store expected scores for each turn
    expected_scores = [0] * (N + 1)
    # Calculate expected scores from the last turn back to the first
    for turn in range(N, 0, -1):
        die_value = simulate_die_throw()
        # Calculate the expected score if the game continues
        if turn > 1:
            expected_future_score = 3.5  # Expected value of a fair die
            continue_score = expected_future_score + expected_scores[turn - 1]
        else:
            continue_score = die_value  # If it's the last turn, just take the die value
        # Compare the continue score with the die value
        expected_scores[turn] = max(continue_score, die_value)
    # Return the expected score for the first turn
    return expected_scores[1]