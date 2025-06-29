'''
Module to manage pigeons and nests.
'''
class PigeonManager:
    def __init__(self, num_pigeons):
        self.nests = [0] * (num_pigeons + 1)  # Nests indexed from 1
        self.pigeons = [0] * (num_pigeons + 1)  # Pigeon to nest mapping
        for i in range(1, num_pigeons + 1):
            self.nests[i] = 1  # Each pigeon starts in its own nest
            self.pigeons[i] = i  # Pigeon i is in nest i
    def move_pigeon(self, pigeon, new_nest):
        current_nest = self.pigeons[pigeon]
        if current_nest != new_nest:
            self.nests[current_nest] -= 1
            self.nests[new_nest] += 1
            self.pigeons[pigeon] = new_nest
    def count_multiple_pigeons(self):
        return sum(1 for count in self.nests if count > 1)