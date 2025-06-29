'''
Contains the game logic for calculating scores and determining the winner.
'''
from typing import List
class Game:
    def __init__(self, H: int, W: int, A: List[List[str]]):
        self.H = H
        self.W = W
        self.A = A
        self.takahashi_points = 0
        self.aoki_points = 0
        self.current_player = 'Takahashi'  # Start with Takahashi
    def play_game(self):
        x, y = 0, 0  # Starting position
        while x < self.H and y < self.W:
            # Update points based on the current square
            if self.A[x][y] == 'B':
                if self.current_player == 'Takahashi':
                    self.takahashi_points += 1
                else:
                    self.aoki_points += 1
            elif self.A[x][y] == 'R':
                if self.current_player == 'Takahashi':
                    self.takahashi_points -= 1
                else:
                    self.aoki_points -= 1
            # Check if the player has reached the bottom-right corner
            if x == self.H - 1 and y == self.W - 1:
                break  # End the game
            # Determine next move
            can_move_down = x + 1 < self.H
            can_move_right = y + 1 < self.W
            # Evaluate potential scores for both moves based on the current player
            down_score = self.evaluate_move(x + 1, y) if can_move_down else None
            right_score = self.evaluate_move(x, y + 1) if can_move_right else None
            # Choose the move that maximizes the current player's score
            if down_score is not None and (right_score is None or down_score >= right_score):
                x += 1  # Move down
            elif right_score is not None:
                y += 1  # Move right
            else:
                break  # No valid moves, end the game
            # Switch player
            self.current_player = 'Aoki' if self.current_player == 'Takahashi' else 'Takahashi'
    def evaluate_move(self, x, y):
        '''
        Evaluate the potential score change for the current player if they move to (x, y).
        '''
        # Check if the move is within bounds
        if x < self.H and y < self.W:
            if self.A[x][y] == 'B':
                return 1  # Increment score for blue
            elif self.A[x][y] == 'R':
                return -1  # Decrement score for red
        return 0  # Return 0 for invalid moves
    def get_winner(self) -> str:
        '''
        Determine the winner based on the final scores.
        '''
        if self.takahashi_points > self.aoki_points:
            return 'Takahashi'
        elif self.aoki_points > self.takahashi_points:
            return 'Aoki'
        else:
            return 'Draw'