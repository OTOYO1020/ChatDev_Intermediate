'''
This module contains the GomokuGame class, which handles the game logic for Gomoku.
'''
class GomokuGame:
    def __init__(self):
        self.board = [[None for _ in range(15)] for _ in range(15)]
        self.current_player = "X"
        self.game_over = False  # Track if the game is over
    def make_move(self, row, col):
        '''
        Attempts to make a move for the current player at the specified row and column.
        Returns a message indicating the result of the move.
        '''
        if self.game_over:
            return "Game is already over!"  # Prevent moves if the game is over
        if row < 0 or row >= 15 or col < 0 or col >= 15:
            return "Invalid move! Out of bounds."
        if self.board[row][col] is not None:
            return "Invalid move! Cell already occupied."
        self.board[row][col] = self.current_player
        if self.check_win(row, col):
            self.game_over = True  # Set game over state
            return f"Player {self.current_player} wins!"
        # Switch players
        self.current_player = "O" if self.current_player == "X" else "X"
        # Return a message indicating the move was successful
        return "Move successful."
    def check_win(self, row, col):
        '''
        Checks if the current player has won the game by looking for five in a row
        in horizontal, vertical, and diagonal directions.
        '''
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
        for dr, dc in directions:
            count = 1
            for d in [1, -1]:
                r, c = row, col
                while 0 <= r + d * dr < 15 and 0 <= c + d * dc < 15 and self.board[r + d * dr][c + d * dc] == self.current_player:
                    count += 1
                    r += d * dr
                    c += d * dc
            if count >= 5:
                return True
        return False
    def reset_game(self):
        '''
        Resets the game board and current player to start a new game.
        '''
        self.board = [[None for _ in range(15)] for _ in range(15)]
        self.current_player = "X"
        self.game_over = False  # Reset game over state
    def print_board(self):
        '''
        Prints the current state of the game board to the console.
        '''
        for row in self.board:
            print(" ".join(['.' if cell is None else cell for cell in row]))