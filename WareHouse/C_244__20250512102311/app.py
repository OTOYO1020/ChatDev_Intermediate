'''
App class to manage the game logic.
'''
from game import Game
import sys
class App:
    def __init__(self):
        self.game = None
    def run(self):
        '''
        Start the application and initialize the game.
        '''
        n = int(input("Enter an integer N (1-1000): "))
        if 1 <= n <= 1000:
            self.game = Game(n)
            self.play_game()
        else:
            print("Error: N must be between 1 and 1000.", file=sys.stderr)
    def play_game(self):
        '''
        Main game loop to handle declarations and game flow.
        '''
        while not self.game.game_over:
            takahashi_declaration = self.game.declare_integer()
            if takahashi_declaration is None:
                print("Game Over: No more integers to declare.")
                break
            print(takahashi_declaration)  # Output the declared integer
            sys.stdout.flush()  # Flush the output
            while True:  # Loop until a valid input is received
                try:
                    aoki_declaration = int(input(f"Enter Aoki's declared integer (0 to end, between 0 and {2 * self.game.n + 1}): "))
                    if aoki_declaration < 0 or aoki_declaration > 2 * self.game.n + 1:
                        print(f"Error: Aoki's declaration must be between 0 and {2 * self.game.n + 1}.", file=sys.stderr)
                        continue  # Prompt for input again
                    break  # Valid input received, exit the loop
                except ValueError:
                    print("Error: Please enter a valid integer.", file=sys.stderr)
            if self.game.check_aoki_declaration(aoki_declaration):
                print("Game Over: Takahashi has won!")
                break