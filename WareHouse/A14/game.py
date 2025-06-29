'''
This file contains the game logic for the Hit and Blow game.
'''
import random
class Game:
    def __init__(self):
        self.number = self.generate_number()
        self.remaining_lives = 7
    def generate_number(self):
        '''
        Generates a random three-digit number with different digits.
        Returns:
            str: The generated number
        '''
        digits = random.sample(range(1, 10), 3)
        return ''.join(map(str, digits))
    def validate_input(self, guess):
        '''
        Validates the user's input.
        Parameters:
            guess (str): The user's guess
        Returns:
            bool: True if the input is valid, False otherwise
        '''
        if len(guess) != 3:
            return False
        if not guess.isdigit():
            return False
        if len(set(guess)) != 3:
            return False
        return True
    def compare_numbers(self, guess):
        '''
        Compares the user's guess with the generated number and determines the hits and blows.
        Parameters:
            guess (str): The user's guess
        Returns:
            str: The result of the guess (hit, blow, or incorrect)
        '''
        hits = 0
        blows = 0
        for i in range(3):
            if guess[i] == self.number[i]:
                hits += 1
            elif guess[i] in self.number:
                blows += 1
        if hits == 3:
            return "win"
        if self.remaining_lives == 1:
            return "lose"
        self.remaining_lives -= 1
        return f"Hits: {hits}, Blows: {blows}"
    def make_guess(self, guess):
        '''
        Makes a guess based on the user's input and updates the game state.
        Parameters:
            guess (str): The user's guess
        Returns:
            str: The result of the guess (hit, blow, incorrect, win, or lose)
        '''
        if not self.validate_input(guess):
            return "Incorrect input. Please enter a valid three-digit number with different digits."
        if guess == self.number:
            return "win"
        result = self.compare_numbers(guess)
        if result == "win" or result == "lose":
            return result
        return result