'''
Module to manage pigeons and nests.
'''
class PigeonNestManager:
    def __init__(self, N):
        self.nests = {i: 1 for i in range(1, N + 1)}  # Each nest starts with one pigeon
        self.pigeon_locations = {i: i for i in range(1, N + 1)}  # Pigeon i in Nest i
        self.multiple_pigeons_count = 0  # Track nests with multiple pigeons
    def move_pigeon(self, pigeon, nest):
        current_nest = self.pigeon_locations[pigeon]
        # Update the count of the current nest
        if self.nests[current_nest] > 0:
            # Check if the current nest had multiple pigeons before decrementing
            if self.nests[current_nest] == 2:
                self.multiple_pigeons_count -= 1  # A nest lost its multiple pigeons status
            self.nests[current_nest] -= 1  # Decrease the count of pigeons in the current nest
        # Move pigeon to the new nest
        if nest not in self.nests:
            self.nests[nest] = 0  # Initialize the nest if it doesn't exist
        # Check the new nest status before incrementing
        if self.nests[nest] == 1:  # If the nest had one pigeon before
            self.multiple_pigeons_count += 1  # Now it will have multiple pigeons
        elif self.nests[nest] == 2:  # If the nest had two pigeons before
            pass  # No change in multiple pigeons count
        elif self.nests[nest] == 0:  # If the nest was empty before
            pass  # No change in multiple pigeons count
        self.nests[nest] += 1  # Increase the count of pigeons in the new nest
        # Update the pigeon location
        self.pigeon_locations[pigeon] = nest
    def count_multiple_pigeons(self):
        return self.multiple_pigeons_count