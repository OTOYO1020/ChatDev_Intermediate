'''
Main application file to run the program for calculating minimum operations
to create K consecutive 'o's in a grid.
'''
from operations import min_operations_to_consecutive_o
def main():
    # Read input values
    H = int(input("Enter Height (H): "))
    W = int(input("Enter Width (W): "))
    K = int(input("Enter Consecutive 'o's (K): "))
    S = []
    print("Enter the grid rows (each row on a new line, end with an empty line):")
    while True:
        row = input()
        if row == "":
            break
        S.append(row)
    # Calculate the minimum operations
    result = min_operations_to_consecutive_o(H, W, K, S)
    print(f"Minimum Operations: {result}")
if __name__ == "__main__":
    main()