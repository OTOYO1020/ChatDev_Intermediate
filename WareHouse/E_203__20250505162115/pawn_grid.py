'''
Module to manage the pawn grid and check reachable positions.
'''
class PawnGrid:
    def __init__(self, N, black_pawns):
        self.N = N
        self.black_pawns = set(black_pawns)
    def is_reachable(self, y):
        # A white pawn can reach (2N, Y) if there are no black pawns in the same column
        # or in the diagonal paths leading to (2N, y)
        if (2 * self.N, y) in self.black_pawns:  # Check the column directly
            return False
        # Check diagonal paths
        for dy in range(1, self.N + 1):  # Check up to N steps diagonally
            if (2 * self.N - dy, y - dy) in self.black_pawns and 0 <= y - dy <= 2 * self.N:
                return False  # Left diagonal
            if (2 * self.N - dy, y + dy) in self.black_pawns and 0 <= y + dy <= 2 * self.N:
                return False  # Right diagonal
        return True