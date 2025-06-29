Here is the `manual.md` file for the lighted squares calculation application:

```markdown
# Lighted Squares Calculation Application

This application calculates the maximum number of squares that can be lighted by placing a lamp optimally on a grid. The grid is defined by empty squares ('.') and obstacles ('#'). 

## Main Functions

- **Input Handling**: The application reads the dimensions of the grid and the grid layout from the user.
- **Light Count Calculation**: It calculates how many squares can be lighted from each position in the grid, both horizontally and vertically.
- **Maximum Lighted Squares**: It determines the maximum number of squares that can be lighted by placing a lamp on an optimal position.
- **Output**: The application outputs the maximum number of lighted squares.

## Installation

To run the application, you need to have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Environment Dependencies

This application does not require any external libraries beyond the standard Python library. However, ensure that you have Python 3.x installed.

## How to Use the Application

1. **Clone the Repository**: If you haven't already, clone the repository containing the application files.
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Run the Application**: Execute the main application file.
   ```bash
   python main.py
   ```

3. **Input the Grid Dimensions**: When prompted, enter the number of rows (H) and columns (W) for the grid.
   ```
   Enter number of rows (H): 3
   Enter number of columns (W): 5
   ```

4. **Input the Grid Layout**: Enter the grid layout using '#' for obstacles and '.' for empty squares. For example:
   ```
   Enter grid layout (use '#' for obstacles and '.' for empty squares):
   ..#..
   .#...
   ....#
   ```

5. **View the Result**: After entering the grid layout, the application will calculate and display the maximum number of lighted squares.
   ```
   Maximum lighted squares: 7
   ```

## Example

Here’s a quick example of how to use the application:

1. Start the application.
2. Input:
   ```
   Enter number of rows (H): 4
   Enter number of columns (W): 5
   Enter grid layout (use '#' for obstacles and '.' for empty squares):
   .....
   .#...
   ..#..
   .....
   ```
3. Output:
   ```
   Maximum lighted squares: 8
   ```

## Error Handling

The application includes error handling for the following scenarios:
- If the grid dimensions do not match the input.
- If the grid contains characters other than '#' and '.'.

In case of an error, an appropriate message will be displayed.

## Conclusion

This application provides a simple yet effective way to calculate the maximum number of lighted squares in a grid. It is designed for ease of use and can be run in any environment that supports Python. Enjoy exploring different grid configurations and their lighting possibilities!
```

This user manual provides a comprehensive overview of the application, including its main functions, installation instructions, usage guidelines, and error handling.