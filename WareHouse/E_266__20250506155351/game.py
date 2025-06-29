'''
Contains the Game class that handles the game logic.
'''
import random
class Game:
    def __init__(self, max_turns):
        self.max_turns = max_turns
    def roll_die(self):
        return random.randint(1, 6)
    def calculate_expected_score(self, current_turn, current_score):
        if current_turn == self.max_turns:
            return current_score
        else:
            # Calculate the expected value of continuing the game
            expected_value_next_roll = (1 + 2 + 3 + 4 + 5 + 6) / 6  # Average of 1 to 6
            # Compare current score with the expected value of continuing
            return max(current_score, expected_value_next_roll)
    def run(self):
        expected_score = 0
        for turn in range(1, self.max_turns + 1):
            die_value = self.roll_die()
            if turn == self.max_turns:
                expected_score += die_value  # Last turn, just take the die value
            else:
                # Use the calculate_expected_score method to determine the expected score
                expected_value = self.calculate_expected_score(turn, die_value)
                expected_score += expected_value
        return expected_score