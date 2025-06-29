'''
Class to represent the game board and manage game state.
'''
from player import Player
class Board:
    def __init__(self, game):
        self.game = game
        self.size = 15
        self.board = [[0] * self.size for _ in range(self.size)]
        self.current_player = Player('X')  # Start with player X
        self.player1 = Player('X')
        self.player2 = Player('O')
        self.is_game_over = False  # Initialize game over flag
    def draw_board(self):
        print("Current board:")
        for row in self.board:
            print(' '.join(['.' if cell == 0 else cell for cell in row]))
    def make_move(self, x, y):
        if self.is_game_over:
            print("Game is over! Please reset to play again.")
            return
        if 0 <= x < self.size and 0 <= y < self.size and self.board[y][x] == 0:
            self.board[y][x] = self.current_player.symbol
            self.draw_board()
            if self.check_winner():
                print(f"Player {self.current_player.symbol} wins!")
                self.is_game_over = True  # Set game over flag
                return  # Prevent further moves after winning
            # Switch players based on symbol
            self.current_player = self.player2 if self.current_player.symbol == 'X' else self.player1
        else:
            print("Invalid move! Try again.")
    def check_winner(self):
        # Check horizontal, vertical, and diagonal for a winner
        for y in range(self.size):
            for x in range(self.size):
                if self.board[y][x] != 0:
                    if (self.check_direction(x, y, 1, 0) or  # Horizontal
                        self.check_direction(x, y, 0, 1) or  # Vertical
                        self.check_direction(x, y, 1, 1) or  # Diagonal \
                        self.check_direction(x, y, 1, -1)):  # Diagonal /
                        return True
        return False
    def check_direction(self, x, y, dx, dy):
        count = 0
        symbol = self.board[y][x]
        for i in range(5):
            nx, ny = x + i * dx, y + i * dy
            if 0 <= nx < self.size and 0 <= ny < self.size and self.board[ny][nx] == symbol:
                count += 1
            else:
                break
        return count == 5
    def reset_game(self):
        self.board = [[0] * self.size for _ in range(self.size)]
        self.current_player = Player('X')  # Start with player X
        self.is_game_over = False  # Reset game over flag
        self.draw_board()