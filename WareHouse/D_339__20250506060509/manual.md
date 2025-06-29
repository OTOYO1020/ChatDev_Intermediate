Here's the `manual.md` file for the grid meeting problem software:

```markdown
# Grid Meeting Problem

A Python application to solve the grid meeting problem where two players represented by 'P' must find the minimum number of moves to meet on an empty cell ('.') in a grid configuration.

## Quick Install

To run the application, ensure you have Python installed on your machine. You can install the required dependencies using pip:

```bash
pip install collections
```

## 🤔 What is this?

The Grid Meeting Problem application allows users to input a grid configuration and determine the minimum number of moves required for two players to meet. The grid consists of empty cells ('.'), obstacles ('#'), and players ('P'). The players can move in four directions (up, down, left, right) but cannot move through obstacles.

### Main Functions

- **Input Grid Size**: The application reads an integer `N` from standard input, representing the size of the grid (N x N).
- **Input Grid Configuration**: The application reads `N` strings representing the grid layout.
- **Player Location**: The application identifies the coordinates of the two players in the grid.
- **Breadth-First Search (BFS)**: The application implements a BFS algorithm to explore the grid and find the minimum moves required for both players to meet.

## How to Use

1. **Run the Application**: Execute the `main.py` file in your terminal or command prompt.

   ```bash
   python main.py
   ```

2. **Input the Grid Size**: When prompted, enter the size of the grid (N). For example, for a 5x5 grid, enter `5`.

3. **Input the Grid Configuration**: Enter `N` strings, each representing a row of the grid. Use 'P' for players, '.' for empty cells, and '#' for obstacles. For example:

   ```
   P....
   ..#..
   ..#..
   ....P
   ```

4. **View the Result**: The application will output the minimum number of moves required for both players to meet. If it is not possible for them to meet, it will output `-1`.

## Example

### Input

```
5
P....
..#..
..#..
....P
```

### Output

```
6
```

This indicates that it takes a minimum of 6 moves for both players to meet.

## 📖 Documentation

For more detailed information on the implementation and algorithms used, please refer to the source code in `main.py` and `grid.py`.

- **`main.py`**: The main application file that handles user input and output.
- **`grid.py`**: Contains the `Grid` class that implements the BFS logic for finding the meeting point.

Feel free to reach out for support or further inquiries regarding the application!
```

This manual provides a comprehensive overview of the software, including installation instructions, usage guidelines, and example inputs and outputs.