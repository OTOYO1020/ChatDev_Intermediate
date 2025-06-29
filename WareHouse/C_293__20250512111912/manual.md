Here's a detailed user manual for the software that counts distinct paths in a grid, formatted in Markdown as requested:

```markdown
# Distinct Path Counter

A Python application for counting distinct paths in a grid, ensuring that all values in the path are unique.

## Overview

This application allows users to input a grid of integers and calculates the number of distinct paths from the top-left corner to the bottom-right corner of the grid. A path is considered distinct if all integers in the path are unique.

## Main Functions

- **count_happy_paths(H: int, W: int, A: List[List[int]]) -> int**: This function encapsulates the logic for counting distinct paths in the grid. It takes the height and width of the grid along with the grid values as input and returns the total count of valid distinct paths.

- **is_distinct_path(path: List[int]) -> bool**: A helper function that checks if all integers in the current path are distinct.

- **find_paths(i: int, j: int, path: List[int])**: A recursive function that explores all possible paths from the current position (i, j) to the destination (H, W). It utilizes memoization to optimize performance.

## Installation

To run this application, you need to have Python installed on your system. Follow these steps to set up the environment:

1. **Install Python**: Make sure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **Install Required Dependencies**: This application uses the built-in `typing` module, which is included in Python 3.5 and later. No additional packages are required.

## How to Use

1. **Run the Application**: Open your terminal or command prompt and navigate to the directory where the `main.py` file is located.

2. **Input Grid Dimensions**: When prompted, enter the height (H) and width (W) of the grid.

3. **Input Grid Values**: Enter the grid values row by row, separating each integer with a comma. For example:
   ```
   1,2,3
   4,5,6
   7,8,9
   ```

4. **View Results**: After entering the grid, the application will calculate and display the number of distinct paths from the top-left to the bottom-right corner.

## Example Usage

```bash
$ python main.py
Enter Height (H): 3
Enter Width (W): 3
Enter Grid values (comma-separated rows):
1,2,3
4,5,6
7,8,9
Distinct Paths: 6
```

## Error Handling

The application includes basic error handling. If the input does not match the expected format or dimensions, an error message will be displayed. Ensure that the number of integers in each row matches the specified width.

## Conclusion

This application provides a straightforward way to count distinct paths in a grid. It can be useful for educational purposes, algorithm practice, or as a component in larger applications that require pathfinding capabilities.

For any further questions or support, please contact the development team.
```

This manual provides a comprehensive guide for users to understand the functionality, installation, and usage of the distinct path counting application.