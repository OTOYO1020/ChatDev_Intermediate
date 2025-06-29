'''
This file contains the game logic for the Hit and Blow game.
'''
import random
class HitAndBlowGame:
    def __init__(self):
        self.number = self.generate_number()
        self.remaining_lives = 7
        self.game_over = False
    def generate_number(self):
        '''
        Generates a random three-digit number with different digits.
        Returns:
            str: Random three-digit number
        '''
        digits = random.sample(range(10), 3)
        return ''.join(map(str, digits))
    def check_guess(self, guess):
        '''
        Checks the user's guess and returns the number of hits and blows.
        Parameters:
            guess (str): User's guess
        Returns:
            dict: Dictionary containing the number of hits, blows, and game_over flag
        '''
        if self.game_over:
            return {'hits': 0, 'blows': 0, 'game_over': True}
        if guess == self.number:
            self.game_over = True
            return {'hits': 3, 'blows': 0, 'game_over': True}
        hits = sum(1 for x, y in zip(guess, self.number) if x == y)
        common_digits = set(guess) & set(self.number)
        blows = len(common_digits) - hits
        return {'hits': hits, 'blows': blows, 'game_over': self.game_over}
    def reduce_life(self):
        '''
        Reduces the number of remaining lives by 1.
        '''
        self.remaining_lives -= 1
    def get_remaining_lives(self):
        '''
        Returns the number of remaining lives.
        Returns:
            int: Number of remaining lives
        '''
        return self.remaining_lives
    def get_number(self):
        '''
        Returns the generated number.
        Returns:
            str: Generated number
        '''
        return self.number