'''
Contains the logic for parsing the maze and calculating the maximum moves between road squares.
'''
from collections import deque
from typing import List, Tuple
def parse_maze(H: int, W: int, S: List[str]) -> List[Tuple[int, int]]:
    '''
    Parses the maze to identify all road squares and their coordinates.
    Parameters:
    H (int): The number of rows in the maze.
    W (int): The number of columns in the maze.
    S (List[str]): The list of strings representing the maze.
    Returns:
    List[Tuple[int, int]]: A list of coordinates of road squares.
    '''
    road_squares = []
    for i in range(H):
        for j in range(W):
            if S[i][j] == '.':
                road_squares.append((i, j))
    return road_squares
def bfs(start: Tuple[int, int], end: Tuple[int, int], maze: List[str], H: int, W: int) -> int:
    '''
    Performs a breadth-first search to find the shortest path between two points in the maze.
    Parameters:
    start (Tuple[int, int]): The starting coordinates.
    end (Tuple[int, int]): The ending coordinates.
    maze (List[str]): The maze representation.
    H (int): The number of rows in the maze.
    W (int): The number of columns in the maze.
    Returns:
    int: The minimum number of moves required to reach the end from the start.
    '''
    if start == end:
        return 0  # Return 0 if start and end are the same
    visited = set()
    queue = deque([(start, 0)])  # (position, distance)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
    visited.add(start)  # Mark the start as visited immediately
    while queue:
        (current_x, current_y), distance = queue.popleft()
        for dx, dy in directions:
            new_x, new_y = current_x + dx, current_y + dy
            if 0 <= new_x < H and 0 <= new_y < W and (new_x, new_y) not in visited:
                if maze[new_x][new_y] == '.':
                    if (new_x, new_y) == end:
                        return distance + 1
                    visited.add((new_x, new_y))  # Mark as visited
                    queue.append(((new_x, new_y), distance + 1))
    return float('inf')  # unreachable
def max_moves(H: int, W: int, S: List[str]) -> int:
    '''
    Calculates the maximum number of moves between any two road squares in the maze.
    Parameters:
    H (int): The number of rows in the maze.
    W (int): The number of columns in the maze.
    S (List[str]): The list of strings representing the maze.
    Returns:
    int: The maximum number of moves found between any two road squares.
    '''
    road_squares = parse_maze(H, W, S)
    if len(road_squares) < 2:
        raise ValueError("There must be at least two road squares in the maze.")
    max_distance = 0
    for i in range(len(road_squares)):
        for j in range(i + 1, len(road_squares)):
            distance = bfs(road_squares[i], road_squares[j], S, H, W)
            if distance != float('inf'):
                max_distance = max(max_distance, distance)
    return max_distance