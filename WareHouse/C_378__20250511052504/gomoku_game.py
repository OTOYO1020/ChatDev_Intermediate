'''
Contains the logic for the Gomoku game.
'''
class GomokuGame:
    def __init__(self):
        self.board = [[' ' for _ in range(15)] for _ in range(15)]
        self.current_player = 'X'
        self.game_over = False
    def make_move(self, row, col):
        if self.board[row][col] != ' ' or self.game_over:
            print("Invalid move. The cell is already occupied or the game is over.")
            return  # Early return to prevent further processing
        self.board[row][col] = self.current_player
        if self.check_win(row, col):
            self.game_over = True
        else:
            self.current_player = 'O' if self.current_player == 'X' else 'X'
    def check_win(self, row, col):
        '''
        Check if the current player has won the game by forming a line of five pieces.
        '''
        return (self.check_line(row, col, 1, 0) or  # Horizontal
                self.check_line(row, col, 0, 1) or  # Vertical
                self.check_line(row, col, 1, 1) or  # Diagonal \
                self.check_line(row, col, 1, -1))   # Diagonal /
    def check_line(self, row, col, delta_row, delta_col):
        '''
        Check if there are five pieces in a line in the specified direction.
        '''
        count = 1  # Start with the current piece
        for direction in [1, -1]:  # Check in both directions
            for step in range(1, 5):  # Check the next 4 pieces
                r = row + direction * step * delta_row
                c = col + direction * step * delta_col
                if 0 <= r < 15 and 0 <= c < 15 and self.board[r][c] == self.current_player:
                    count += 1
                else:
                    break
        return count >= 5
    def reset_game(self):
        '''
        Reset the game to the initial state.
        '''
        self.board = [[' ' for _ in range(15)] for _ in range(15)]
        self.current_player = 'X'
        self.game_over = False
    def __str__(self):
        board_str = '\n'.join(['|'.join(row) for row in self.board])
        return board_str.replace(' ', '.')