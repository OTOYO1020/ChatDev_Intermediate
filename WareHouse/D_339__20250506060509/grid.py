'''
Grid class to handle the BFS logic for the grid meeting problem.
'''
from collections import deque
class Grid:
    def __init__(self, size, grid_data):
        self.size = size
        self.grid_data = grid_data
        self.players = self.find_players()
    def find_players(self):
        players = []
        for i in range(self.size):
            for j in range(self.size):
                if self.grid_data[i][j] == 'P':
                    players.append((i, j))
        if len(players) != 2:
            raise ValueError("Error: There must be exactly 2 players in the grid.")  # Raise an exception if not exactly 2 players found
        return players
    def bfs(self):
        (x1, y1), (x2, y2) = self.players
        if (x1, y1) == (x2, y2):
            return 0  # Both players are already at the same cell
        queue = deque([(x1, y1, x2, y2, 0)])  # Queue for both players
        visited = set()  # Visited states for both players
        visited.add((x1, y1, x2, y2))
        while queue:
            x1, y1, x2, y2, moves = queue.popleft()
            # Check if both players are at the same cell
            if (x1, y1) == (x2, y2):
                return moves
            # Possible moves for both players
            for dx1, dy1 in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx1, ny1 = x1 + dx1, y1 + dy1
                if 0 <= nx1 < self.size and 0 <= ny1 < self.size and self.grid_data[nx1][ny1] == '.':
                    for dx2, dy2 in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nx2, ny2 = x2 + dx2, y2 + dy2
                        if 0 <= nx2 < self.size and 0 <= ny2 < self.size and self.grid_data[nx2][ny2] == '.':
                            if (nx1, ny1, nx2, ny2) not in visited:
                                visited.add((nx1, ny1, nx2, ny2))
                                queue.append((nx1, ny1, nx2, ny2, moves + 1))
            # Check if one player can move while the other stays
            for dx2, dy2 in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx2, ny2 = x2 + dx2, y2 + dy2
                if 0 <= nx2 < self.size and 0 <= ny2 < self.size and self.grid_data[nx2][ny2] == '.':
                    if (x1, y1, nx2, ny2) not in visited:
                        visited.add((x1, y1, nx2, ny2))
                        queue.append((x1, y1, nx2, ny2, moves + 1))
        return -1  # If no meeting point is found