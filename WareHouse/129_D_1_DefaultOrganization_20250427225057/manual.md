Here's a detailed user manual for the lighted squares application, formatted in Markdown:

```markdown
# Lighted Squares Application

A Python application designed to calculate the maximum number of squares that can be lighted by placing a lamp optimally on a grid. The grid is represented by a combination of empty squares ('.') and obstacles ('#').

## Main Functions

- **Input Handling**: Reads the dimensions of the grid and the grid layout from the user.
- **Light Count Calculation**: Computes how many squares can be lighted from each position in the grid.
- **Maximum Lighted Squares Calculation**: Determines the maximum number of squares that can be lighted by placing a lamp in the optimal position.
- **Output**: Displays the result to the user.

## Installation

To run the Lighted Squares application, you need to have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

### Environment Dependencies

This application does not have any external dependencies beyond the standard Python library. However, it is recommended to use Python 3.6 or higher.

## How to Use the Application

1. **Clone the Repository**: If you have the source code in a repository, clone it to your local machine using:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Run the Application**: Execute the `main.py` script to start the application:
   ```bash
   python main.py
   ```

3. **Input the Grid Dimensions**: When prompted, enter the number of rows (H) and columns (W) of the grid, separated by a space. For example:
   ```
   Enter number of rows (H) and columns (W): 4 5
   ```

4. **Input the Grid Layout**: Enter each row of the grid layout, using '.' for empty squares and '#' for obstacles. For example:
   ```
   Enter row 1 of the grid: ..#..
   Enter row 2 of the grid: .#...
   Enter row 3 of the grid: ..#..
   Enter row 4 of the grid: .....
   ```

5. **View the Result**: After entering the grid layout, the application will calculate and display the maximum number of lighted squares:
   ```
   Maximum Lighted Squares: 8
   ```

## Example Usage

Here is an example of how the application might be used:

```
Enter number of rows (H) and columns (W): 3 3
Enter row 1 of the grid: ...
Enter row 2 of the grid: .#.
Enter row 3 of the grid: ...
Maximum Lighted Squares: 4
```

## Conclusion

The Lighted Squares application provides a simple yet effective way to determine the optimal placement of a lamp in a grid layout. By following the instructions above, users can easily install and run the application to solve their grid lighting problems.
```

This manual provides a comprehensive overview of the application, including its main functions, installation instructions, and usage guidelines. Let me know if you need any further modifications or additional information!