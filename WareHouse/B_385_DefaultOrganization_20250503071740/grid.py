'''
Grid class to manage Santa's movements and track visited houses.
'''
class Grid:
    def __init__(self, height, width, start_x, start_y, grid_data):
        self.height = height
        self.width = width
        self.current_position = (start_x, start_y)  # Already in 0-based indexing
        self.grid = grid_data
        self.houses_visited = set()
        # Check if the starting position contains a house and add it to the visited set
        if self.grid[self.current_position[0]][self.current_position[1]] == '@':
            self.houses_visited.add(self.current_position)
    def move_santa(self, commands):
        for command in commands:
            if command not in ['U', 'D', 'L', 'R']:
                print(f"Invalid command '{command}' ignored. Valid commands are: U, D, L, R.")
                continue
            new_position = self.get_new_position(command)
            if self.is_passable(new_position):
                if self.grid[new_position[0]][new_position[1]] == '@':
                    self.houses_visited.add(new_position)
                self.current_position = new_position  # Update only if the position is valid
            else:
                print(f"Invalid move attempted to {new_position}, staying at {self.current_position}.")
        # Return the current position adjusted back to 1-based indexing for output
        final_position_adjusted = (self.current_position[0] + 1, self.current_position[1] + 1)
        return final_position_adjusted, len(self.houses_visited)
    def get_new_position(self, command):
        x, y = self.current_position
        if command == 'U':
            return (x - 1, y)
        elif command == 'D':
            return (x + 1, y)
        elif command == 'L':
            return (x, y - 1)
        elif command == 'R':
            return (x, y + 1)
        return self.current_position
    def is_passable(self, position):
        x, y = position
        if 0 <= x < self.height and 0 <= y < self.width:
            return self.grid[x][y] != '#'
        return False