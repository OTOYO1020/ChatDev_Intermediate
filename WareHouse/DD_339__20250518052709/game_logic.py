'''
Contains the logic for calculating the minimum moves for two players on a grid.
'''
from collections import deque
from typing import List
def minimum_moves(N: int, grid: List[str]) -> int:
    # Find player positions
    player1 = player2 = None
    for i in range(N):
        for j in range(N):
            if grid[i][j] == '1':
                player1 = (i, j)
            elif grid[i][j] == '2':
                player2 = (i, j)
    if not player1 or not player2:
        return -1  # One of the players is missing
    # Check if players are adjacent before starting BFS
    if abs(player1[0] - player2[0]) + abs(player1[1] - player2[1]) == 1:
        return 1  # They can move to each other's position in one move
    def bfs(start1, start2):
        queue = deque([(start1, start2, 0)])  # (player1_position, player2_position, moves)
        visited = set()
        visited.add((start1, start2))
        # Initialize distance matrices for both players
        dist1 = [[-1] * N for _ in range(N)]
        dist2 = [[-1] * N for _ in range(N)]
        dist1[start1[0]][start1[1]] = 0
        dist2[start2[0]][start2[1]] = 0
        while queue:
            (x1, y1), (x2, y2), moves = queue.popleft()
            # Check if both players are at the same position
            if (x1, y1) == (x2, y2):
                return moves
            # Explore all possible moves for both players
            for dx1, dy1 in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx1, ny1 = x1 + dx1, y1 + dy1
                if 0 <= nx1 < N and 0 <= ny1 < N and grid[nx1][ny1] == '.' and dist1[nx1][ny1] == -1:
                    dist1[nx1][ny1] = dist1[x1][y1] + 1
                    new_state = ((nx1, ny1), (x2, y2))
                    if new_state not in visited:
                        visited.add(new_state)
                        queue.append((new_state[0], new_state[1], moves + 1))
            for dx2, dy2 in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx2, ny2 = x2 + dx2, y2 + dy2
                if 0 <= nx2 < N and 0 <= ny2 < N and grid[nx2][ny2] == '.' and dist2[nx2][ny2] == -1:
                    dist2[nx2][ny2] = dist2[x2][y2] + 1
                    new_state = ((x1, y1), (nx2, ny2))
                    if new_state not in visited:
                        visited.add(new_state)
                        queue.append((new_state[0], new_state[1], moves + 1))
        return -1  # If no common cell is reachable
    # Get the result from BFS
    return bfs(player1, player2)