'''
Main file to run the Gomoku game using standard input and output.
'''
from gomoku_logic import GomokuLogic
class GomokuGame:
    def __init__(self):
        self.board_size = 15
        self.logic = GomokuLogic(self.board_size)
        self.current_player = 'X'
    def draw_board(self):
        """
        Draws the current state of the board to the console.
        """
        for row in self.logic.board:
            print(' '.join(['.' if cell == '' else cell for cell in row]))
    def handle_click(self, x, y):
        """
        Handles a player's move by updating the board and checking for a win or draw.
        Parameters:
        x (int): The x-coordinate of the move.
        y (int): The y-coordinate of the move.
        Returns:
        bool: True if the game ends (win or draw), False otherwise.
        """
        if self.logic.make_move(x, y, self.current_player):
            self.draw_board()
            if self.logic.is_winner(self.current_player):
                print(f"Player {self.current_player} wins!")
                return True  # Game ends
            elif self.logic.is_draw():
                print("It's a draw!")
                return True  # Game ends
            self.current_player = 'O' if self.current_player == 'X' else 'X'
        else:
            print("Invalid move. The cell is already occupied.")
        return False  # Game continues
    def play(self):
        """
        Starts the game loop, prompting players for their moves.
        """
        self.draw_board()
        game_ongoing = True
        while game_ongoing:
            user_input = input(f"Player {self.current_player}, enter your move (x y): ")
            try:
                x, y = map(int, user_input.split())
                # Validate coordinates
                if 0 <= x < self.board_size and 0 <= y < self.board_size:
                    game_ongoing = not self.handle_click(x, y)
                else:
                    print("Invalid move. Coordinates must be between 0 and 14.")
            except ValueError:
                print("Invalid input. Please enter two integers separated by a space.")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
if __name__ == "__main__":
    game = GomokuGame()
    game.play()