Here's a detailed user manual for the Sudoku validation software, formatted in Markdown as requested:

```markdown
# Sudoku Validator

A simple application to validate Sudoku grids, ensuring that each number from 1 to 9 appears exactly once in each row, column, and 3x3 subgrid.

## Main Functions

The Sudoku Validator includes the following main functions:

1. **Input Validation**: Ensures that the user inputs a complete 9x9 grid with integers between 1 and 9.
2. **Row Validation**: Checks that each row contains all integers from 1 to 9 exactly once.
3. **Column Validation**: Checks that each column contains all integers from 1 to 9 exactly once.
4. **Subgrid Validation**: Validates that each 3x3 subgrid contains all integers from 1 to 9 exactly once.
5. **User Interface**: Provides a graphical user interface (GUI) for easy input and validation of Sudoku grids.

## Installation

To run the Sudoku Validator, you need to have Python installed on your system. Follow these steps to set up the environment:

1. **Install Python**: Download and install Python from the [official website](https://www.python.org/downloads/).

2. **Clone the Repository**: Clone the repository containing the Sudoku Validator code.
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

3. **Install Dependencies**: Use pip to install the required dependencies. Open your terminal and run:
   ```bash
   pip install tkinter
   ```

## How to Use the Sudoku Validator

### Command Line Interface

1. **Run the Application**: Open your terminal, navigate to the directory where the `main.py` file is located, and run:
   ```bash
   python main.py
   ```

2. **Input the Sudoku Grid**: You will be prompted to enter the 9x9 Sudoku grid. Each row should be entered on a new line, with numbers separated by spaces. For example:
   ```
   5 3 4 6 7 8 9 1 2
   6 7 2 1 9 5 3 4 8
   1 9 8 3 4 2 5 6 7
   8 5 9 7 6 1 4 2 3
   4 2 6 8 5 3 7 9 1
   7 1 3 9 2 4 8 5 6
   9 6 1 5 3 7 2 8 4
   2 8 7 4 1 9 6 3 5
   3 4 5 2 8 6 1 7 9
   ```

3. **Validation Result**: After entering the grid, the application will validate the input and print "Yes" if the Sudoku grid is valid, or "No" if it is not.

### Graphical User Interface

1. **Run the Application**: Open your terminal, navigate to the directory where the `gui.py` file is located, and run:
   ```bash
   python gui.py
   ```

2. **Enter the Sudoku Grid**: A window will appear with a 9x9 grid of entry fields. Fill in each cell with integers between 1 and 9.

3. **Validate the Grid**: Click the "Validate" button to check the Sudoku grid. If there are any errors (e.g., empty cells or invalid numbers), an error message will be displayed. Otherwise, a message box will show whether the grid is valid ("Yes") or not ("No").

## Conclusion

The Sudoku Validator is a straightforward tool for checking the validity of Sudoku grids. Whether you prefer using the command line or a graphical interface, this application provides an easy way to ensure your Sudoku puzzles are correctly formatted. Enjoy validating your Sudoku grids!
```

This manual provides a comprehensive overview of the software, including its main functions, installation instructions, and usage guidelines for both command line and GUI interfaces.