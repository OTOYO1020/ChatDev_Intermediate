Here's a detailed user manual for the software we developed, following the structure you provided:

```markdown
# Move Calculator

A Python application to calculate the minimum number of moves from a starting position to a target position based on specific movement rules.

## Quick Install

To run the Move Calculator, you need to have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

Once Python is installed, you can clone the repository or download the files directly. Ensure you have the required dependencies, which are included in the standard library.

## 🤔 What is this?

The Move Calculator is designed to determine the minimum number of moves required to reach a target position on a grid from a starting position. The movement rules allow for specific conditions that dictate how the moves can be made.

### Main Functions

- **min_moves(r1: int, c1: int, r2: int, c2: int) -> int**: 
  - Calculates the minimum number of moves from the starting position `(r1, c1)` to the target position `(r2, c2)`.
  - Returns `0` if the starting position is the same as the target position.
  - Determines if the target can be reached in one move based on defined movement rules.
  - If not reachable in one move, it uses a breadth-first search (BFS) algorithm to explore possible moves.

- **can_reach_in_one_move(r1: int, c1: int, r2: int, c2: int) -> bool**: 
  - Checks if the target position can be reached in a single move based on the movement rules.

- **bfs(r1: int, c1: int, r2: int, c2: int) -> int**: 
  - Implements the BFS algorithm to explore valid moves from the starting position to the target position.

## How to Use

1. **Run the Application**:
   - Open your terminal or command prompt.
   - Navigate to the directory where the `main.py` file is located.
   - Run the command:
     ```bash
     python main.py
     ```

2. **Input Handling**:
   - When prompted, enter the starting position and target position in the format:
     ```
     r1 c1 r2 c2
     ```
   - For example, to move from position (1, 2) to (3, 4), you would enter:
     ```
     1 2 3 4
     ```

3. **Output**:
   - The application will output the minimum number of moves required to reach the target position.

## Example

If you start at position (0, 0) and want to reach (2, 2), you would enter:
```
0 0 2 2
```
The application will calculate and display the minimum moves needed.

## Additional Notes

- The grid is defined within the range of 0 to 100 for both rows and columns.
- The application uses breadth-first search to ensure all possible moves are explored efficiently.
- Ensure that you do not enter positions outside the defined grid boundaries.

## Support

For any issues or feature requests, please contact our support team or refer to the documentation for further assistance.

```

This manual provides a comprehensive overview of the Move Calculator application, including installation instructions, usage guidelines, and examples to help users understand how to interact with the software effectively.