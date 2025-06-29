Here's a detailed user manual for the Sudoku validation application, formatted in Markdown as requested:

```markdown
# Sudoku Validator

A simple application to validate Sudoku grids based on standard Sudoku rules.

## Overview

The Sudoku Validator checks if a given 9x9 grid satisfies the conditions of a valid Sudoku puzzle. Each row, column, and 3x3 subgrid must contain the integers 1 to 9 exactly once.

## Main Functions

- **is_valid_sudoku(grid: List[List[int]]) -> str**: Main function to validate the Sudoku grid.
- **check_rows(grid: List[List[int]]) -> bool**: Helper function to verify that each row contains the integers 1 to 9 exactly once.
- **check_columns(grid: List[List[int]]) -> bool**: Helper function to verify that each column contains the integers 1 to 9 exactly once.
- **check_subgrids(grid: List[List[int]]) -> bool**: Helper function to verify that each 3x3 subgrid contains the integers 1 to 9 exactly once.

## Installation

To run the Sudoku Validator, you need to have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

### Dependencies

This application requires no additional dependencies beyond Python's standard library.

## How to Use

1. **Clone the Repository**: If you haven't already, clone the repository containing the application code.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Run the Application**: Execute the main script to start the application.

   ```bash
   python main.py
   ```

3. **Input the Sudoku Grid**: The application will prompt you to enter a 9x9 Sudoku grid. You should enter 9 lines, each containing 9 integers separated by spaces. For example:

   ```
   5 3 0 0 7 0 0 0 0
   6 0 0 1 9 5 0 0 0
   0 9 8 0 0 0 0 6 0
   8 0 0 0 6 0 0 0 3
   4 0 0 8 0 3 0 0 1
   7 0 0 0 2 0 0 0 6
   0 6 0 0 0 0 2 8 0
   0 0 0 4 1 9 0 0 5
   0 0 0 0 8 0 0 7 9
   ```

   Note: Use `0` for empty cells.

4. **Validation Result**: After entering the grid, the application will validate it and print either "Yes" if the grid is valid or "No" if it is not.

5. **Restart or Exit**: You can restart the input process if you wish to validate another grid or exit the application.

## Error Handling

- The application allows up to 3 attempts to enter each row correctly. If you exceed this limit, it will prompt you to restart the input process.
- Ensure that each row contains exactly 9 integers between 0 and 9 (where `0` represents an empty cell).

## Conclusion

The Sudoku Validator is a straightforward tool for checking the validity of Sudoku grids. It is designed to be user-friendly and provides clear feedback on input errors. Enjoy validating your Sudoku puzzles!
```

This manual provides a comprehensive guide for users to understand the functionality of the Sudoku Validator application, how to install it, and how to use it effectively.