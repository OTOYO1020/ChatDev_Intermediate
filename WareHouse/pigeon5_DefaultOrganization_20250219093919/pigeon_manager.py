'''
PigeonManager class to manage the pigeons and nests.
'''
class PigeonManager:
    def __init__(self, num_pigeons, num_nests):
        '''
        Initializes the PigeonManager with the given number of pigeons and nests.
        Parameters:
        num_pigeons (int): The number of pigeons.
        num_nests (int): The number of nests.
        '''
        self.nests = [0] * (num_nests + 1)  # Nests indexed from 1
        self.pigeon_locations = [0] * (num_pigeons + 1)  # Pigeons indexed from 1
        for i in range(1, num_pigeons + 1):
            self.pigeon_locations[i] = i  # Initialize pigeon locations
            self.nests[i] = 1  # Each pigeon in its own nest
    def move_pigeon(self, pigeon_id, nest_id):
        '''
        Moves a pigeon from its current nest to a new nest.
        Parameters:
        pigeon_id (int): The ID of the pigeon to move.
        nest_id (int): The ID of the nest to move the pigeon to.
        '''
        current_nest = self.pigeon_locations[pigeon_id]
        if current_nest != nest_id:  # Only move if the nest is different
            # Move the pigeon to the new nest, replacing the existing pigeon
            if self.nests[nest_id] > 0:  # If the destination nest is occupied
                # Find the pigeon currently in the destination nest
                for pid in range(1, len(self.pigeon_locations)):
                    if self.pigeon_locations[pid] == nest_id:
                        # Move the existing pigeon to the current pigeon’s nest
                        self.pigeon_locations[pid] = current_nest
                        self.nests[current_nest] += 1  # Increase count in the current nest
                        break
            # Move the pigeon to the new nest
            self.nests[current_nest] -= 1
            self.nests[nest_id] += 1
            self.pigeon_locations[pigeon_id] = nest_id
    def count_multiple_pigeons(self):
        '''
        Counts the number of nests that contain more than one pigeon.
        Returns:
        int: The count of nests with multiple pigeons.
        '''
        return sum(1 for count in self.nests if count > 1)