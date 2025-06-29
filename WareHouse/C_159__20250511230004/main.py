'''
Gomoku Game Implementation for Command Line
'''
class GomokuGame:
    def __init__(self):
        self.board_size = 15
        self.board = [['' for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.current_player = 'X'
        self.game_over = False
    def make_move(self, x, y):
        '''
        Places the current player's mark on the board at the specified coordinates.
        Parameters:
            x (int): The row index for the move.
            y (int): The column index for the move.
        Returns:
            str: A message indicating if the current player has won, if the game is a draw, or if the move was successful.
        '''
        if self.board[x][y] != '':
            return "Invalid move. The cell is already occupied."  # New feedback for occupied cell
        if not self.game_over:
            self.board[x][y] = self.current_player
            if self.check_win():
                self.game_over = True
                return f'Player {self.current_player} wins!'
            if all(cell != '' for row in self.board for cell in row):  # Check for a draw
                self.game_over = True
                return 'The game is a draw!'
            self.current_player = 'O' if self.current_player == 'X' else 'X'
        return None
    def check_win(self):
        '''
        Checks the board for a winning condition.
        Returns:
            bool: True if there is a winning condition, otherwise False.
        '''
        for x in range(self.board_size):
            for y in range(self.board_size):
                if self.board[x][y] == '':
                    continue
                if self.check_direction(x, y, 1, 0) or self.check_direction(x, y, 0, 1) or \
                   self.check_direction(x, y, 1, 1) or self.check_direction(x, y, 1, -1):
                    return True
        return False
    def check_direction(self, x, y, dx, dy):
        '''
        Checks for consecutive pieces in a specified direction.
        Parameters:
            x (int): The starting row index.
            y (int): The starting column index.
            dx (int): The change in row index for each step.
            dy (int): The change in column index for each step.
        Returns:
            bool: True if there are at least 5 consecutive pieces, otherwise False.
        '''
        count = 0
        # Check in the forward direction
        for i in range(5):  # Check for at least 5 in a row
            nx, ny = x + i * dx, y + i * dy
            if 0 <= nx < self.board_size and 0 <= ny < self.board_size and self.board[nx][ny] == self.board[x][y]:
                count += 1
            else:
                break
        # Check in the opposite direction
        for i in range(1, 5):  # Check for additional pieces in the opposite direction
            nx, ny = x - i * dx, y - i * dy
            if 0 <= nx < self.board_size and 0 <= ny < self.board_size and self.board[nx][ny] == self.board[x][y]:
                count += 1
            else:
                break
        return count >= 5  # Ensure at least 5 in a row for a win
    def reset_game(self):
        '''
        Resets the game to the initial state.
        '''
        self.board = [['' for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.current_player = 'X'
        self.game_over = False
    def print_board(self):
        '''
        Prints the current state of the game board.
        '''
        for row in self.board:
            print(' '.join(['.' if cell == '' else cell for cell in row]))
def main():
    game = GomokuGame()
    while not game.game_over:
        game.print_board()
        print(f"Player {game.current_player}'s turn.")
        try:
            x, y = map(int, input("Enter your move (row and column): ").split())
            if 0 <= x < game.board_size and 0 <= y < game.board_size:
                result = game.make_move(x, y)
                if result:
                    game.print_board()
                    print(result)
            else:
                print("Invalid move. Please enter row and column within the board size.")
        except ValueError:
            print("Invalid input. Please enter two integers separated by space.")
if __name__ == "__main__":
    main()