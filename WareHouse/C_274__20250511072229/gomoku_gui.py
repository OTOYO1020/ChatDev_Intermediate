'''
This module contains the GomokuGUI class which handles the console interface for the game.
'''
from gomoku_game import GomokuGame
class GomokuGUI:
    def __init__(self):
        '''
        Initializes the GUI for the Gomoku game, creating a new game instance.
        '''
        self.game = GomokuGame()
    def display_board(self):
        '''
        Displays the current state of the game board in the console.
        '''
        for row in self.game.board:
            print(' | '.join(row))
            print('-' * 29)
    def play_game(self):
        '''
        Manages the main game loop, allowing players to make moves until there is a winner or a draw.
        '''
        while self.game.winner is None:
            self.display_board()
            try:
                row = int(input(f"Player {self.game.current_player}, enter your move row (0-14): "))
                col = int(input(f"Player {self.game.current_player}, enter your move column (0-14): "))
                self.game.make_move(row, col)
            except ValueError:
                print("Invalid input. Please enter integers only.")
        self.display_board()
        if self.game.winner == 'Draw':
            print("The game is a draw!")
        else:
            print(f"Player {self.game.winner} wins!")
        # Prompt to reset the game or exit
        while True:
            reset_choice = input("Do you want to play again? (yes/no): ").strip().lower()
            if reset_choice == 'yes':
                self.reset_game()
                self.play_game()  # Start a new game
                break
            elif reset_choice == 'no':
                print("Thank you for playing! Goodbye!")
                break
            else:
                print("Invalid choice. Please enter 'yes' or 'no'.")
    def reset_game(self):
        '''
        Resets the game using the reset method from the GomokuGame class.
        '''
        self.game.reset_game()