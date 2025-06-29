'''
Module containing the SlimeSynthesizer class for calculating minimum slimes.
'''
from typing import List
class SlimeSynthesizer:
    '''
    Class to synthesize slimes based on sizes and counts.
    '''
    def min_slimes(self, N: int, sizes: List[int], counts: List[int]) -> int:
        '''
        Calculate the minimum number of slimes after optimal synthesis.
        '''
        slime_map = dict(zip(sizes, counts))
        while True:
            new_slime_map = {}
            total_leftover_slimes = 0  # Track leftover slimes separately
            pairs_formed = False
            for size, count in slime_map.items():
                pairs = count // 2  # Calculate how many pairs can be formed
                leftover = count % 2  # Check if there's a leftover slime
                if pairs > 0:
                    pairs_formed = True
                    # Synthesize slimes of the same size if possible
                    new_slime_map[size] = new_slime_map.get(size, 0) + pairs
                total_leftover_slimes += leftover  # Accumulate leftover slimes
            # If no pairs were formed, we can break the loop
            if not pairs_formed:
                break
            # Add leftover slimes back to the slime_map for the next iteration
            if total_leftover_slimes > 0:
                new_slime_map['leftover'] = total_leftover_slimes
            # Update slime_map for the next iteration
            slime_map = new_slime_map
        # Return the total remaining slimes including leftovers
        return sum(slime_map.values())  # Return the correct count of leftover slimes