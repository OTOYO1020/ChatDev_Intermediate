'''
Contains the CardGame class that manages the game logic.
'''
class CardGame:
    def __init__(self, A, B):
        self.A = A
        self.B = B
    def can_remove_pair(self):
        '''
        Check if there exists a removable pair of cards.
        A removable pair is defined as a pair (A[i], B[i]) such that A[i] == B[j] or B[i] == A[j].
        Returns a list of indices of removable pairs.
        '''
        removable_pairs = []
        for i in range(len(self.A)):
            for j in range(len(self.B)):
                if i != j and (self.A[i] == self.B[j] or self.B[i] == self.A[j]):
                    removable_pairs.append((i, j))
        return removable_pairs
    def play_game(self, turn):
        '''
        Simulate the game recursively.
        If no moves are available, return the winner based on the current turn.
        If moves are available, iterate through the possible pairs of cards,
        remove them, and recursively call play_game for the next turn.
        '''
        # Get removable pairs
        removable_pairs = self.can_remove_pair()
        # Check if there are no moves available
        if not removable_pairs:
            return "Takahashi" if turn == 1 else "Aoki"
        # Iterate through the removable pairs
        for i, j in removable_pairs:
            # Create new lists without the removed cards
            new_A = [self.A[k] for k in range(len(self.A)) if k != i]
            new_B = [self.B[k] for k in range(len(self.B)) if k != j]
            game = CardGame(new_A, new_B)
            winner = game.play_game(1 - turn)  # Switch turn
            if winner == "Aoki":
                return "Takahashi"  # If Aoki would win, Takahashi wins
        return "Aoki"  # If all moves lead to Takahashi winning, Aoki wins