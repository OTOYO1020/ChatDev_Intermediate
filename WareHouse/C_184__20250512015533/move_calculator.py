'''
Contains the logic for calculating the minimum number of moves from a starting position to a target position.
'''
from collections import deque
class MoveCalculator:
    GRID_MIN = 0
    GRID_MAX = 100
    def min_moves(self, r1: int, c1: int, r2: int, c2: int) -> int:
        if (r1, c1) == (r2, c2):
            return 0
        if self.can_reach_in_one_move(r1, c1, r2, c2):
            return 1
        return self.bfs(r1, c1, r2, c2)
    def can_reach_in_one_move(self, r1: int, c1: int, r2: int, c2: int) -> bool:
        return (r1 + c1 == r2 + c2) or (r1 - c1 == r2 - c2) or (abs(r1 - r2) + abs(c1 - c2) <= 3)
    def bfs(self, r1: int, c1: int, r2: int, c2: int) -> int:
        queue = deque([(r1, c1, 0)])  # (row, column, moves)
        visited = set((r1, c1))
        while queue:
            r, c, moves = queue.popleft()
            # Explore all possible moves within the range of -3 to 3
            for dr in range(-3, 4):
                for dc in range(-3, 4):
                    if abs(dr) + abs(dc) <= 3:  # Movement constraint
                        new_r, new_c = r + dr, c + dc
                        # Check if the new position is within valid grid boundaries
                        if self.GRID_MIN <= new_r <= self.GRID_MAX and self.GRID_MIN <= new_c <= self.GRID_MAX:
                            # Check if the move adheres to the movement rules based on the target position
                            if (new_r + new_c == r2 + c2) and (new_r - new_c == r2 - c2):
                                if (new_r, new_c) == (r2, c2):
                                    return moves + 1
                                if (new_r, new_c) not in visited:
                                    visited.add((new_r, new_c))
                                    queue.append((new_r, new_c, moves + 1))
        return -1  # If no path found