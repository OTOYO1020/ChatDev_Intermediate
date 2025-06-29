'''
Grid class to manage the grid structure, bulbs, blocks, and illumination logic.
'''
class Grid:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.grid = [['.' for _ in range(width)] for _ in range(height)]
        self.bulbs = []
        self.blocks = []
    def add_bulbs(self, bulb_coords):
        for A, B in bulb_coords:
            if not (0 <= A < self.height and 0 <= B < self.width):
                raise ValueError(f"Invalid coordinates for bulb ({A}, {B}). Please enter values within the grid dimensions (0 to {self.height-1}, 0 to {self.width-1}).")
            if self.grid[A][B] in ['B', 'X']:  # Check if there's a bulb or block at the position
                raise ValueError(f"Cannot place a bulb on a block or another bulb at ({A}, {B}).")
            if (A, B) in self.bulbs:  # Check for uniqueness
                raise ValueError(f"Duplicate bulb coordinates ({A}, {B}) are not allowed.")
            self.bulbs.append((A, B))
            self.grid[A][B] = 'B'  # Mark bulb on grid
    def add_blocks(self, block_coords):
        for C, D in block_coords:
            if not (0 <= C < self.height and 0 <= D < self.width):
                raise ValueError(f"Invalid coordinates for block ({C}, {D}). Please enter values within the grid dimensions (0 to {self.height-1}, 0 to {self.width-1}).")
            if self.grid[C][D] in ['B', 'X']:  # Check if there's a bulb or block at the position
                raise ValueError(f"Cannot place a block on a bulb or another block at ({C}, {D}).")
            if (C, D) in self.blocks:  # Check for uniqueness
                raise ValueError(f"Duplicate block coordinates ({C}, {D}) are not allowed.")
            self.blocks.append((C, D))
            self.grid[C][D] = 'X'  # Mark block on grid
    def illuminate(self):
        illuminated = set()
        for A, B in self.bulbs:
            # Skip illumination if the bulb is on a block
            if self.grid[A][B] == 'X':
                continue
            # Include the bulb's own position as illuminated
            illuminated.add((A, B))
            # Illuminate in all four directions
            for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  # right, down, left, up
                x, y = A, B
                while True:
                    x += direction[0]
                    y += direction[1]
                    if 0 <= x < self.height and 0 <= y < self.width:
                        if self.grid[x][y] == 'X':  # Block encountered
                            break
                        illuminated.add((x, y))  # Add illuminated square
                    else:  # Edge of grid
                        break
        return len(illuminated)