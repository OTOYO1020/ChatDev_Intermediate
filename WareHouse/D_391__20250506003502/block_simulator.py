'''
Defines the BlockSimulator class to manage blocks and handle queries.
'''
from block import Block
class BlockSimulator:
    def __init__(self, blocks):
        self.blocks = blocks
        self.final_positions = {}
    def simulate(self, height):
        filled_positions = set()
        for block in self.blocks:
            final_pos = block.final_position(height, filled_positions)
            # Ensure that the position is not already filled
            while final_pos in filled_positions:
                final_pos = (final_pos[0], final_pos[1] + 1)  # Move up if the position is filled
            self.final_positions[block.block_id] = final_pos  # Use block ID as key
            filled_positions.add(final_pos)  # Mark this position as filled
    def query(self, block_id, time):
        # Check if block_id is valid
        if block_id < 1 or block_id > len(self.blocks):
            return False  # Block ID is out of range
        final_pos = self.final_positions.get(block_id)
        if final_pos is None:
            return False  # Final position not found
        return final_pos[1] == time  # Check if the final position's y-coordinate equals T_j