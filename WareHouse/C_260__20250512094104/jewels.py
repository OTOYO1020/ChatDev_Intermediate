'''
Module containing the function to calculate maximum blue jewels.
'''
def max_blue_jewels(N: int, X: int, Y: int) -> int:
    if N < 1 or N > 10:
        return 0  # Return 0 for invalid N values
    def convert(level: int) -> int:
        if level == 1:
            return 0  # Base case: no additional blue jewels from red jewels at level 1
        else:
            # Convert red jewel of level n to blue jewels of level n
            blue_jewels_from_red = X
            # Convert blue jewels of level n to blue jewels of level n-1
            blue_jewels_from_blue = convert(level - 1) * Y
            # Total blue jewels from this level, including those from level n-1
            return blue_jewels_from_red + blue_jewels_from_blue
    total_blue_jewels = convert(N)
    return total_blue_jewels