'''
Main entry point for the Gomoku game application.
'''
from game_logic import GameLogic
class GomokuGame:
    def __init__(self):
        self.board_size = 15
        self.game_logic = GameLogic(self.board_size)
        self.current_player = 'black'
        self.play_game()
    def play_game(self):
        '''
        Main loop for playing the game. It prompts the current player for their move,
        updates the game state, and checks for a winner or a draw.
        '''
        while True:
            self.print_board()
            try:
                x, y = map(int, input(f"{self.current_player.capitalize()}'s turn. Enter row and column (0-14): ").split())
                if self.game_logic.place_stone(x, y, self.current_player):
                    if self.game_logic.is_winner(self.current_player):
                        self.print_board()
                        print(f"{self.current_player.capitalize()} wins!")
                        break
                    # Check for a draw only if there is no winner
                    if self.game_logic.is_draw():
                        self.print_board()
                        print("The game is a draw!")
                        break
                    self.current_player = 'white' if self.current_player == 'black' else 'black'
                else:
                    print("Invalid move. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Please enter two numbers between 0 and 14.")
        # Prompt to play again after the game ends
        play_again = input("Do you want to play again? (y/n): ").strip().lower()
        if play_again == 'y':
            self.game_logic.reset()
            self.current_player = 'black'
            self.play_game()  # Restart the game
        else:
            print("Thanks for playing!")
    def print_board(self):
        '''
        Prints the current state of the game board to the console.
        '''
        for row in self.game_logic.board:
            print(' '.join(['.' if cell == '' else cell[0] for cell in row]))
if __name__ == "__main__":
    GomokuGame()