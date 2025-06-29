'''
Contains the logic for the Gomoku game, including board management and win checking.
'''
class GomokuGame:
    def __init__(self):
        self.board = [[None for _ in range(15)] for _ in range(15)]
        self.current_player = "X"
        self.winner = None
    def make_move(self, x, y):
        if self.winner is not None:
            print("Game over. No more moves can be made.")
            return False  # Invalid move
        if self.is_board_full():
            print("Game over. The board is full.")
            return False  # Invalid move
        if x < 0 or x >= 15 or y < 0 or y >= 15:
            print("Invalid move. Please choose row and column numbers between 0 and 14.")
            return False  # Invalid move
        if self.board[x][y] is None:
            self.board[x][y] = self.current_player
            if self.check_winner():
                self.winner = self.current_player
            self.current_player = "O" if self.current_player == "X" else "X"
            return True  # Move was successful
        else:
            return False  # Invalid move
    def check_winner(self):
        for x in range(15):
            for y in range(15):
                if self.board[x][y] is not None:
                    if self.check_line(x, y):
                        return True
        return False
    def check_line(self, x, y):
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
        for dx, dy in directions:
            count = 1  # Start with the current piece
            # Check in the positive direction
            for step in range(1, 5):
                nx, ny = x + step * dx, y + step * dy
                if 0 <= nx < 15 and 0 <= ny < 15 and self.board[nx][ny] == self.board[x][y]:
                    count += 1
                else:
                    break
            # Check in the negative direction
            for step in range(1, 5):
                nx, ny = x - step * dx, y - step * dy
                if 0 <= nx < 15 and 0 <= ny < 15 and self.board[nx][ny] == self.board[x][y]:
                    count += 1
                else:
                    break
            # Ensure exactly five in a row
            if count == 5:
                # Check if the piece before and after the five in a row is different
                before = (x - dx, y - dy)
                after = (x + 5 * dx, y + 5 * dy)
                if (0 <= before[0] < 15 and 0 <= before[1] < 15 and self.board[before[0]][before[1]] == self.board[x][y]) or \
                   (0 <= after[0] < 15 and 0 <= after[1] < 15 and self.board[after[0]][after[1]] == self.board[x][y]):
                    continue  # More than five in a row
                return True
        return False
    def reset_game(self):
        self.board = [[None for _ in range(15)] for _ in range(15)]
        self.current_player = "X"
        self.winner = None
    def print_board(self):
        for row in self.board:
            print(' '.join(['.' if cell is None else cell for cell in row]))
    def is_board_full(self):
        return all(cell is not None for row in self.board for cell in row)