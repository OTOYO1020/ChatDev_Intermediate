'''
Main entry point for the Sudoku validation application.
'''
from validator import is_valid_sudoku
def main():
    while True:  # Loop until a valid grid is entered
        A = []
        print("Please enter the 9x9 Sudoku grid (each row on a new line):")
        for _ in range(9):
            try:
                row = list(map(int, input().strip().split()))
                if len(row) != 9 or any(num < 1 or num > 9 for num in row):
                    raise ValueError  # Raise an error if the input is invalid
                A.append(row)
            except ValueError:
                print("Invalid input. Each row must contain exactly 9 integers between 1 and 9.")
                break  # Exit the for loop to prompt for input again
        else:  # This else corresponds to the for loop
            if len(A) != 9:
                print("Invalid input. The grid must be a complete 9x9 grid.")
                continue  # Prompt for input again
            # Validate the entire grid
            if is_valid_sudoku(A):
                print("Yes")
            else:
                print("No")
            break  # Exit the while loop after successful validation
if __name__ == "__main__":
    main()