'''
BFS logic implementation for finding the shortest path in a grid.
'''
from collections import deque, defaultdict
def find_shortest_time(S, G, grid):
    H = len(grid)
    W = len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([S])
    visited = set()
    visited.add(S)
    teleporters = defaultdict(list)
    # Collect teleporters
    for i in range(H):
        for j in range(W):
            if 'a' <= grid[i][j] <= 'z':
                teleporters[grid[i][j]].append((i, j))
    time = 0
    while queue:
        for _ in range(len(queue)):
            current = queue.popleft()
            if current == G:
                return time
            # Explore all possible moves
            for d in directions:
                ni, nj = current[0] + d[0], current[1] + d[1]
                if 0 <= ni < H and 0 <= nj < W and (ni, nj) not in visited and grid[ni][nj] != '#':
                    visited.add((ni, nj))
                    queue.append((ni, nj))
            # Handle teleporters
            if 'a' <= grid[current[0]][current[1]] <= 'z':
                teleporter_char = grid[current[0]][current[1]]
                for teleporter in teleporters[teleporter_char]:
                    if teleporter not in visited:
                        visited.add(teleporter)
                        queue.append(teleporter)
    return -1  # If G is unreachable