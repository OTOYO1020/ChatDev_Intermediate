'''
Contains the logic for the Gomoku game.
'''
class GomokuGame:
    def __init__(self):
        self.board = [[' ' for _ in range(15)] for _ in range(15)]
        self.current_player = 'X'
        self.winner = None
    def make_move(self, row, col):
        '''
        Places a move on the board for the current player.
        '''
        if self.winner is not None:
            raise ValueError("Game over. No more moves can be made.")
        if not (0 <= row < 15 and 0 <= col < 15):
            raise ValueError("Move out of bounds.")
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            if self.check_winner(row, col):
                self.winner = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
        else:
            raise ValueError("Cell already occupied.")
    def check_winner(self, row, col):
        '''
        Checks if the current player has won the game.
        '''
        return (self.check_line(row, col, 1, 0) or  # Horizontal
                self.check_line(row, col, 0, 1) or  # Vertical
                self.check_line(row, col, 1, 1) or  # Diagonal \
                self.check_line(row, col, 1, -1))   # Diagonal /
    def check_line(self, row, col, delta_row, delta_col):
        '''
        Checks for a winning line in the specified direction.
        '''
        count = 0
        for direction in [1, -1]:
            r, c = row, col
            while 0 <= r < 15 and 0 <= c < 15 and self.board[r][c] == self.current_player:
                count += 1
                r += direction * delta_row
                c += direction * delta_col
        return count >= 5
    def reset_game(self):
        '''
        Resets the game to the initial state.
        '''
        self.board = [[' ' for _ in range(15)] for _ in range(15)]
        self.current_player = 'X'
        self.winner = None
    def __str__(self):
        '''
        Returns a string representation of the game board.
        '''
        board_str = '\n'.join(['|'.join(row) for row in self.board])
        return board_str