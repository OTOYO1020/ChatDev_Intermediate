'''
This module contains the logic for the number guessing game application.
'''
from game import Game
class GameApp:
    def __init__(self):
        self.game = Game()
    def run(self):
        '''
        Run the main game loop, prompting the user for guesses.
        '''
        print("Welcome to the Number Guessing Game!")
        print("Guess a number between 1 and 100:")
        while True:
            try:
                user_guess = int(input("Enter your guess: "))
                result = self.game.guess(user_guess)
                print(result)
                if "Correct!" in result:
                    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
                    if play_again == 'yes':
                        self.game.reset()
                    else:
                        print("Thank you for playing!")
                        break
            except ValueError:
                print("Please enter a valid number.")