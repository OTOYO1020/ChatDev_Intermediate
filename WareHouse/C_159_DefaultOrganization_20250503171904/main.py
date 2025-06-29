'''
Main application file to run the cuboid volume calculator.
'''
from cuboid_volume_calculator import CuboidVolumeCalculator
def main():
    '''
    Main function to run the application.
    '''
    try:
        L = int(input("Enter a positive integer L (1 <= L <= 1000): "))
        if 1 <= L <= 1000:
            calculator = CuboidVolumeCalculator()
            max_vol = calculator.max_volume(L)
            print(f"Maximum Volume: {max_vol}")
        else:
            print("Please enter a value between 1 and 1000.")
    except ValueError:
        print("Invalid input. Please enter a positive integer.")
if __name__ == "__main__":
    main()