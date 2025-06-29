'''
This file contains the game logic for the Hit and Blow game.
'''
import random
class HitAndBlowGame:
    def __init__(self):
        self.number = self.generate_number()
        self.lives = 7
    def generate_number(self):
        '''
        Generates a random three-digit number with different digits.
        '''
        digits = random.sample(range(10), 3)
        return "".join(str(digit) for digit in digits)
    def check_guess(self, guess):
        '''
        Checks the user's guess and returns the number of hits and blows.
        '''
        if len(guess) != 3 or not guess.isdigit() or len(set(guess)) != 3:
            return "invalid"
        hits = 0
        blows = 0
        guess_digits = list(guess)
        number_digits = list(self.number)
        for i in range(3):
            if guess_digits[i] == number_digits[i]:
                hits += 1
                guess_digits[i] = None
                number_digits[i] = None
        for i in range(3):
            if guess_digits[i] is not None and guess_digits[i] in number_digits:
                blows += 1
                number_digits[number_digits.index(guess_digits[i])] = None
        if hits == 3:
            return "win"
        elif self.lives == 1:
            self.reduce_lives()
            return "lose"
        else:
            self.reduce_lives()
            return {"hits": hits, "blows": blows}
    def reduce_lives(self):
        '''
        Reduces the number of lives by 1.
        '''
        self.lives -= 1