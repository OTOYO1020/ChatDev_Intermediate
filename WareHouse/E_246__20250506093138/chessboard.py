'''
Chessboard class to manage the chessboard and bishop movements.
'''
from collections import deque
class Chessboard:
    def __init__(self, size, rows):
        self.size = size
        self.board = [row.strip() for row in rows]
    def is_valid_move(self, x, y):
        '''Check if the move is within bounds and not occupied by a pawn.'''
        if 0 <= x < self.size and 0 <= y < self.size:
            return self.board[x][y] != 'P'  # Assuming 'P' represents a pawn
        return False
    def bfs(self, start, target):
        '''Perform BFS to find the minimum moves for the bishop.'''
        if not self.is_valid_move(*start) or not self.is_valid_move(*target):
            return -1
        if start == target:  # Check if starting position is the same as target
            return 0
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        queue = deque([(start, 0)])  # (position, moves)
        visited = set()
        visited.add(start)
        while queue:
            (current_x, current_y), moves = queue.popleft()
            for dx, dy in directions:
                x, y = current_x, current_y
                while True:
                    x += dx
                    y += dy
                    if not self.is_valid_move(x, y):
                        break
                    if (x, y) not in visited:
                        visited.add((x, y))
                        queue.append(((x, y), moves + 1))  # Increment moves only when moving to a new position
                        # If we reach the target, we can return immediately
                        if (x, y) == target:
                            return moves + 1
        return -1