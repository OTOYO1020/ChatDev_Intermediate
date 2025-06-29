'''
This module contains the main application that provides a command-line interface
for calculating the maximum volume of a cuboid based on user input.
'''
from cuboid_calculator import CuboidVolumeCalculator
def main():
    try:
        L = int(input("Enter the sum of dimensions (L): "))
        volume = CuboidVolumeCalculator.max_volume_cuboid(L)
        print(f"Max Volume: {volume:.2f}")
    except ValueError as e:
        print(f"Input Error: {str(e)}")
if __name__ == "__main__":
    main()