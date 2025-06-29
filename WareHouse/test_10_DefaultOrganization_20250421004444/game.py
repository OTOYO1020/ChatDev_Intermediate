'''
This module contains the game logic for the number guessing game.
'''
import random
class Game:
    def __init__(self):
        self.reset()  # Initialize the game by resetting it
    def guess(self, user_guess):
        '''
        Evaluate the user's guess against the number to guess.
        '''
        self.attempts += 1
        if user_guess < self.number_to_guess:
            return "Too low! Remember, the number is between 1 and 100."
        elif user_guess > self.number_to_guess:
            return "Too high! Remember, the number is between 1 and 100."
        else:
            return "Correct! You've guessed the number in {} attempts.".format(self.attempts)
    def reset(self):
        '''
        Reset the game by generating a new number and resetting attempts.
        '''
        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0