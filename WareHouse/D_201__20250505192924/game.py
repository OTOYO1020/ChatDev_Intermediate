'''
Contains the Game class that manages the game logic and state.
'''
class Game:
    def __init__(self, h, w, grid):
        self.h = h
        self.w = w
        self.grid = grid
        self.takahashi_points = 0
        self.aoki_points = 0
    def play_game(self, x, y, turn):
        # Check if the current position is out of bounds
        if x < 0 or x >= self.h or y < 0 or y >= self.w:
            return  # Exit if out of bounds
        # Update points based on the current player's turn
        if self.grid[x][y] == '+':
            if turn == 0:
                self.takahashi_points += 1  # Takahashi scores
            else:
                self.aoki_points += 1  # Aoki scores
        else:
            # Ensure points do not go below zero
            if turn == 0:
                self.takahashi_points = max(0, self.takahashi_points - 1)  # Takahashi loses a point
            else:
                self.aoki_points = max(0, self.aoki_points - 1)  # Aoki loses a point
        # Initialize scores for both paths
        right_score = self.takahashi_points if turn == 0 else self.aoki_points
        down_score = self.takahashi_points if turn == 0 else self.aoki_points
        # Check possible moves (right and down)
        if y + 1 < self.w:  # Move right
            right_score = self.play_game(x, y + 1, 1 - turn)
        if x + 1 < self.h:  # Move down
            down_score = self.play_game(x + 1, y, 1 - turn)
        # Return the maximum score achieved from both paths
        return max(right_score, down_score)
    def get_winner(self):
        # Determine the winner based on the final scores
        if self.takahashi_points > self.aoki_points:
            return "Takahashi"
        elif self.takahashi_points < self.aoki_points:
            return "Aoki"
        else:
            return "Draw"