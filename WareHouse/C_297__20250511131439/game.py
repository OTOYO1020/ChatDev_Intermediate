'''
Contains the logic for the Gomoku game.
'''
class GomokuGame:
    def __init__(self):
        self.board_size = 15
        self.board = [[' ' for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.current_player = 'X'
        self.game_over = False
    def make_move(self, x, y):
        # Check if the move is within bounds and the cell is empty
        if 0 <= x < self.board_size and 0 <= y < self.board_size:
            if self.board[x][y] == ' ' and not self.game_over:
                self.board[x][y] = self.current_player
                if self.check_win(x, y):  # Pass the last move coordinates
                    self.game_over = True
                    return True  # Return True to indicate a successful move
                # Switch player only if the game is not over
                self.current_player = 'O' if self.current_player == 'X' else 'X'
                return True
        return False
    def check_win(self, x, y):
        # Check all directions from the last move
        return (self.check_direction(x, y, 1, 0) +  # Horizontal
                self.check_direction(x, y, 0, 1) +  # Vertical
                self.check_direction(x, y, 1, 1) +  # Diagonal \
                self.check_direction(x, y, 1, -1)) >= 5  # Diagonal /
    def check_direction(self, x, y, dx, dy):
        count = 1  # Start with the current piece
        # Check in the positive direction
        for i in range(1, 5):
            nx, ny = x + i * dx, y + i * dy
            if 0 <= nx < self.board_size and 0 <= ny < self.board_size and self.board[nx][ny] == self.board[x][y]:
                count += 1
            else:
                break
        # Check in the negative direction
        for i in range(1, 5):
            nx, ny = x - i * dx, y - i * dy
            if 0 <= nx < self.board_size and 0 <= ny < self.board_size and self.board[nx][ny] == self.board[x][y]:
                count += 1
            else:
                break
        return count >= 5
    def reset_game(self):
        # Reset the game to the initial state
        self.board = [[' ' for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.current_player = 'X'
        self.game_over = False
    def __str__(self):
        board_str = '\n'.join(['|'.join(row) for row in self.board])
        return board_str.replace(' ', '.')