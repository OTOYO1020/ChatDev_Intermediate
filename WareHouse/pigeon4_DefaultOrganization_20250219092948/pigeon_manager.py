'''
This module manages the pigeons and nests.
'''
class PigeonManager:
    def __init__(self, num_pigeons):
        # Initialize each pigeon in its corresponding nest
        self.pigeons = {i: i for i in range(1, num_pigeons + 1)}  # Pigeon i starts in nest i
        self.nests = {i: 1 for i in range(1, num_pigeons + 1)}  # Each nest starts with one pigeon
    def move_pigeon(self, pigeon_id, nest_id):
        # Move pigeon from its current nest to a new nest
        current_nest = self.pigeons[pigeon_id]
        if current_nest != nest_id:
            # Update the count of pigeons in the affected nests
            self.nests[current_nest] -= 1
            self.nests[nest_id] += 1
            self.pigeons[pigeon_id] = nest_id
    def count_multiple_pigeons(self):
        # Count the number of nests that contain more than one pigeon
        return sum(1 for count in self.nests.values() if count > 1)