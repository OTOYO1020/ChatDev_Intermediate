Here's a detailed user manual for the ice square exploration application, formatted in Markdown:

```markdown
# Ice Square Exploration Application

Explore the grid of ice squares and discover how many unique squares you can touch!

## Overview

This application allows users to navigate a grid representing ice squares and rocks. The player starts at a specific position and can move in four directions (up, down, left, right) until they hit a rock or the edge of the grid. The goal is to count the number of unique ice squares that can be reached from the starting position.

## Main Functions

- **Grid Initialization**: The application reads the dimensions of the grid and the layout, initializing the grid for exploration.
- **Movement Logic**: The player can move in four directions, and the application checks for reachable ice squares.
- **Exploration**: Starting from a specified position, the application explores all reachable ice squares and counts them.
- **Output**: The application prints the total number of unique ice squares that can be touched.

## Installation

To run the Ice Square Exploration Application, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. **Install Python**: Ensure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: If you have the source code in a repository, clone it to your local machine using:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

3. **Install Dependencies**: The application uses the `collections` module, which is part of the Python standard library, so no additional dependencies are required.

## How to Use the Application

1. **Run the Application**: Open your terminal or command prompt and navigate to the directory where the application files are located. Run the following command:
   ```bash
   python main.py
   ```

2. **Input the Grid Dimensions**: When prompted, enter the dimensions of the grid (N and M) as two integers separated by a space. For example:
   ```
   5 5
   ```

3. **Input the Grid Layout**: Next, input the grid layout as N strings, each of length M. Use `.` to represent ice squares and `#` to represent rocks. For example:
   ```
   .....
   ..#..
   ..#..
   ..#..
   .....
   ```

4. **View the Result**: After entering the grid layout, the application will process the input and print the count of reachable ice squares.

## Example

Here’s an example of how to run the application:

```bash
$ python main.py
5 5
.....
..#..
..#..
..#..
.....
```

**Output:**
```
13
```

This indicates that there are 13 unique ice squares that can be touched starting from the position (2, 2).

## Conclusion

The Ice Square Exploration Application provides an engaging way to explore grid-based navigation and counting. Feel free to modify the grid layout and experiment with different configurations to see how many ice squares you can reach!

For any questions or support, please contact the development team.
```

This manual provides a comprehensive guide for users to understand the application, its functionalities, installation steps, and usage instructions.