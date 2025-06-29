'''
Contains the GomokuGame class which manages the game logic.
'''
from cell import Cell  # Import the Cell class
class GomokuGame:
    def __init__(self):
        self.board_size = 15
        self.board = [[Cell(row, col) for col in range(self.board_size)] for row in range(self.board_size)]
        self.current_player = "X"
    def draw_board(self):
        # Draw the current state of the board
        for row in self.board:
            print(" | ".join(cell.value if cell.value else "." for cell in row))
            print("-" * (self.board_size * 4 - 1))
    def make_move(self, row, col):
        # Check if the move is within the bounds of the board
        if row < 0 or row >= self.board_size or col < 0 or col >= self.board_size:
            print("Invalid move. Please enter row and column within the board size.")
            return False  # Return False to indicate the move was invalid
        # Attempt to make a move at the specified row and column
        if self.board[row][col].value == "":
            self.board[row][col].value = self.current_player
            self.draw_board()
            if self.check_win(row, col):
                print(f"Player {self.current_player} wins!")
                return True  # Indicate that the game has ended
            self.current_player = "O" if self.current_player == "X" else "X"
            return True  # Indicate that the move was valid and the game continues
        else:
            print("Cell already occupied. Try again.")
            return False  # Return False to indicate the move was invalid
    def check_win(self, row, col):
        # Check all directions for a win
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]  # (down, right, diagonal down-right, diagonal down-left)
        for dr, dc in directions:
            count = 1
            # Check in the positive direction
            for d in [1, -1]:
                r, c = row, col
                while 0 <= r + d * dr < self.board_size and 0 <= c + d * dc < self.board_size:
                    r += d * dr
                    c += d * dc
                    if self.board[r][c].value == self.current_player:
                        count += 1
                    else:
                        break
            if count >= 5:
                return True
        return False
    def run(self):
        # Start the game loop
        self.draw_board()
        moves_made = 0  # Track the number of moves made
        while True:
            try:
                row = int(input(f"Player {self.current_player}, enter row (0-{self.board_size-1}): "))
                col = int(input(f"Player {self.current_player}, enter column (0-{self.board_size-1}): "))
                while not self.make_move(row, col):  # Continue prompting until a valid move is made
                    row = int(input(f"Player {self.current_player}, enter row (0-{self.board_size-1}): "))
                    col = int(input(f"Player {self.current_player}, enter column (0-{self.board_size-1}): "))
                moves_made += 1  # Increment moves made
                if moves_made == self.board_size * self.board_size:
                    print("The game is a draw!")
                    break  # End the game if the board is full
            except (ValueError, IndexError):
                print("Invalid input. Please enter valid row and column numbers.")