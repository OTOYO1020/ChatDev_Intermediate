'''
Contains the game logic for Gomoku, including board management and win checking.
'''
class Board:
    def __init__(self, size=15):
        self.size = size
        self.board = [[' ' for _ in range(size)] for _ in range(size)]
    def place_piece(self, x, y, player_symbol):
        if 0 <= x < self.size and 0 <= y < self.size:  # Check if coordinates are within bounds
            if self.board[x][y] == ' ':
                self.board[x][y] = player_symbol
                return True
        return False
    def check_winner(self, player_symbol):
        # Check horizontal, vertical, and diagonal for a win
        for x in range(self.size):
            for y in range(self.size):
                if self.board[x][y] == player_symbol:
                    if self.check_direction(x, y, 1, 0, player_symbol) or \
                       self.check_direction(x, y, 0, 1, player_symbol) or \
                       self.check_direction(x, y, 1, 1, player_symbol) or \
                       self.check_direction(x, y, 1, -1, player_symbol):
                        return True
        return False
    def check_direction(self, x, y, dx, dy, player_symbol):
        count = 0
        for i in range(5):
            nx, ny = x + i * dx, y + i * dy
            if 0 <= nx < self.size and 0 <= ny < self.size and self.board[nx][ny] == player_symbol:
                count += 1
            else:
                break
        # Check if there are exactly 5 pieces in a row
        if count == 5:
            # Check if the next piece in the same direction is not the same player symbol
            next_x, next_y = x + 5 * dx, y + 5 * dy
            if not (0 <= next_x < self.size and 0 <= next_y < self.size and self.board[next_x][next_y] == player_symbol):
                return True
        return False
    def is_board_full(self):
        for row in self.board:
            if ' ' in row:
                return False
        return True
    def display_board(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * (self.size * 2 - 1))
class GomokuGame:
    def __init__(self):
        self.board = Board()
        self.current_player = 'X'  # X starts first
    def switch_player(self):
        self.current_player = 'X' if self.current_player == 'O' else 'O'
    def start_game(self):
        while True:
            self.board.display_board()
            print(f"Player {self.current_player}, enter your move (row and column): ")
            try:
                x, y = map(int, input().split())
                if self.board.place_piece(x, y, self.current_player):
                    if self.board.check_winner(self.current_player):
                        self.board.display_board()
                        print(f"Player {self.current_player} wins!")
                        return  # End the game
                    elif self.board.is_board_full():
                        self.board.display_board()
                        print("The game is a draw!")
                        return  # End the game
                    else:
                        self.switch_player()
                else:
                    print("Invalid move, try again.")
            except (ValueError, IndexError):
                print("Invalid input, please enter row and column as two integers (0-14).")