'''
This module contains the implementation of the Gomoku game logic.
'''
class Gomoku:
    def __init__(self):
        self.board = self.initialize_board()
        self.current_player = 'X'  # Player X starts first
    def initialize_board(self):
        '''
        Initializes a 15x15 board for the Gomoku game.
        '''
        return [[' ' for _ in range(15)] for _ in range(15)]
    def display_board(self):
        '''
        Displays the current state of the board.
        '''
        for row in self.board:
            print('|'.join(row))
            print('-' * 29)
    def make_move(self, row, col):
        '''
        Places the current player's mark on the board and checks for a win.
        '''
        if 0 <= row < 15 and 0 <= col < 15:  # Check if the move is within bounds
            if self.board[row][col] == ' ':
                self.board[row][col] = self.current_player
                if self.check_win(row, col):
                    self.display_board()
                    print(f"Player {self.current_player} wins!")
                    return True  # Game over
                self.current_player = 'O' if self.current_player == 'X' else 'X'
                return False  # Game continues
            else:
                print("Invalid move. Try again.")
        else:
            print("Move out of bounds. Please enter numbers between 0 and 14.")
        return False  # Game continues
    def check_win(self, row, col):
        '''
        Checks for win conditions in all directions from the last move.
        '''
        return (self.check_direction(row, col, 1, 0) or  # Horizontal
                self.check_direction(row, col, 0, 1) or  # Vertical
                self.check_direction(row, col, 1, 1) or  # Diagonal \
                self.check_direction(row, col, 1, -1))   # Diagonal /
    def check_direction(self, row, col, delta_row, delta_col):
        '''
        Checks for five in a row in a specified direction.
        '''
        count = 1  # Count the current piece
        for direction in [1, -1]:  # Check both directions
            for step in range(1, 5):
                r = row + direction * step * delta_row
                c = col + direction * step * delta_col
                if 0 <= r < 15 and 0 <= c < 15 and self.board[r][c] == self.current_player:
                    count += 1
                else:
                    break
        return count >= 5  # Win if there are 5 in a row
    def start_game(self):
        '''
        Starts the Gomoku game and handles user interaction.
        '''
        while True:
            self.display_board()
            user_input = input(f"Player {self.current_player}, enter your move as 'row col' (0-14 0-14) or 'exit' to quit: ")
            if user_input.lower() == 'exit':
                print("Thanks for playing!")
                break  # Exit the game
            try:
                row, col = map(int, user_input.split())
                if self.make_move(row, col):
                    break  # Exit the loop if there's a winner
            except (ValueError, IndexError):
                print("Invalid input. Please enter two numbers between 0 and 14 separated by a space or 'exit' to quit.")