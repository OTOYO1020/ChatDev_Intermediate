'''
Main entry point for the Grid Counter application.
'''
from grid_counter import GridCounter
def main():
    '''
    Main function to handle user input and output results.
    '''
    try:
        # Parse input for row and column sums
        h1 = int(input("Enter Row sum 1 (h1): "))
        h2 = int(input("Enter Row sum 2 (h2): "))
        h3 = int(input("Enter Row sum 3 (h3): "))
        w1 = int(input("Enter Column sum 1 (w1): "))
        w2 = int(input("Enter Column sum 2 (w2): "))
        w3 = int(input("Enter Column sum 3 (w3): "))
        grid_counter = GridCounter()
        result = grid_counter.countWays(h1, h2, h3, w1, w2, w3)
        print(f"Valid configurations: {result}")
    except ValueError:
        print("Please enter valid integers.")
if __name__ == "__main__":
    main()