Here's a detailed user manual for the software, formatted in Markdown as requested:

```markdown
# Shortest Path Finder

A Python application designed to find the shortest path in a grid layout, allowing for teleportation between specific characters.

## Main Functions

- **Input Grid**: Users can input a grid layout where:
  - `#` represents walls (impassable).
  - `S` represents the starting position.
  - `G` represents the goal position.
  - Lowercase letters (`a` to `z`) represent teleportation points.

- **Find Shortest Path**: The application uses a breadth-first search (BFS) algorithm to explore the grid and find the shortest time to reach the goal from the start position, considering walls and teleportation.

## Installation

To run the application, you need to have Python installed on your system. Follow these steps to set up the environment:

1. **Install Python**: Download and install Python from [python.org](https://www.python.org/downloads/).

2. **Install Dependencies**: Open your terminal or command prompt and run the following command to install the required dependencies:

   ```bash
   pip install tkinter
   ```

   Note: `tkinter` is usually included with Python installations, but if you encounter issues, ensure it is installed.

## How to Use the Application

1. **Run the Application**: Navigate to the directory where the application files are located and run the following command:

   ```bash
   python main.py
   ```

2. **Input Grid Dimensions**:
   - Enter the height (H) and width (W) of the grid in the respective fields.

3. **Input the Grid**:
   - In the provided text area, input the grid layout. Each row should be on a new line. For example:
     ```
     S..#.
     ..#..
     ..#..
     ..#G.
     ```

4. **Find the Shortest Path**:
   - Click the "Find Shortest Path" button. The application will process the input and display the shortest time to reach the goal or indicate if the goal is unreachable.

5. **Error Handling**:
   - The application will show error messages if:
     - The grid dimensions do not match the specified height and width.
     - There are not exactly one `S` and one `G` in the grid.

## Example Usage

- **Input Example**:
  ```
  Height (H): 4
  Width (W): 5
  Grid:
  S..#.
  ..#..
  ..#..
  ..#G.
  ```

- **Output**:
  - The application will display the shortest time taken to reach `G` from `S`.

## Conclusion

The Shortest Path Finder application provides an intuitive interface for users to find paths in a grid layout with teleportation capabilities. For any issues or feature requests, please contact support.
```

This manual provides a comprehensive overview of the application, including its main functions, installation instructions, and usage guidelines. It should serve as a useful resource for users looking to utilize the software effectively.