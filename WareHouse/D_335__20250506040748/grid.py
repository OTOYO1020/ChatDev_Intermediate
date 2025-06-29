'''
Grid class to manage the placement of Takahashi and dragon parts.
'''
class Grid:
    def __init__(self, n):
        self.size = n
        self.grid = [[0 for _ in range(n)] for _ in range(n)]
        self.current_part = 1
        self.takahashi_position = (n // 2, n // 2)
        self.grid[self.takahashi_position[0]][self.takahashi_position[1]] = 'T'
    def place_parts(self):
        '''
        Places dragon parts in the grid adjacent to Takahashi.
        The placement is done systematically in available adjacent cells.
        '''
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        current_position = (self.takahashi_position[0] + 1, self.takahashi_position[1])  # Start below Takahashi
        self.place_part(0, self.takahashi_position)  # Ensure Takahashi is marked
        self.place_part(self.current_part, current_position)  # Place first part
        self.current_part += 1
        positions_to_explore = [current_position]
        while self.current_part < self.size ** 2:
            placed = False
            if not positions_to_explore:
                print("Unable to place all parts, stopping placement.")
                break
            current_position = positions_to_explore.pop(0)  # Get the next position to explore
            for direction in directions:
                new_position = (current_position[0] + direction[0], current_position[1] + direction[1])
                if self.is_valid_position(new_position):
                    self.place_part(self.current_part, new_position)
                    positions_to_explore.append(new_position)  # Add new position to explore
                    self.current_part += 1
                    placed = True
                    break  # Exit the loop after placing one part
            if not placed:
                print("No valid placements found for the current part.")
                # Backtrack to the last valid position if needed
                if positions_to_explore:
                    current_position = positions_to_explore[-1]  # Go back to the last valid position
    def is_valid_position(self, position):
        '''
        Checks if the given position is valid (within bounds and not occupied).
        '''
        x, y = position
        return 0 <= x < self.size and 0 <= y < self.size and self.grid[x][y] == 0
    def place_part(self, part, position):
        '''
        Places a dragon part at the specified position in the grid.
        '''
        self.grid[position[0]][position[1]] = part
    def get_grid(self):
        '''
        Returns the current state of the grid.
        '''
        return self.grid