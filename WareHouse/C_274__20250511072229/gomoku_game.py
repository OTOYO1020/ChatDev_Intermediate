'''
This module contains the GomokuGame class which handles the game logic.
'''
class GomokuGame:
    def __init__(self):
        '''
        Initializes a new game of Gomoku with an empty board and sets the current player to 'X'.
        '''
        self.board = [[' ' for _ in range(15)] for _ in range(15)]
        self.current_player = 'X'
        self.winner = None
    def make_move(self, row, col):
        '''
        Places the current player's mark on the board at the specified row and column if the move is valid.
        Parameters:
        row (int): The row index for the move.
        col (int): The column index for the move.
        '''
        if self.winner is not None:
            print("Game over! Player {} has already won.".format(self.winner))
            return
        if 0 <= row < 15 and 0 <= col < 15:  # Check for valid indices
            if self.board[row][col] == ' ':
                self.board[row][col] = self.current_player
                if self.check_winner(row, col):
                    self.winner = self.current_player
                elif self.is_board_full():  # Check for draw condition
                    print("The game is a draw!")
                    self.winner = 'Draw'
                self.current_player = 'O' if self.current_player == 'X' else 'X'
            else:
                print("Invalid move. The cell is already occupied.")
        else:
            print("Invalid move. Please enter values between 0 and 14.")
    def check_winner(self, row, col):
        '''
        Checks if the current player has won the game after making a move at the specified row and column.
        Parameters:
        row (int): The row index of the last move.
        col (int): The column index of the last move.
        Returns:
        bool: True if the current player has won, False otherwise.
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
    def is_board_full(self):
        '''
        Checks if the board is full.
        Returns:
        bool: True if the board is full, False otherwise.
        '''
        return all(cell != ' ' for row in self.board for cell in row)
    def reset_game(self):
        '''
        Resets the game to the initial state, clearing the board and setting the current player to 'X'.
        '''
        self.board = [[' ' for _ in range(15)] for _ in range(15)]
        self.current_player = 'X'
        self.winner = None