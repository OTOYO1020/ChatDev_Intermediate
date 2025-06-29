'''
Contains the game logic and rules for the Gomoku game.
'''
class GameLogic:
    def __init__(self, board_size):
        '''
        Initializes the game logic with a specified board size.
        Parameters:
        board_size (int): The size of the board (number of rows and columns).
        '''
        self.board_size = board_size
        self.board = [['' for _ in range(board_size)] for _ in range(board_size)]
    def place_stone(self, x, y, player):
        '''
        Places a stone on the board at the specified coordinates if the move is valid.
        Parameters:
        x (int): The row index where the stone is to be placed.
        y (int): The column index where the stone is to be placed.
        player (str): The player making the move ('black' or 'white').
        Returns:
        bool: True if the stone was placed successfully, False otherwise.
        '''
        if 0 <= x < self.board_size and 0 <= y < self.board_size:  # Check bounds
            if self.board[x][y] == '':
                self.board[x][y] = player
                return True
        return False
    def is_winner(self, player):
        '''
        Checks if the specified player has won the game.
        Parameters:
        player (str): The player to check for a win ('black' or 'white').
        Returns:
        bool: True if the player has won, False otherwise.
        '''
        for x in range(self.board_size):
            for y in range(self.board_size):
                if self.board[x][y] == player:
                    if self.check_direction(x, y, player):
                        return True
        return False
    def check_direction(self, x, y, player):
        '''
        Checks all possible winning directions from a given position.
        Parameters:
        x (int): The row index of the starting position.
        y (int): The column index of the starting position.
        player (str): The player to check for a win ('black' or 'white').
        Returns:
        bool: True if there is a winning line, False otherwise.
        '''
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
        for dx, dy in directions:
            count = 1
            # Check in the positive direction
            for step in range(1, 5):
                nx, ny = x + dx * step, y + dy * step
                if 0 <= nx < self.board_size and 0 <= ny < self.board_size and self.board[nx][ny] == player:
                    count += 1
                else:
                    break
            # Check in the negative direction
            for step in range(1, 5):
                nx, ny = x - dx * step, y - dy * step
                if 0 <= nx < self.board_size and 0 <= ny < self.board_size and self.board[nx][ny] == player:
                    count += 1
                else:
                    break
            if count >= 5:
                return True
        return False
    def is_draw(self):
        '''
        Checks if the game is a draw (i.e., there are no valid moves left).
        Returns:
        bool: True if the game is a draw, False otherwise.
        '''
        # Check if the board is full
        for row in self.board:
            if '' in row:
                return False
        # If the board is full, check for winners
        return not self.is_winner('black') and not self.is_winner('white')
    def reset(self):
        '''
        Resets the game board to its initial empty state.
        '''
        self.board = [['' for _ in range(self.board_size)] for _ in range(self.board_size)]