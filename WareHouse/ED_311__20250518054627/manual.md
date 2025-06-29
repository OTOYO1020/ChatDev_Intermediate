Here's a detailed user manual for the software, formatted in Markdown as requested:

```markdown
# Holeless Squares Counter

A Python application to count the number of holeless squares in a grid based on user-defined holed squares.

## Introduction

This software allows users to define a grid of specified height and width, mark certain squares as "holed," and then calculate the total number of holeless squares that can be formed within the grid. The application is designed to handle various edge cases, such as when there are no holed squares or when the grid is fully holed.

## Main Functions

1. **Grid Initialization**: Users can define the grid's height and width, as well as the coordinates of holed squares.
2. **Marking Holed Squares**: The application marks the specified squares as holed in the grid.
3. **Counting Holeless Squares**: The software iterates through the grid to count all possible holeless squares based on the marked holed squares.
4. **Input Parsing**: The application includes a utility function to parse user input for holed square coordinates.

## Installation

To run the application, you need to have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

### Environment Dependencies

You may need to install the following dependencies:

```bash
pip install typing
```

## How to Use

1. **Run the Application**: Execute the `main.py` file to start the application.

   ```bash
   python main.py
   ```

2. **Input Parameters**: When prompted, enter the following:
   - **Grid Height (H)**: The height of the grid (integer).
   - **Grid Width (W)**: The width of the grid (integer).
   - **Number of Holed Squares (N)**: The total number of holed squares (integer).
   - **Holed Squares**: Enter the coordinates of the holed squares in the format `(x,y)` separated by spaces. For example: `(0,1) (1,2) (2,3)`.

3. **View Results**: After entering the required information, the application will output the total number of holeless squares found in the grid.

### Example Usage

```
Enter Grid Height (H): 4
Enter Grid Width (W): 4
Enter Number of Holed Squares (N): 2
Enter Holed Squares (x,y) separated by space: (1,1) (2,2)
Total Holeless Squares: 10
```

## Edge Cases

- If **N** is 0, the application will calculate the total number of squares possible in the grid without any holes.
- If the grid is fully holed, the application will return 0 as there are no holeless squares.

## Troubleshooting

- Ensure that the coordinates for holed squares are within the bounds of the grid.
- If you encounter any errors, check the input format for holed squares and ensure it matches the expected format `(x,y)`.

## Conclusion

This application provides a straightforward way to analyze grids with holed squares and count the number of holeless squares. For any further assistance or feature requests, please contact the development team.

```

This manual provides a comprehensive overview of the software, including installation instructions, usage guidelines, and troubleshooting tips. It should help users effectively utilize the application.