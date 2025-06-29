'''
This file implements a basic Gomoku game using standard input and output.
'''
class GomokuGame:
    def __init__(self):
        '''
        Initializes the Gomoku game with a 15x15 board, sets the current player to 'X', and game_over to False.
        '''
        self.board_size = 15
        self.board = [[' ' for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.current_player = 'X'
        self.game_over = False
    def make_move(self, row, col):
        '''
        Makes a move on the board for the current player at the specified row and column.
        Parameters:
        row (int): The row index for the move.
        col (int): The column index for the move.
        Returns:
        str: A message indicating the winner if the game is over, otherwise a message for invalid moves.
        '''
        if self.board[row][col] != ' ':
            return "Invalid move! Cell is already occupied."
        if not self.game_over:
            self.board[row][col] = self.current_player
            if self.check_winner(row, col):
                self.game_over = True
                return f'Player {self.current_player} wins!'
            if self.check_draw():
                self.game_over = True
                return "The game is a draw!"
            self.current_player = 'O' if self.current_player == 'X' else 'X'
        return None
    def check_winner(self, row, col):
        '''
        Checks if the current player has won the game after making a move at the specified row and column.
        Parameters:
        row (int): The row index of the last move.
        col (int): The column index of the last move.
        Returns:
        bool: True if the current player has won, otherwise False.
        '''
        return (self.check_line(row, col, 1, 0) or  # Horizontal
                self.check_line(row, col, 0, 1) or  # Vertical
                self.check_line(row, col, 1, 1) or  # Diagonal \
                self.check_line(row, col, 1, -1))   # Diagonal /
    def check_line(self, row, col, delta_row, delta_col):
        '''
        Checks if there are five consecutive pieces of the current player in a specified direction.
        Parameters:
        row (int): The row index of the last move.
        col (int): The column index of the last move.
        delta_row (int): The change in row index for the direction.
        delta_col (int): The change in column index for the direction.
        Returns:
        bool: True if there are five consecutive pieces, otherwise False.
        '''
        count = 0
        for direction in (1, -1):
            r, c = row, col
            while 0 <= r < self.board_size and 0 <= c < self.board_size and self.board[r][c] == self.current_player:
                count += 1
                r += direction * delta_row
                c += direction * delta_col
        return count >= 5
    def check_draw(self):
        '''
        Checks if the game is a draw (i.e., the board is full and there is no winner).
        Returns:
        bool: True if the game is a draw, otherwise False.
        '''
        for row in self.board:
            if ' ' in row:  # If there's at least one empty cell, it's not a draw
                return False
        return True
    def reset_game(self):
        '''
        Resets the game to its initial state.
        '''
        self.board = [[' ' for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.current_player = 'X'
        self.game_over = False
    def print_board(self):
        '''
        Prints the current state of the game board.
        '''
        for row in self.board:
            print('|'.join(row))
            print('-' * (self.board_size * 2 - 1))
def main():
    '''
    The main function to run the Gomoku game.
    '''
    game = GomokuGame()
    while True:
        game.print_board()
        if game.game_over:
            print(f'Game over! Player {game.current_player} has won!')
            break
        try:
            row = int(input(f"Player {game.current_player}, enter your move row (0-{game.board_size-1}): "))
            col = int(input(f"Player {game.current_player}, enter your move column (0-{game.board_size-1}): "))
            result = game.make_move(row, col)
            if result:
                if result.startswith("Invalid move"):
                    print(result)  # Inform the player of the invalid move
                else:
                    game.print_board()
                    print(result)
                    break
            # Check for game over after a successful move
            if game.game_over:
                print(f'Game over! Player {game.current_player} has won!')
                break
        except (ValueError, IndexError):
            print("Invalid input. Please enter numbers within the board range.")
if __name__ == "__main__":
    main()