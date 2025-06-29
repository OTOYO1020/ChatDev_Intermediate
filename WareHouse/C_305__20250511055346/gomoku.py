'''
This module contains the game logic for the Gomoku game.
'''
class GomokuGame:
    def __init__(self):
        self.board = [[' ' for _ in range(15)] for _ in range(15)]
        self.current_player = 'X'
        self.winner = None
    def make_move(self, row, col):
        '''
        Attempts to place the current player's mark on the board at the specified row and column.
        Returns True if the move was successful, False otherwise.
        '''
        if self.board[row][col] == ' ' and self.winner is None:
            self.board[row][col] = self.current_player
            if self.check_winner(row, col):
                self.winner = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            return True  # Move was successful
        return False  # Move was invalid
    def check_winner(self, row, col):
        '''
        Checks if the current player has won the game after making a move at the specified row and column.
        '''
        return (self.check_direction(row, col, 1, 0) or  # Horizontal
                self.check_direction(row, col, 0, 1) or  # Vertical
                self.check_direction(row, col, 1, 1) or  # Diagonal /
                self.check_direction(row, col, 1, -1))   # Diagonal \
    def check_direction(self, row, col, delta_row, delta_col):
        '''
        Checks in both directions for a winning sequence of five marks.
        '''
        count = 0
        for direction in [1, -1]:  # Check both directions
            r, c = row, col
            while 0 <= r < 15 and 0 <= c < 15 and self.board[r][c] == self.current_player:
                count += 1
                r += delta_row * direction  # Move in the current direction
                c += delta_col * direction  # Move in the current direction
        return count >= 5
    def reset_game(self):
        '''
        Resets the game board and current player to start a new game.
        '''
        self.board = [[' ' for _ in range(15)] for _ in range(15)]
        self.current_player = 'X'
        self.winner = None
    def print_board(self):
        '''
        Prints the current state of the game board to the console.
        '''
        for row in self.board:
            print('|'.join(row))
            print('-' * 29)