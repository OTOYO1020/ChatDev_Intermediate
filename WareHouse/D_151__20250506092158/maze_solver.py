'''
Module to solve the maze using BFS to find the maximum moves between road squares.
'''
from collections import deque
class MazeSolver:
    def __init__(self, width, height, grid):
        self.width = width
        self.height = height
        self.grid = grid
    def bfs(self, start, goal):
        """
        Perform Breadth-First Search to find the shortest path from start to goal.
        Parameters:
        start (tuple): The starting position in the maze (row, column).
        goal (tuple): The goal position in the maze (row, column).
        Returns:
        int: The number of moves required to reach the goal from the start, or float('inf') if no path exists.
        Note: If the start or goal is surrounded by walls, the BFS will return float('inf').
        """
        # If start and goal are the same, return 0 moves immediately
        if start == goal:
            return 0
        queue = deque([start])
        visited = set()  # Reset visited for each BFS call
        visited.add(start)
        moves = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
        while queue:
            for _ in range(len(queue)):
                current = queue.popleft()
                if current == goal:
                    return moves  # Return the number of moves when goal is reached
                # Explore all possible directions
                for direction in directions:
                    next_pos = (current[0] + direction[0], current[1] + direction[1])
                    # Check if the next position is valid and not visited
                    if (0 <= next_pos[0] < self.height and
                        0 <= next_pos[1] < self.width and
                        next_pos not in visited and
                        self.grid[next_pos[0]][next_pos[1]] == '.'):
                        visited.add(next_pos)
                        queue.append(next_pos)
        return float('inf')  # Return float('inf') to indicate no path found
    def calculate_max_moves(self):
        road_squares = [(i, j) for i in range(self.height) for j in range(self.width) if self.grid[i][j] == '.']
        if not road_squares:  # Check if there are no road squares
            return 0  # No moves possible if there are no road squares
        max_moves = 0
        for start in road_squares:
            for goal in road_squares:
                if start != goal:  # Ensure we only call bfs for different start and goal
                    moves = self.bfs(start, goal)
                    if moves != float('inf'):  # Only update max_moves if a valid path exists
                        max_moves = max(max_moves, moves)
        return max_moves