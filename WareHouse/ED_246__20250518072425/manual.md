```markdown
# Bishop Movement Application

This application allows users to calculate the minimum number of moves required for a bishop to move from a starting position to a target position on a chessboard, while adhering to chess movement rules.

## Main Functions

- **min_moves_bishop(N: int, A_x: int, A_y: int, B_x: int, B_y: int, S: List[str]) -> int**: 
  - This function calculates the minimum number of moves for a bishop to reach the target position from the starting position on an N x N chessboard.
  - It validates the bishop's movement according to chess rules, ensuring it can only move to empty squares and not through occupied squares (pawns).
  - Returns the minimum number of moves required or `-1` if the target position is unreachable.

## Installation

To run the Bishop Movement Application, you need to have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

### Environment Dependencies

You may need to install the following dependencies:

```bash
pip install collections
```

## How to Use the Application

1. **Clone the Repository**: 
   - Clone the repository containing the application files to your local machine.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Run the Application**:
   - Navigate to the directory containing the `main.py` file.
   - Open a terminal and run the following command:

   ```bash
   python main.py
   ```

3. **Modify Input Parameters**:
   - You can modify the input parameters in the `main.py` file to test different scenarios. 
   - The parameters include:
     - `N`: Size of the chessboard (e.g., 8 for an 8x8 board).
     - `A_x`, `A_y`: Starting position of the bishop (0-indexed).
     - `B_x`, `B_y`: Target position of the bishop (0-indexed).
     - `S`: Board configuration represented as a list of strings, where each string represents a row of the chessboard. Use '.' for empty squares and 'P' for pawns.

4. **Example Input**:
   - The default input in `main.py` is set to an 8x8 empty chessboard with the bishop starting at (0, 0) and the target at (7, 7).

```python
N = 8
A_x, A_y = 0, 0  # Starting position
B_x, B_y = 7, 7  # Target position
S = [
    "........",
    "........",
    "........",
    "........",
    "........",
    "........",
    "........",
    "........"
]  # Board configuration
```

5. **Output**:
   - The program will print the minimum number of moves required for the bishop to reach the target position or `-1` if it is unreachable.

## Testing

You can test the function with various input scenarios by modifying the board configuration and positions in the `main.py` file. Ensure to check edge cases, such as blocked paths and immediate reachability.

## Conclusion

This application provides a straightforward way to calculate the bishop's movement on a chessboard while adhering to chess rules. Feel free to explore and modify the code to suit your needs!
```