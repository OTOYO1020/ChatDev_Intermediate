'''
This module contains the logic for the Gomoku game.
'''
class GomokuGame:
    def __init__(self):
        self.board = [[None for _ in range(15)] for _ in range(15)]
        self.current_player = "X"
        self.winner = None
    def make_move(self, x, y):
        if self.winner is not None:
            return "Game over. No more moves allowed."  # Prevent moves after game over
        if 0 <= x < 15 and 0 <= y < 15:
            if self.board[x][y] is None:
                self.board[x][y] = self.current_player
                if self.check_winner():  # Check for winner only after a successful move
                    self.winner = self.current_player
                elif self.check_draw():  # Check for draw
                    self.winner = "Draw"  # Set winner to "Draw" to indicate the game is over
                else:
                    self.current_player = "O" if self.current_player == "X" else "X"
                return True  # Move was successful
            else:
                return False  # Move was invalid (cell already occupied)
        return False  # Move was invalid (out of bounds)
    def check_winner(self):
        # Check horizontal, vertical, and diagonal for a win
        for x in range(15):
            for y in range(15):
                if self.board[x][y] is not None:
                    if self.check_direction(x, y, 1, 0) or \
                       self.check_direction(x, y, 0, 1) or \
                       self.check_direction(x, y, 1, 1) or \
                       self.check_direction(x, y, 1, -1):
                        return True
        return False
    def check_direction(self, x, y, dx, dy):
        count = 0
        for i in range(5):  # Check for 5 in a row
            nx, ny = x + i * dx, y + i * dy
            if 0 <= nx < 15 and 0 <= ny < 15 and self.board[nx][ny] == self.board[x][y]:
                count += 1
            else:
                break
        return count == 5  # Ensure exactly 5 in a row
    def check_draw(self):
        # Check if the board is full and there is no winner
        if all(cell is not None for row in self.board for cell in row) and self.winner is None:
            return True
        return False
    def reset_game(self):
        self.board = [[None for _ in range(15)] for _ in range(15)]
        self.current_player = "X"
        self.winner = None
    def print_board(self):
        for row in self.board:
            print(' '.join(['.' if cell is None else cell for cell in row]))
    def run(self):
        while self.winner is None:
            self.print_board()
            print(f"Current Player: {self.current_player}")
            try:
                x, y = map(int, input("Enter your move (row and column): ").split())
                result = self.make_move(x, y)
                if result is False:
                    print("Invalid move. Try again.")
                elif result == "Game over. No more moves allowed.":
                    print(result)
            except ValueError:
                print("Invalid input. Please enter two numbers separated by a space.")
        self.print_board()
        if self.winner == "Draw":
            print("It's a draw!")
        else:
            print(f"Player {self.winner} wins!")