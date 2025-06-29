'''
Contains the logic for the card game.
'''
import bisect
class CardGame:
    def __init__(self, N, K, P):
        self.N = N
        self.K = K
        self.P = P
        self.table = []
        self.eaten_moves = [-1] * N
        # Create a mapping of card values to their original indices
        self.card_index_map = {value: index for index, value in enumerate(P)}
    def play_game(self):
        for move in range(self.N):
            X = self.P[move]
            self._stack_card(X)
            if len(self.table) == self.K:
                self._mark_eaten_moves(move)
        return self.eaten_moves
    def _stack_card(self, X):
        # Use bisect to find the position to stack the card
        position = bisect.bisect_left(self.table, X)
        # Insert X at the found position or append it if position is at the end
        if position < len(self.table):
            self.table.insert(position, X)  # Insert X at the found position
        else:
            self.table.append(X)  # Append X if it's the largest card
    def _mark_eaten_moves(self, move):
        for i in range(self.K):
            card_value = self.table[-1 - i]  # Get the card value being eaten
            original_index = self.card_index_map[card_value]  # Use the mapping to find the original index
            self.eaten_moves[original_index] = move  # Mark the eaten move for the original index
        del self.table[-self.K:]  # Remove the last K cards from the table