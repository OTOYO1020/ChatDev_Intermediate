'''
Main file for the Gomoku game application.
'''
class Cell:
    '''
    Represents a single cell in the Gomoku game board.
    '''
    def __init__(self):
        self.value = None  # None, 'X', or 'O'
    def set_value(self, value):
        '''
        Sets the value of the cell.
        '''
        self.value = value
class GomokuGame:
    '''
    Main class for the Gomoku game logic.
    '''
    def __init__(self):
        self.board = [[Cell() for _ in range(15)] for _ in range(15)]
        self.current_player = 'X'
        self.game_over = False
    def print_board(self):
        '''
        Prints the current state of the game board.
        '''
        for row in self.board:
            print(' '.join(cell.value if cell.value else '.' for cell in row))
        print()
    def is_board_full(self):
        '''
        Checks if the board is full.
        '''
        for row in self.board:
            for cell in row:
                if cell.value is None:
                    return False
        return True
    def make_move(self, row, col):
        '''
        Handles a player's move.
        '''
        if self.game_over:
            print("Game is over. No more moves can be made.")
            return
        if self.board[row][col].value is not None:
            print("Invalid move. Try again.")
            return
        self.board[row][col].set_value(self.current_player)
        self.print_board()
        if self.check_winner(row, col):
            print(f"Player {self.current_player} wins!")
            self.game_over = True
        elif self.is_board_full():
            print("The game is a draw!")
            self.game_over = True
        else:
            self.current_player = 'O' if self.current_player == 'X' else 'X'
    def check_winner(self, row, col):
        '''
        Checks if the current player has won the game.
        '''
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]  # Horizontal, Vertical, Diagonal /
        for dr, dc in directions:
            count = 1
            for step in range(1, 5):
                r, c = row + dr * step, col + dc * step
                if 0 <= r < 15 and 0 <= c < 15 and self.board[r][c].value == self.current_player:
                    count += 1
                else:
                    break
            for step in range(1, 5):
                r, c = row - dr * step, col - dc * step
                if 0 <= r < 15 and 0 <= c < 15 and self.board[r][c].value == self.current_player:
                    count += 1
                else:
                    break
            if count >= 5:
                return True
        return False
if __name__ == "__main__":
    game = GomokuGame()
    while not game.game_over:
        try:
            move = input(f"Player {game.current_player}, enter your move (row and column): ")
            row, col = map(int, move.split())
            if 0 <= row < 15 and 0 <= col < 15:
                game.make_move(row, col)
            else:
                print("Move out of bounds. Please enter values between 0 and 14.")
        except ValueError:
            print("Invalid input. Please enter two integers separated by a space.")