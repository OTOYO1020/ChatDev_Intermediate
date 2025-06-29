'''
Main file to run the Sudoku validation application using standard input.
'''
from typing import List
from sudoku_validator import is_valid_sudoku
def main():
    while True:  # Allow the user to restart the input process
        grid = []
        print("Enter the Sudoku grid (9 lines with 9 integers each, separated by spaces). Example: '5 3 0 0 7 0 0 0 0':")
        for _ in range(9):
            attempts = 0
            while attempts < 3:  # Allow up to 3 attempts
                try:
                    line = input().strip()
                    if not line:  # Check for empty input
                        raise ValueError("Input cannot be empty.")
                    row = list(map(int, line.split()))
                    if len(row) != 9 or any(num < 0 or num > 9 for num in row):  # Ensure numbers are between 0 and 9
                        raise ValueError("Each row must contain 9 integers between 0 and 9.")
                    grid.append(row)
                    break
                except ValueError as e:
                    attempts += 1
                    print(f"Invalid input: {e}. You have {3 - attempts} attempts left.")
                except Exception as e:
                    attempts += 1
                    print(f"Unexpected error: {e}. You have {3 - attempts} attempts left.")
            if attempts == 3:
                print("Too many invalid attempts for this row. Please restart the input process.")
                grid.clear()  # Clear the grid to indicate a restart
                break  # Exit the inner loop to restart the grid input process
        else:  # This else corresponds to the for loop, executes if no break occurs
            if len(grid) != 9:  # Check if we have exactly 9 rows
                print("Incomplete grid. Please restart the input process.")
                continue  # Restart the input process
            result = is_valid_sudoku(grid)
            print(result)
            break  # Exit the loop after successful input and validation
if __name__ == "__main__":
    main()