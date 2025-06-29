'''
This module contains the GomokuGame class which implements the game logic.
'''
class GomokuGame:
    def __init__(self):
        self.board_size = 15
        self.board = [[None for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.current_player = "X"
    def print_board(self):
        '''
        Print the current state of the board.
        '''
        for row in self.board:
            print(" ".join(['.' if cell is None else cell for cell in row]))
    def make_move(self, row, col):
        '''
        Place the current player's mark on the board at the specified row and column.
        If the move is valid, it checks for a winner or a full board.
        '''
        if self.board[row][col] is None:
            self.board[row][col] = self.current_player
            self.print_board()
            if self.check_winner():
                print(f"Player {self.current_player} wins!")
                self.reset_game()
            elif self.is_board_full():
                print("The game is a draw!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
        else:
            print("Invalid move! Try again.")
            # Do not switch players; prompt for a new move
    def check_winner(self):
        '''
        Check if there is a winner on the board.
        '''
        for row in range(self.board_size):
            for col in range(self.board_size):
                if self.board[row][col] is not None:
                    if self.check_direction(row, col, 1, 0) or \
                       self.check_direction(row, col, 0, 1) or \
                       self.check_direction(row, col, 1, 1) or \
                       self.check_direction(row, col, 1, -1):
                        return True
        return False
    def check_direction(self, row, col, delta_row, delta_col):
        '''
        Check if there are five consecutive pieces in a given direction.
        '''
        count = 0
        player = self.board[row][col]
        for _ in range(5):
            # Check if the current position is within bounds
            if 0 <= row < self.board_size and 0 <= col < self.board_size and self.board[row][col] == player:
                count += 1
            else:
                break
            row += delta_row
            col += delta_col
        return count == 5
    def is_board_full(self):
        '''
        Check if the board is full.
        '''
        return all(cell is not None for row in self.board for cell in row)
    def reset_game(self):
        '''
        Reset the game board and current player.
        '''
        self.board = [[None for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.current_player = "X"
        print("Game has been reset. Player X's turn.")
        self.print_board()
    def run(self):
        '''
        Start the game loop.
        '''
        print("Welcome to Gomoku!")
        print("Instructions: Players take turns to place their marks (X or O) on the board.")
        print("Enter your move as two integers (row and column) separated by a space.")
        print("Enter 'exit' to quit the game.")
        self.print_board()
        while True:
            try:
                move = input(f"Player {self.current_player}, enter your move (row and column) or 'exit' to quit: ")
                if move.lower() == 'exit':
                    print("Thanks for playing!")
                    break
                row, col = map(int, move.split())
                if 0 <= row < self.board_size and 0 <= col < self.board_size:
                    self.make_move(row, col)
                else:
                    print("Move out of bounds! Please enter valid coordinates.")
            except ValueError:
                print("Invalid input! Please enter row and column as two integers.")