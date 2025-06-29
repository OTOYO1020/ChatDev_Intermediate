'''
Module to calculate the maximum volume of a cuboid given a positive integer L.
'''
class CuboidVolumeCalculator:
    '''
    Class to encapsulate the logic for calculating the maximum volume of a cuboid.
    '''
    def max_volume(self, L):
        '''
        Calculates the maximum volume of a cuboid with dimensions a, b, c such that a + b + c = L.
        The method uses a mathematical approach to find the maximum volume.
        '''
        max_volume = 0
        # Iterate a from 1 to L // 3
        for a in range(1, L // 3 + 1):
            b = (L - a) // 2  # Set b to half of the remaining length
            c = L - a - b  # Calculate c
            if b > 0 and c > 0:  # Ensure b and c are positive
                volume = a * b * c
                if volume > max_volume:
                    max_volume = volume
        return max_volume