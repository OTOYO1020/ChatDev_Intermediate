Here's a detailed user manual for the grid navigation application, formatted in Markdown:

```markdown
# Grid Navigation Application

A Python application for navigating a grid to find the shortest path from a starting point 'S' to a goal point 'G', while considering obstacles and lines of sight.

## Main Functions

- **Grid Representation**: The application allows users to input a grid of characters where:
  - `S` represents the starting point.
  - `G` represents the goal point.
  - `.` represents passable squares.
  - `#` represents impassable squares.
  - `>`, `<`, `v`, `^` represent people facing different directions, marking lines of sight as impassable.

- **Pathfinding**: The application uses a breadth-first search (BFS) algorithm to explore the grid and find the minimum number of moves required to reach the goal from the starting point.

- **User Interface**: A simple GUI built with Tkinter allows users to input grid dimensions and the grid itself, and to run the pathfinding algorithm with a button click.

## Installation

To run the Grid Navigation Application, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. **Install Python**: Download and install Python from [python.org](https://www.python.org/downloads/).

2. **Install Required Libraries**: Open your terminal or command prompt and run the following command to install the required libraries:
   ```bash
   pip install tkinter
   ```

## How to Use the Application

1. **Run the Application**: Execute the `main.py` file to start the application. You can do this by navigating to the directory containing `main.py` and running:
   ```bash
   python main.py
   ```

2. **Input Grid Dimensions**: In the GUI, enter the dimensions of the grid (H for height and W for width) in the format `H W`. For example, for a grid of 5 rows and 6 columns, you would enter:
   ```
   5 6
   ```

3. **Input the Grid**: In the text area provided, input the grid representation. Each row should contain exactly W characters. For example:
   ```
   S.....
   ..#...
   ..#..G
   ..#...
   ......
   ```

4. **Run the Algorithm**: Click the "Run" button to execute the pathfinding algorithm. The application will process the grid and display the result in a message box.

5. **View Results**: After running the algorithm, a message box will show either the minimum number of moves required to reach the goal or indicate that the goal is unreachable.

## Example Usage

1. **Input**:
   ```
   5 6
   S.....
   ..#...
   ..#..G
   ..#...
   ......
   ```

2. **Output**:
   ```
   Minimum moves: 6
   ```

## Troubleshooting

- **Input Errors**: If the number of lines entered does not match the specified height or if any line does not have the correct width, an error message will be displayed.

- **Unreachable Goal**: If the algorithm cannot find a path to the goal, a message will indicate that the goal is unreachable.

## Conclusion

The Grid Navigation Application is a powerful tool for visualizing and solving grid-based pathfinding problems. With its intuitive interface and robust algorithm, users can easily explore different grid configurations and find optimal paths.
```

This manual provides a comprehensive overview of the application, including its functionality, installation instructions, and usage guidelines.