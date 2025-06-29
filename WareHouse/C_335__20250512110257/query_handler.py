'''
Module to handle the logic of processing queries related to part positions.
'''
class QueryHandler:
    def __init__(self, N):
        # Initialize positions starting from (1, 0) for part 1 to (N, 0) for part N
        self.positions = [(i, 0) for i in range(1, N + 1)]  # Correct initialization
    def update_position(self, direction):
        # Store the current head's position
        head_x, head_y = self.positions[0]
        # Update head's position based on the direction
        if direction == 'R':
            head_x += 1
        elif direction == 'L':
            head_x -= 1
        elif direction == 'U':
            head_y += 1
        elif direction == 'D':
            head_y -= 1
        else:
            raise ValueError("Invalid direction")
        # Ensure head's position does not go below (1, 0)
        head_x = max(head_x, 1)
        head_y = max(head_y, 0)
        # Move each part to the position of the part in front
        for i in range(len(self.positions) - 1, 0, -1):
            self.positions[i] = self.positions[i - 1]  # Each part takes the position of the part in front
        # Update the head's position last
        self.positions[0] = (head_x, head_y)
    def get_position(self, p):
        if p < 1 or p > len(self.positions):
            raise IndexError("Part index out of range")
        return self.positions[p - 1]  # Access the positions list using zero-based indexing