Here's a detailed user manual for the chess application, formatted in Markdown:

```markdown
# Chess Application

A simple application to simulate the movement of a bishop on a chessboard using breadth-first search (BFS) to find the minimum number of moves from a starting position to a target position.

## Main Functions

- **Input Chessboard Size**: The application allows users to input the size of the chessboard (N x N).
- **Input Chessboard Rows**: Users can input N strings representing the rows of the chessboard, where 'P' represents a pawn that blocks the bishop's movement.
- **Input Starting and Target Positions**: Users can specify the starting and target positions of the bishop in zero-based format.
- **BFS Algorithm**: The application uses a breadth-first search algorithm to calculate the minimum number of moves required for the bishop to reach the target position, considering the obstacles on the board.

## Installation

To run the chess application, you need to have Python installed on your system. Follow these steps to set up the environment:

1. **Install Python**: Make sure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: If you have the source code in a repository, clone it to your local machine. If not, create two files named `main.py` and `chessboard.py` and copy the provided code into them.

3. **Install Required Dependencies**: The application uses the `collections` module, which is included in the Python standard library, so no additional installations are required.

## How to Use the Application

1. **Run the Application**: Open a terminal or command prompt, navigate to the directory where `main.py` is located, and run the following command:
   ```bash
   python main.py
   ```

2. **Input the Chessboard Size**: When prompted, enter a positive integer for the size of the chessboard (e.g., `8` for an 8x8 chessboard).

3. **Input the Chessboard Rows**: Enter N strings, each containing exactly N characters. Use 'P' to represent pawns. For example:
   ```
   Enter Row 1 (must be 8 characters long): ........
   Enter Row 2 (must be 8 characters long): ..P.....
   Enter Row 3 (must be 8 characters long): ........
   Enter Row 4 (must be 8 characters long): ........
   Enter Row 5 (must be 8 characters long): ..P.....
   Enter Row 6 (must be 8 characters long): ........
   Enter Row 7 (must be 8 characters long): ........
   Enter Row 8 (must be 8 characters long): ........
   ```

4. **Input the Starting Position**: Enter the starting position of the bishop in zero-based format (e.g., `0,0` for the top-left corner).

5. **Input the Target Position**: Enter the target position of the bishop in zero-based format (e.g., `1,1` for the second square).

6. **View the Result**: The application will output the minimum number of moves required for the bishop to reach the target position or `-1` if it is not possible.

## Example Usage

```
Enter Chessboard Size (N): 8
Enter Row 1 (must be 8 characters long): ........
Enter Row 2 (must be 8 characters long): ..P.....
Enter Row 3 (must be 8 characters long): ........
Enter Row 4 (must be 8 characters long): ........
Enter Row 5 (must be 8 characters long): ..P.....
Enter Row 6 (must be 8 characters long): ........
Enter Row 7 (must be 8 characters long): ........
Enter Row 8 (must be 8 characters long): ........
Enter Starting Position (Ax, Ay) in zero-based format (e.g., 0,0 for top-left): 0,0
Enter Target Position (Bx, By) in zero-based format (e.g., 1,1 for second square): 1,1
Minimum Moves: 1
```

## Conclusion

This chess application provides a straightforward way to simulate the movement of a bishop on a chessboard while considering obstacles. By following the instructions above, users can easily set up and run the application to explore different chessboard configurations and bishop movements.
```

This manual provides clear instructions on how to install and use the chess application, ensuring that users can easily navigate through the functionalities offered.