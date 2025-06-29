'''
This module defines the SlimeManager class, which manages slime sizes and their counts,
and handles the synthesis process.
'''
class SlimeManager:
    def __init__(self):
        self.slime_counts = {}
    def add_slime(self, size, count):
        '''
        Adds the given count of slimes of a specific size to the slime_counts dictionary.
        Parameters:
        size (int): The size of the slime.
        count (int): The number of slimes of that size.
        '''
        self.slime_counts[size] = self.slime_counts.get(size, 0) + count
    def synthesize_slimes(self):
        '''
        Synthesizes slimes by combining pairs of slimes of the same size to create larger slimes.
        This process continues until no further synthesis can be performed.
        '''
        while True:
            made_changes = False
            sizes_to_check = list(self.slime_counts.keys())  # Get the current sizes to check
            for size in sizes_to_check:
                if self.slime_counts[size] >= 2:
                    made_changes = True
                    new_slimes = self.slime_counts[size] // 2
                    self.slime_counts[size] %= 2
                    self.slime_counts[2 * size] = self.slime_counts.get(2 * size, 0) + new_slimes
            # If no changes were made, break the loop
            if not made_changes:
                break
            # Clean up any sizes that have zero slimes to avoid unnecessary iterations
            self.slime_counts = {size: count for size, count in self.slime_counts.items() if count > 0}
    def get_final_slime_count(self):
        '''
        Returns the total number of slimes remaining after synthesis.
        Returns:
        int: The total count of slimes.
        '''
        return sum(self.slime_counts.values())