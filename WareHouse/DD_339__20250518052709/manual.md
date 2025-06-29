```markdown
# Minimum Moves Game

A grid-based game where two players navigate through a grid to find the minimum moves required to meet at the same cell.

## Main Functions

The main function of this software is to determine the minimum number of moves required for two players to meet on a grid. The players are represented by '1' and '2', while empty cells are represented by '.'. The function handles various scenarios, including adjacent starting positions and obstacles.

### Key Features:
- **Grid Input**: Accepts a grid size and layout as input.
- **BFS Algorithm**: Utilizes a breadth-first search algorithm to explore possible moves for both players.
- **Move Tracking**: Tracks the number of moves taken for each player to reach each cell.
- **Edge Case Handling**: Manages scenarios where players start adjacent to each other or are blocked by obstacles.

## Installation

To run the application, ensure you have Python installed on your system. You can install the required dependencies using pip:

```bash
pip install collections
```

## How to Use/Play

1. **Run the Application**: Execute the `main.py` file in your terminal or command prompt.

   ```bash
   python main.py
   ```

2. **Input Grid Size**: When prompted, enter the size of the grid (N). For example, for a 5x5 grid, enter `5`.

3. **Input Grid Layout**: Enter the grid layout row by row. Each row should be a string containing characters '1', '2', and '.' only. For example:

   ```
   .....
   ..1..
   ..2..
   .....
   .....
   ```

4. **View Result**: After entering the grid, the application will output the minimum moves required for both players to meet. If it's impossible for them to meet, it will return `-1`.

### Example Input/Output

**Input:**
```
Enter grid size (N): 5
Enter grid (each row as a string):
.....
..1..
..2..
.....
.....
```

**Output:**
```
Minimum Moves: 1
```

## Error Handling

The application includes error handling for the following scenarios:
- If the grid size does not match the number of rows provided.
- If the grid contains invalid characters (anything other than '.', '1', or '2').

In case of an error, a message will be printed to the standard error output.

## Conclusion

This software provides a simple yet effective way to determine the minimum moves for two players on a grid. It is designed to be user-friendly and robust, handling various edge cases to ensure accurate results.
```