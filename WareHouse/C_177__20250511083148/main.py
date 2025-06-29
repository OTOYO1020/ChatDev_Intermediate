'''
This file implements a basic Gomoku game using standard input and output.
'''
class GomokuGame:
    def __init__(self):
        self.board_size = 15
        self.board = [[0] * self.board_size for _ in range(self.board_size)]
        self.current_player = 1
        self.winner = None
    def make_move(self, x, y):
        '''
        Places a move on the board for the current player at the specified coordinates.
        Parameters:
            x (int): The row index for the move.
            y (int): The column index for the move.
        '''
        if self.winner is not None:
            print(f"Game over! Player {self.winner} has already won.")
            return  # Prevent further moves if the game is over
        if self.board[x][y] != 0:
            print("Invalid move. This cell is already occupied. Please choose another cell.")
            return  # Prevent placing a piece on an occupied cell
        self.board[x][y] = self.current_player
        if self.check_winner():
            self.winner = self.current_player
        self.current_player = 3 - self.current_player  # Switch between player 1 and 2
    def check_winner(self):
        '''
        Checks the board for a winner by examining all possible directions.
        Returns:
            bool: True if there is a winner, otherwise False.
        '''
        for x in range(self.board_size):
            for y in range(self.board_size):
                if self.board[x][y] != 0:
                    if (self.check_direction(x, y, 1, 0) or  # Horizontal
                        self.check_direction(x, y, 0, 1) or  # Vertical
                        self.check_direction(x, y, 1, 1) or  # Diagonal \
                        self.check_direction(x, y, 1, -1)):  # Diagonal /
                        return True
        return False
    def check_direction(self, x, y, dx, dy):
        '''
        Checks for exactly five consecutive pieces in a specified direction.
        Parameters:
            x (int): The starting row index.
            y (int): The starting column index.
            dx (int): The change in row index for each step.
            dy (int): The change in column index for each step.
        Returns:
            bool: True if there are exactly five consecutive pieces, otherwise False.
        '''
        count = 0
        # Count in the positive direction
        for i in range(5):  
            nx, ny = x + i * dx, y + i * dy
            if 0 <= nx < self.board_size and 0 <= ny < self.board_size and self.board[nx][ny] == self.board[x][y]:
                count += 1
            else:
                break
        # Count in the negative direction
        for i in range(1, 5):  
            nx, ny = x - i * dx, y - i * dy
            if 0 <= nx < self.board_size and 0 <= ny < self.board_size and self.board[nx][ny] == self.board[x][y]:
                count += 1
            else:
                break
        return count == 5  # Check for exactly 5 in a row
    def reset_game(self):
        '''
        Resets the game board to the initial state.
        '''
        self.board = [[0] * self.board_size for _ in range(self.board_size)]
        self.current_player = 1
        self.winner = None
    def print_board(self):
        '''
        Prints the current state of the game board.
        '''
        for row in self.board:
            print(' '.join(['X' if cell == 1 else 'O' if cell == 2 else '.' for cell in row]))
def main():
    '''
    Main function to run the Gomoku game.
    '''
    game = GomokuGame()
    while game.winner is None:
        game.print_board()
        valid_move = False  # Flag to check if the move is valid
        while not valid_move:
            try:
                x, y = map(int, input(f"Player {game.current_player}, enter your move (row and column): ").split())
                if 0 <= x < game.board_size and 0 <= y < game.board_size:
                    game.make_move(x, y)
                    valid_move = True  # Move is valid, exit the loop
                else:
                    print("Invalid move. Please enter values within the board size.")
            except ValueError:
                print("Invalid input. Please enter two integers separated by a space.")
    game.print_board()
    print(f"Player {game.winner} wins!")
if __name__ == "__main__":
    main()