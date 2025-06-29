Here's a detailed user manual for the maze solver application, formatted in Markdown:

```markdown
# Maze Solver

A Python application to find the maximum number of moves between road squares in a maze using Breadth-First Search (BFS).

## Introduction

The Maze Solver application allows users to input a maze grid and calculates the maximum number of moves required to navigate between any two road squares (represented by '.') in the maze. The application utilizes the BFS algorithm to efficiently find the shortest paths between pairs of road squares.

## Main Functions

- **Input Maze Dimensions**: Users can specify the height (H) and width (W) of the maze.
- **Input Maze Grid**: Users can input the maze grid consisting of characters '.' (road) and '#' (wall).
- **Calculate Maximum Moves**: The application calculates the maximum number of moves required to reach from one road square to another.
- **Output Result**: The application prints the maximum number of moves found.

## Installation

To run the Maze Solver application, ensure you have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

### Environment Dependencies

This application requires the `collections` module, which is included in the Python standard library. No additional installations are necessary.

## How to Use

1. **Clone the Repository**: If you haven't already, clone the repository containing the application files.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Run the Application**: Execute the `main.py` file to start the application.

   ```bash
   python main.py
   ```

3. **Input Maze Dimensions**: When prompted, enter the dimensions of the maze (H and W) separated by a space.

   ```
   5 5
   ```

4. **Input Maze Grid**: Enter the maze grid line by line. Use '.' for road squares and '#' for walls. For example:

   ```
   .....
   .###.
   ..#..
   .###.
   .....
   ```

5. **View Output**: After entering the maze, the application will calculate and print the maximum number of moves required to navigate between road squares.

   ```
   Maximum moves: 6
   ```

## Example Usage

Here’s an example of how to input a maze:

```
Input:
5 5
.....
.###.
..#..
.###.
.....
```

Output:
```
Maximum moves: 6
```

## Conclusion

The Maze Solver application is a simple yet powerful tool for analyzing maze structures. By leveraging BFS, it efficiently computes the maximum moves required between road squares, making it a valuable resource for maze enthusiasts and developers alike.

For any issues or feature requests, please reach out to the support team.
```

This manual provides a comprehensive overview of the Maze Solver application, including installation instructions, usage guidelines, and examples. It is designed to help users understand how to effectively use the software.