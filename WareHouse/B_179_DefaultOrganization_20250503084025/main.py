'''
Main file to run the Dice Roll application.
'''
from dice_roll import check_doublets
def main():
    N = 0
    while True:  # Loop until valid input is received
        try:
            N = int(input("Enter number of rolls (3-100): "))
            if N < 3 or N > 100:
                print("N must be between 3 and 100. Please try again.")
                continue  # Prompt again
            break  # Exit the loop if input is valid
        except ValueError:
            print("Please enter a valid integer.")
    dice_rolls = []
    for i in range(N):
        while True:  # Loop until valid input is received
            try:
                D1, D2 = map(int, input(f"Enter roll {i + 1} (two integers separated by space): ").split())
                if len([D1, D2]) != 2:  # Check if exactly two integers are provided
                    raise ValueError("You must enter exactly two integers.")
                dice_rolls.append((D1, D2))
                break  # Exit the loop if input is valid
            except ValueError as e:
                print(f"Error: {e}. Please enter two valid integers separated by space.")
    result = check_doublets(dice_rolls)
    print(result)
if __name__ == "__main__":
    main()