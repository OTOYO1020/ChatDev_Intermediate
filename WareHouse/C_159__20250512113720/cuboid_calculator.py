'''
This module contains the CuboidVolumeCalculator class which provides
a method to calculate the maximum volume of a cuboid given the sum
of its dimensions L.
'''
class CuboidVolumeCalculator:
    @staticmethod
    def max_volume_cuboid(L: int) -> float:
        """
        Calculate the maximum volume of a rectangular cuboid given the sum of its dimensions L.
        Parameters:
        L (int): The sum of the dimensions of the cuboid. Must be within the range 1 ≤ L ≤ 1000.
        Returns:
        float: The maximum volume of the cuboid.
        """
        if L < 1 or L > 1000:
            raise ValueError("L must be between 1 and 1000.")
        # Calculate dimensions ensuring they are as equal as possible and are integers
        a = L // 3
        b = L // 3
        c = L - (a + b)  # Ensure the sum of dimensions equals L
        # Calculate volume
        volume = a * b * c
        return float(volume)