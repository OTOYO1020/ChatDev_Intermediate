'''
Main entry point for the application that reads input and calculates the number of ways to reach a target cell in a grid.
'''
from grid_logic import GridLogic
def main():
    while True:
        try:
            x = int(input("Enter X (1 ≤ X ≤ 10^6): "))
            y = int(input("Enter Y (1 ≤ Y ≤ 10^6): "))
            # Validate the input values to ensure they are within the specified range
            if not (1 <= x <= 10**6 and 1 <= y <= 10**6):
                print("Input values must be between 1 and 10^6. Please try again.")
                continue  # Prompt for input again if values are out of range
            break  # Exit loop if input is valid
        except ValueError:
            print("Input Error: Please enter valid integers.")
    grid_logic = GridLogic()
    result = grid_logic.calculate_ways(x, y)
    print(f"Ways to reach ({x}, {y}): {result}")
if __name__ == "__main__":
    main()