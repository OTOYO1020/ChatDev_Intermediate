'''
This is the main entry point for the Jewel Converter application.
'''
from jewel_converter import JewelConverter
if __name__ == "__main__":
    # Read inputs from standard input
    N = int(input("Enter level of red jewel (N): "))
    X = int(input("Enter blue jewels from red jewel (X): "))
    Y = int(input("Enter blue jewels from blue jewel (Y): "))
    # Create an instance of JewelConverter
    converter = JewelConverter(N, X, Y)
    # Calculate total blue jewels
    total_blue_jewels = converter.convert_jewels()
    # Print the result
    print(f"Total blue jewels of level 1: {total_blue_jewels}")