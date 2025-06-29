'''
Contains the logic for calculating the minimum moves for a bishop on a chessboard.
'''
from collections import deque
class BishopGame:
    def __init__(self, N, A_x, A_y, B_x, B_y, S):
        self.N = N
        self.start = (A_x, A_y)
        self.target = (B_x, B_y)
        self.board = S
        self.visited = set()
    def min_moves_bishop(self):
        # Check if the starting position is blocked
        if self.board[self.start[0]][self.start[1]] == 'P':
            return -1
        # Check if the target position is blocked
        if self.board[self.target[0]][self.target[1]] == 'P':
            return -1
        # Check if the starting and target positions are on the same color
        if (self.start[0] + self.start[1]) % 2 != (self.target[0] + self.target[1]) % 2:
            return -1
        # Check if starting position is the same as target position
        if self.start == self.target:
            return 0  # Return 0 moves if already at the target
        # Check if the target can be reached in one move
        if self.target in self.get_possible_moves(self.start[0], self.start[1]):
            return 1  # Return 1 move if directly reachable
        return self.bfs()
    def is_valid_move(self, x, y):
        return 0 <= x < self.N and 0 <= y < self.N and self.board[x][y] == '.'
    def get_possible_moves(self, x, y):
        moves = []
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        for dx, dy in directions:
            nx, ny = x, y
            while True:
                nx += dx
                ny += dy
                if not (0 <= nx < self.N and 0 <= ny < self.N):
                    break  # Stop if out of bounds
                if self.board[nx][ny] == 'P':
                    break  # Stop if we hit a pawn
                if self.board[nx][ny] == '.':
                    moves.append((nx, ny))  # Valid empty square
                else:
                    break  # Stop if we hit any other piece
        return moves
    def bfs(self):
        queue = deque([(self.start[0], self.start[1], 0)])  # (x, y, moves)
        self.visited.add(self.start)
        while queue:
            x, y, moves = queue.popleft()
            for nx, ny in self.get_possible_moves(x, y):
                if (nx, ny) == self.target:
                    return moves + 1
                if (nx, ny) not in self.visited:
                    self.visited.add((nx, ny))
                    queue.append((nx, ny, moves + 1))
        return -1