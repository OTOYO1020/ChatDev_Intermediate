'''
Grid processing logic for the grid navigation program.
'''
from typing import List, Tuple
from collections import deque
class GridProcessor:
    '''
    Class to process the grid and perform BFS to find the goal.
    '''
    def __init__(self, grid_input: List[List[str]]):
        self.grid = grid_input
        self.H = len(self.grid)
        self.W = len(self.grid[0]) if self.H > 0 else 0
        self.start = self.find_position('S')
        self.goal = self.find_position('G')
        self.line_of_sight = set()
        if not self.start or not self.goal:
            raise ValueError("Grid must contain 'S' and 'G'.")
        self.mark_line_of_sight()
    def find_position(self, char: str) -> Tuple[int, int]:
        '''
        Finds the position of a character in the grid.
        '''
        for r in range(self.H):
            for c in range(self.W):
                if self.grid[r][c] == char:
                    return (r, c)
        return None
    def mark_line_of_sight(self):
        '''
        Marks the squares in the line of sight of any person.
        '''
        directions = {
            '>': (0, 1),
            '<': (0, -1),
            'v': (1, 0),
            '^': (-1, 0)
        }
        for r in range(self.H):
            for c in range(self.W):
                if self.grid[r][c] in directions:
                    dr, dc = directions[self.grid[r][c]]
                    nr, nc = r, c
                    # Mark in the direction of the person's sight
                    while 0 <= nr < self.H and 0 <= nc < self.W:
                        if self.grid[nr][nc] == '#':  # Stop at obstacles
                            break
                        if (nr, nc) != self.start and (nr, nc) != self.goal:  # Exclude 'S' and 'G'
                            self.line_of_sight.add((nr, nc))
                        nr += dr
                        nc += dc
                    # Mark the position of the person itself as part of the line of sight
                    if (r, c) != self.start and (r, c) != self.goal:  # Exclude 'S' and 'G'
                        self.line_of_sight.add((r, c))
    def can_reach_goal(self, H: int, W: int, grid: List[List[str]]) -> Tuple[bool, int]:
        '''
        Implements BFS to check if the goal is reachable from the start.
        '''
        self.H = H
        self.W = W
        self.grid = grid
        # Initialize BFS queue
        queue = deque()
        queue.append((self.start, 0))  # Start BFS from 'S'
        visited = set()
        visited.add(self.start)
        while queue:
            (current_r, current_c), moves = queue.popleft()
            if (current_r, current_c) == self.goal:
                return True, moves  # Return the number of moves taken to reach the goal
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Up, Down, Left, Right
                new_r, new_c = current_r + dr, current_c + dc
                if (0 <= new_r < self.H and 0 <= new_c < self.W and
                        (new_r, new_c) not in visited and
                        self.grid[new_r][new_c] != '#' and
                        (new_r, new_c) not in self.line_of_sight):  # Check line of sight
                    visited.add((new_r, new_c))
                    queue.append(((new_r, new_c), moves + 1))
        return False, -1  # Return False if the goal is unreachable