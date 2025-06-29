'''
This file contains the data-related classes and functions.
'''
import random
class GameData:
    def __init__(self):
        self.remaining_lives = 7
        self.generate_number()
        self.last_guess = None
    def generate_number(self):
        self.generated_number = ''.join(random.sample('123456789', 3))
    def check_guess(self, guess):
        hits = 0
        blows = 0
        if not self.validate_input(guess):
            return hits, blows
        for i in range(3):
            if guess[i] == self.generated_number[i]:
                hits += 1
            elif guess[i] in self.generated_number:
                blows += 1
        if guess == self.generated_number:
            self.remaining_lives = 0
        else:
            self.remaining_lives -= 1
        self.last_guess = guess
        return hits, blows
    def is_game_over(self):
        return self.remaining_lives == 0 or self.is_game_won()
    def is_game_won(self):
        return self.generated_number == self.last_guess
    def validate_input(self, user_input):
        if len(user_input) != 3 or not user_input.isdigit():
            return False
        digits = set(user_input)
        if len(digits) != 3 or len(user_input) != len(digits):
            return False
        return True