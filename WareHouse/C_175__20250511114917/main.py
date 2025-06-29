'''
This file contains the implementation of a basic Gomoku game using standard input and output.
'''
class GomokuGame:
    def __init__(self):
        self.board_size = 15
        self.board = [[' ' for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.current_player = 'X'  # Player 1 is 'X', Player 2 is 'O'
    def draw_board(self):
        print("  " + " ".join(str(i) for i in range(self.board_size)))
        for i in range(self.board_size):
            print(i, end=" ")
            for j in range(self.board_size):
                print(self.board[i][j], end=" ")
            print()
    def handle_turn(self):
        while True:
            try:
                row = int(input(f"Player {self.current_player}, enter your move row (0-{self.board_size-1}): "))
                col = int(input(f"Player {self.current_player}, enter your move column (0-{self.board_size-1}): "))
                if 0 <= row < self.board_size and 0 <= col < self.board_size:  # Check bounds
                    if self.board[row][col] == ' ':
                        self.board[row][col] = self.current_player
                        return row, col  # Return the last move made
                    else:
                        print("This position is already taken. Try again.")
                else:
                    print("Invalid input. Please enter numbers within the board range.")
            except ValueError:
                print("Invalid input. Please enter valid integers.")
    def check_winner(self, row, col):
        # Check for a winner in all directions: horizontal, vertical, and two diagonals
        for direction in [(1, 0), (0, 1), (1, 1), (1, -1)]:
            count = 1  # Start with the current move
            # Check in both positive and negative directions
            for d in [1, -1]:
                r, c = row, col
                while 0 <= r + d * direction[0] < self.board_size and 0 <= c + d * direction[1] < self.board_size:
                    r += d * direction[0]
                    c += d * direction[1]
                    if self.board[r][c] == self.current_player:
                        count += 1
                    else:
                        break
            # If five in a row is found, return True
            if count >= 5:
                return True
        return False
    def is_board_full(self):
        return all(cell != ' ' for row in self.board for cell in row)
    def reset_game(self):
        self.board = [[' ' for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.current_player = 'X'
    def handle_game_continuation(self):
        if input("Play again? (y/n): ").lower() != 'y':
            print("Thank you for playing!")
            return False  # Indicate that the game should not continue
        self.reset_game()
        return True  # Indicate that the game should continue
    def play_game(self):
        game_ongoing = True  # Flag to track if the game is ongoing
        while game_ongoing:
            self.draw_board()
            row, col = self.handle_turn()
            if self.check_winner(row, col):
                self.draw_board()
                print(f"Player {self.current_player} wins!")
                game_ongoing = self.handle_game_continuation()  # Update based on user input
            elif self.is_board_full():  # Check for a full board
                self.draw_board()
                print("The game is a draw!")
                game_ongoing = self.handle_game_continuation()  # Update based on user input
            self.current_player = 'O' if self.current_player == 'X' else 'X'
if __name__ == "__main__":
    game = GomokuGame()
    game.play_game()