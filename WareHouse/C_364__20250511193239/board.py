'''
Contains the Board class for the Gomoku game.
'''
from piece import Piece
class Board:
    def __init__(self):
        self.size = 15  # 15x15 board
        self.board_state = [[None for _ in range(self.size)] for _ in range(self.size)]
        self.current_player = "black"
    def display_board(self):
        for row in self.board_state:
            display_row = []
            for cell in row:
                if cell is None:
                    display_row.append(".")
                else:
                    display_row.append("B" if cell.color == "black" else "W")
            print(" ".join(display_row))
        print()
    def place_piece(self, x, y):
        if 0 <= x < self.size and 0 <= y < self.size:
            if self.board_state[y][x] is None:
                piece = Piece(self.current_player, x, y)
                self.board_state[y][x] = piece
                if self.check_winner(x, y):
                    self.display_board()  # Show final board before announcing winner
                    print(f"{self.current_player.capitalize()} wins!")
                    return False  # End game
                self.current_player = "white" if self.current_player == "black" else "black"
                return True
            else:
                print("Cell is already occupied. Try a different move.")  # Feedback for occupied cell
        return False
    def check_winner(self, x, y):
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]  # Added (-1, 1) for reverse diagonal
        for dx, dy in directions:
            count = 1
            # Check in the positive direction
            count += self.count_in_direction(x, y, dx, dy)
            # Check in the negative direction
            count += self.count_in_direction(x, y, -dx, -dy)
            if count >= 5:
                return True
        return False
    def count_in_direction(self, x, y, dx, dy):
        count = 0
        color = self.board_state[y][x].color
        # Check in the positive direction
        while 0 <= x < self.size and 0 <= y < self.size:
            if self.board_state[y][x] is None or self.board_state[y][x].color != color:
                break
            count += 1
            x += dx
            y += dy
        return count  # Return the count without subtracting one
    def is_full(self):
        return all(cell is not None for row in self.board_state for cell in row)