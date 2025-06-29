Here's a detailed user manual for the Gomoku game application, formatted in Markdown as requested:

```markdown
# Gomoku Game

A simple implementation of the classic Gomoku game, also known as Five in a Row. This application allows two players to compete against each other by placing their pieces on a 15x15 board.

## Main Functions

- **Start Game**: Initiates the game and allows players to take turns placing their pieces on the board.
- **Display Board**: Shows the current state of the board after each move.
- **Check Winner**: Determines if a player has won by placing five of their pieces in a row, either horizontally, vertically, or diagonally.
- **Draw Condition**: Checks if the board is full and declares a draw if no more moves can be made.

## Installation

To run the Gomoku game, you need to have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

### Environment Dependencies

This application does not require any additional dependencies beyond Python itself. However, ensure you have Python 3.x installed.

## How to Use/Play

1. **Clone the Repository**: If you haven't already, clone the repository containing the game files.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Run the Game**: Execute the `main.py` file to start the game.

   ```bash
   python main.py
   ```

3. **Gameplay Instructions**:
   - Players will take turns entering their moves.
   - Input your move as two integers separated by a space, representing the row and column (0-14).
   - For example, to place a piece in the first row and first column, type `0 0`.
   - The game will display the board after each move and announce if a player wins or if the game ends in a draw.

4. **End of Game**: The game will automatically end when a player wins or when the board is full. You can restart the game by running `main.py` again.

## Example Gameplay

```
Player X, enter your move (row and column): 
0 0
X| | | | | | | | | | | | | | 
-----------------------------
 | | | | | | | | | | | | | | 
-----------------------------
 | | | | | | | | | | | | | | 
-----------------------------
 | | | | | | | | | | | | | | 
-----------------------------
 | | | | | | | | | | | | | | 
-----------------------------
...
```

## Conclusion

Enjoy playing Gomoku! This simple yet engaging game is perfect for two players looking to challenge each other. If you encounter any issues or have suggestions for improvements, please reach out to the development team.
```

This manual provides a comprehensive overview of the Gomoku game, including its functionality, installation instructions, and gameplay guidance, ensuring users can easily understand and enjoy the application.