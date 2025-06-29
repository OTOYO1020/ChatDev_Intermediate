'''
Module to manage the dragon's parts and their positions.
'''
class Dragon:
    def __init__(self, n):
        '''
        Initializes the dragon with n parts, setting initial positions.
        '''
        self.positions = [(i, 0) for i in range(n)]
    def move(self, direction):
        '''
        Moves the dragon's head in the specified direction and updates positions.
        '''
        # Store the current head position
        previous_head_position = self.positions[0]
        x, y = previous_head_position
        # Update head position based on direction
        if direction == 'R':
            x += 1
        elif direction == 'L':
            x -= 1
        elif direction == 'U':
            y += 1
        elif direction == 'D':
            y -= 1
        # Set the new head position
        self.positions[0] = (x, y)
        # Move each part to the position of the part in front of it
        for i in range(1, len(self.positions)):
            # Move part i to where part i-1 was
            self.positions[i] = previous_head_position
            # Update previous_head_position for the next part
            previous_head_position = self.positions[i]
    def get_position(self, part_number):
        '''
        Returns the coordinates of the specified part.
        '''
        return self.positions[part_number - 1]