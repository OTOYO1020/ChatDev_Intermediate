'''
Represents the game board for Gomoku.
'''
from cell import Cell
class Board:
    def __init__(self):
        self.size = 15
        self.cells = [[Cell(x, y) for y in range(self.size)] for x in range(self.size)]
        self.current_player = 1
        self.winner = None
    def draw_board(self):
        for row in self.cells:
            print(" | ".join("X" if cell.state == 1 else "O" if cell.state == 2 else "." for cell in row))
            print("-" * (self.size * 4 - 1))
    def handle_click(self, x, y):
        if self.winner:
            print("Game over! Player {} has already won.".format(self.winner))
            return  # Prevent further moves if the game is over
        if not (0 <= x < self.size and 0 <= y < self.size):
            print("Invalid move. Please enter values between 0 and 14.")
            return
        if self.cells[x][y].state == 0:
            self.cells[x][y].state = self.current_player
            if self.check_winner(x, y):
                self.winner = self.current_player
                print(f"Player {self.winner} wins!")
                return  # Prevent further moves after a win
            self.current_player = 2 if self.current_player == 1 else 1
        else:
            print("Cell already occupied. Please choose another cell.")
    def check_winner(self, x, y):
        '''
        Check for a winner by looking for five consecutive pieces in any direction.
        '''
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]  # horizontal, vertical, diagonal /
        for dx, dy in directions:
            count = 1
            # Check in the positive direction
            for step in range(1, 5):
                nx, ny = x + step * dx, y + step * dy
                if 0 <= nx < self.size and 0 <= ny < self.size and self.cells[nx][ny].state == self.current_player:
                    count += 1
                else:
                    break
            # Check in the negative direction
            for step in range(1, 5):
                nx, ny = x - step * dx, y - step * dy
                if 0 <= nx < self.size and 0 <= ny < self.size and self.cells[nx][ny].state == self.current_player:
                    count += 1
                else:
                    break
            if count >= 5:
                return True
        return False
    def play_game(self):
        '''
        Main loop for playing the game, handling player input and game state.
        '''
        while True:
            self.draw_board()
            try:
                x, y = map(int, input(f"Player {self.current_player}, enter your move (row and column): ").split())
                self.handle_click(x, y)
                if self.winner:
                    self.draw_board()  # Show the final board
                    print(f"Player {self.winner} wins!")
                    if input("Do you want to play again? (y/n): ").lower() != 'y':
                        break
                    else:
                        self.reset_game()  # Reset the game for a new round
            except ValueError:
                print("Invalid input. Please enter two integers separated by a space.")
    def reset_game(self):
        '''
        Reset the game board for a new round.
        '''
        self.cells = [[Cell(x, y) for y in range(self.size)] for x in range(self.size)]
        self.current_player = 1
        self.winner = None