'''
Module to handle the board logic for bomb explosions.
'''
class Board:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.board = [['.' for _ in range(cols)] for _ in range(rows)]
    def populate_board(self, board_input):
        # Populate the board with the input characters
        for i in range(self.rows):
            self.board[i] = list(board_input[i])
    def explode_bombs(self):
        # Initialize the result board with the current state of the board
        result = [row[:] for row in self.board]  # Copy the board state
        affected_cells = set()  # Track affected cells
        for i in range(self.rows):
            for j in range(self.cols):
                # Check if the current cell contains a bomb
                if '1' <= self.board[i][j] <= '9':
                    power = int(self.board[i][j])  # Retrieve bomb power
                    # Check all cells in the board
                    for x in range(self.rows):
                        for y in range(self.cols):
                            manhattan_distance = abs(i - x) + abs(j - y)
                            # If within bomb's power range, mark as affected if not a wall
                            if manhattan_distance <= power:
                                if self.board[x][y] != '#':  # Only mark if it's not a wall
                                    affected_cells.add((x, y))  # Mark for emptying
        # Update the result based on affected cells
        for x, y in affected_cells:
            result[x][y] = '.'  # Set affected cells to empty
        return [''.join(row) for row in result]  # Return the final state of the board