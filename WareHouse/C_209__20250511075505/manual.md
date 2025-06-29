```markdown
# Gomoku Game

A simple implementation of the classic Gomoku game, also known as Five in a Row. This game allows two players to take turns placing their pieces on a 15x15 board, with the objective of being the first to align five of their pieces in a row, either horizontally, vertically, or diagonally.

## Main Functions

- **Command-Line Interface (CLI)**: Play the game in a terminal/command prompt.
- **Graphical User Interface (GUI)**: A simple GUI using tkinter (not fully implemented in this version).
- **Game Logic**: The game checks for valid moves, manages turns, and determines the winner.

## Installation

To run the Gomoku game, you need to have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

### Environment Dependencies

1. **Python**: Ensure you have Python 3.x installed.
2. **tkinter**: This library is included with most Python installations, but if you encounter issues, you may need to install it separately depending on your operating system.

### Installation Steps

1. Clone the repository or download the source code files (`main.py`, `gomoku_game.py`, and `gomoku_gui.py`).
2. Open your terminal or command prompt and navigate to the directory where the files are located.
3. Run the following command to start the game:

   ```bash
   python main.py
   ```

## How to Play

### Command-Line Interface (CLI)

1. After starting the game, you will be prompted to choose a game mode:
   - Enter `1` for Command-Line mode.
   - Enter `2` for GUI mode (not implemented in this version).
   - Enter `q` to quit the game.

2. In Command-Line mode:
   - The game board will be displayed in the terminal.
   - Players take turns entering their moves by specifying the row and column (0-14).
   - For example, entering `7 7` places a piece at row 7, column 7.
   - The game will announce the winner when a player aligns five pieces in a row.

3. If you want to play again after a game ends, you will be prompted to enter `y` or `n`.

### Graphical User Interface (GUI)

- The GUI is not fully implemented in this version. However, once implemented, it will allow players to click on the board to place their pieces visually.

## Game Rules

- Players alternate turns, starting with Player X.
- A valid move consists of placing a piece on an empty cell.
- The first player to align five pieces in a row (horizontally, vertically, or diagonally) wins the game.
- If a player attempts to make an invalid move (e.g., placing a piece on an occupied cell or outside the board), an error message will be displayed.

## Conclusion

Enjoy playing Gomoku! If you encounter any issues or have suggestions for improvements, please reach out to the development team.

```
