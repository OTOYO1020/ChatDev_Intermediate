'''
Contains the Game class that handles the game logic for the stone removal game.
'''
class Game:
    def __init__(self, n, moves):
        self.current_stones = n
        self.moves = sorted(moves, reverse=True)  # Sort moves in descending order
        self.takahashi_stones = 0
        self.aoki_stones = 0
    def play_game(self):
        while self.current_stones > 0:
            # Takahashi's turn
            takahashi_move = self.get_max_move(self.current_stones)
            if takahashi_move is not None:
                self.takahashi_stones += takahashi_move
                self.current_stones -= takahashi_move
            # Aoki's turn
            if self.current_stones > 0:
                aoki_move = self.get_max_move(self.current_stones)
                if aoki_move is not None:
                    self.aoki_stones += aoki_move
                    self.current_stones -= aoki_move
        return self.takahashi_stones
    def get_max_move(self, current_stones):
        # Find the largest move that can be made with the current stones
        for move in self.moves:
            if move <= current_stones:
                return move  # Return the move
        return None  # No valid moves found