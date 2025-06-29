'''
Grid class to manage the grid state and movement logic.
'''
class Grid:
    def __init__(self, height, width, configuration):
        self.height = height
        self.width = width
        self.configuration = configuration
    def is_valid_move(self, current_i, current_j, direction):
        if direction == 'L':
            return current_j > 0 and self.configuration[current_i][current_j - 1] == '.'
        elif direction == 'R':
            return current_j < self.width - 1 and self.configuration[current_i][current_j + 1] == '.'
        elif direction == 'U':
            return current_i > 0 and self.configuration[current_i - 1][current_j] == '.'
        elif direction == 'D':
            return current_i < self.height - 1 and self.configuration[current_i + 1][current_j] == '.'
        return False
    def execute_movements(self, start_i, start_j, movements):
        # Convert to zero-based indexing
        current_i, current_j = start_i - 1, start_j - 1  
        # Validate movements
        valid_moves = {'L', 'R', 'U', 'D'}
        if any(move not in valid_moves for move in movements):
            print("Error: Invalid movement characters found. Only 'L', 'R', 'U', 'D' are allowed.")
            return (start_i, start_j)  # Return the starting position if invalid moves are found
        if not movements:  # Check for empty movements
            print("No movements provided. Staying at the starting position.")
            return (start_i, start_j)  # Return the starting position if no movements are given
        for move in movements:
            if self.is_valid_move(current_i, current_j, move):
                if move == 'L':
                    current_j -= 1
                elif move == 'R':
                    current_j += 1
                elif move == 'U':
                    current_i -= 1
                elif move == 'D':
                    current_i += 1
            else:
                print(f"Invalid move: {move} from position ({current_i + 1}, {current_j + 1}). Move blocked or out of bounds.")
        return (current_i + 1, current_j + 1)  # Convert back to one-based indexing