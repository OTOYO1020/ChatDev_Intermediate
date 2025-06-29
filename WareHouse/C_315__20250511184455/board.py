'''
Contains the Board and Cell classes for the Gomoku game.
'''
class Cell:
    def __init__(self):
        self.state = None  # None, 'X', or 'O'
class Board:
    def __init__(self):
        self.cells = [[Cell() for _ in range(15)] for _ in range(15)]
        self.current_player = 'X'
        self.game_over = False  # Track if the game is over
    def display(self):
        for row in self.cells:
            print(' '.join(['.' if cell.state is None else cell.state for cell in row]))
        print()
    def make_move(self, row, col):
        '''
        Make a move on the board.
        Parameters:
        row (int): The row index for the move.
        col (int): The column index for the move.
        Returns:
        bool: True if the move was successful, False otherwise.
        '''
        if 0 <= row < 15 and 0 <= col < 15 and self.cells[row][col].state is None:
            self.cells[row][col].state = self.current_player
            return True
        return False
    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'
    def check_winner(self):
        '''
        Check for a winner by examining all cells on the board.
        Returns:
        bool: True if there is a winner, False otherwise.
        '''
        for r in range(15):
            for c in range(15):
                if self.cells[r][c].state is not None:
                    if self.check_direction(r, c):
                        return True
        return False
    def check_direction(self, row, col):
        '''
        Check for a winning condition in all directions from the given cell.
        Parameters:
        row (int): The row index of the cell to check.
        col (int): The column index of the cell to check.
        Returns:
        bool: True if there is a winning condition, False otherwise.
        '''
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
        for dr, dc in directions:
            count = 1  # Start with the current cell
            # Check in the positive direction
            for i in range(1, 5):
                r, c = row + dr * i, col + dc * i
                if 0 <= r < 15 and 0 <= c < 15 and self.cells[r][c].state == self.cells[row][col].state:
                    count += 1
                else:
                    break
            # Check in the negative direction
            for i in range(1, 5):
                r, c = row - dr * i, col - dc * i
                if 0 <= r < 15 and 0 <= c < 15 and self.cells[r][c].state == self.cells[row][col].state:
                    count += 1
                else:
                    break
            if count >= 5:  # Check if we have at least 5 in a row
                return True
        return False