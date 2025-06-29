'''
Contains the BlockSimulator class to handle block movement simulation.
'''
from typing import List, Tuple
class BlockSimulator:
    def __init__(self, N: int, W: int, blocks: List[Tuple[int, int]], Q: int, queries: List[Tuple[int, int]]):
        self.N = N
        self.W = W
        self.blocks = blocks
        self.Q = Q
        self.queries = queries
        self.grid = [[0] * W for _ in range(N)]
        # Initialize blocks in the grid
        for x, y in blocks:
            if 0 <= x < W and 0 <= y < N:  # Ensure blocks are within bounds
                self.grid[y][x] = 1
    def block_exists(self, block_index: int, time: float) -> str:
        # Logic to check if the block exists at time T + 0.5
        self.simulate(time + 0.5)  # Simulate for T + 0.5 seconds
        if block_index < len(self.blocks):  # Check if the block index is still valid
            x, y = self.blocks[block_index]
            return "YES" if 0 <= y < self.N and self.grid[y][x] == 1 else "NO"
        return "NO"  # If the block index is invalid, return "NO"
    def simulate(self, time: float):
        # Create a temporary grid to track the final positions
        temp_grid = [[0] * self.W for _ in range(self.N)]
        new_blocks = []
        for index, (x, y) in enumerate(self.blocks):
            # Calculate the new position after 'time' seconds
            new_y = int(y + time)
            if new_y >= self.N:  # If it goes beyond the grid, it will be removed
                continue  # Do not add to new_blocks
            # Check if the new position is occupied
            if temp_grid[new_y][x] == 0:
                temp_grid[new_y][x] = 1  # Place the block in the new position
                new_blocks.append((x, new_y))  # Keep track of the new position
            else:
                # If occupied, find the first available position below
                for below in range(new_y, self.N):
                    if temp_grid[below][x] == 0:
                        temp_grid[below][x] = 1  # Place the block in the first available position
                        new_blocks.append((x, below))  # Keep track of the new position
                        break
                # If no available position is found, the block is effectively removed
        # Update the grid with the new positions
        self.grid = temp_grid
        # Update the blocks list to reflect the new positions
        self.blocks = new_blocks