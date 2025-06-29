'''
Calculator module for calculating the black area based on given coordinates.
'''
from collections import deque
def calculate_black_area(A: int, B: int, C: int, D: int) -> int:
    # Handle edge cases for very large or very small values
    if A > C or B > D:
        return 0  # Invalid rectangle
    # Create a grid representation of the rectangle
    width = C - A + 1
    height = D - B + 1
    grid = [[0 for _ in range(width)] for _ in range(height)]
    # Fill the grid based on the rules for black areas
    for x in range(width):
        for y in range(height):
            actual_x = x + A
            actual_y = y + B
            # Check if the point is on any of the specified lines
            if (actual_x == A or actual_x == C or actual_y == B or actual_y == D or 
                (actual_x + actual_y >= A + B and actual_x + actual_y <= C + D)):
                grid[y][x] = 1  # Mark as black area
    # Implement adjacency coloring using BFS to ensure different colors for adjacent regions
    def color_adjacent(y, x, color):
        queue = deque([(y, x)])
        while queue:
            cy, cx = queue.popleft()
            if cy < 0 or cy >= height or cx < 0 or cx >= width or grid[cy][cx] != 1:
                continue
            grid[cy][cx] = color
            # Color adjacent cells
            for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                queue.append((cy + dy, cx + dx))
    # Color the black areas
    color = 2  # Start coloring from 2 to avoid confusion with black areas
    for y in range(height):
        for x in range(width):
            if grid[y][x] == 1:  # If it's a black area
                color_adjacent(y, x, color)
                color += 1  # Increment color for the next region
    # Calculate the total area of black regions
    black_area = sum(sum(1 for cell in row if cell == 1) for row in grid)
    # Double the calculated area of the black regions
    final_result = black_area * 2
    return final_result