'''
PigeonManager class to manage pigeons and nests.
'''
class PigeonManager:
    def __init__(self, num_pigeons):
        self.nests = [0] * (num_pigeons + 1)  # Nests indexed from 1 to num_pigeons
        self.pigeons = [0] * (num_pigeons + 1)  # Initialize pigeon counts to 0
        self.multi_pigeon_nests = 0  # Counter for nests with multiple pigeons
        for i in range(1, num_pigeons + 1):
            self.nests[i] = i  # Initial placement of pigeons
            self.pigeons[i] = 1  # Each pigeon starts in its own nest
            if i > 1:  # Only the first pigeon starts in its own nest
                self.multi_pigeon_nests += 1  # Increment for the first pigeon
    def move_pigeon(self, pigeon_id, nest_id):
        current_nest = self.nests[pigeon_id]
        if current_nest != nest_id:
            # Update the current nest
            self.pigeons[current_nest] -= 1
            if self.pigeons[current_nest] == 1:  # If it goes from 1 to 0
                self.multi_pigeon_nests -= 1
            # Update the new nest
            self.pigeons[nest_id] += 1
            if self.pigeons[nest_id] == 2:  # If it goes from 1 to 2
                self.multi_pigeon_nests += 1
            # Update the pigeon's current nest
            self.nests[pigeon_id] = nest_id
    def count_nests_with_multiple_pigeons(self):
        return self.multi_pigeon_nests