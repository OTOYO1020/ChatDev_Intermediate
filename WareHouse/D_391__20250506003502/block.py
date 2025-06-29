'''
Defines the Block class to represent each block's position and movement.
'''
class Block:
    def __init__(self, x, y, block_id):
        self.x = x
        self.y = y
        self.block_id = block_id  # Unique identifier for each block
    def final_position(self, height, filled_positions):
        # Block cannot move below the bottom of the simulation
        if self.y >= height - 1:
            return (self.x, self.y)  # Block stays at its current position
        # Find the highest filled position at the block's x-coordinate
        highest_filled_y = max((y for x, y in filled_positions if x == self.x), default=-1)
        # Block stops just above the highest filled position
        if highest_filled_y >= self.y:
            return (self.x, highest_filled_y + 1)  # Block stops just above the highest filled position
        elif highest_filled_y == -1:
            return (self.x, height - 1)  # Block falls to the bottom if no blocks are below
        return (self.x, highest_filled_y + 1)  # Block stops just above the highest filled position