Here's a detailed user manual for the Gomoku game software, formatted in Markdown as requested:

```markdown
# Gomoku Game

A simple implementation of the classic Gomoku game, allowing two players to compete against each other either through a graphical user interface or in the command line.

## Main Functions

- **Two Player Mode**: Play against another player, taking turns to place their markers on the board.
- **Win Detection**: The game automatically checks for a winner after each move.
- **Reset Game**: Easily reset the game to start a new match.
- **Graphical User Interface**: Play using a user-friendly GUI built with Tkinter.
- **Command Line Interface**: Play through the terminal for a more traditional experience.

## Installation

To run the Gomoku game, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. **Install Python**: Make sure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **Install Tkinter**: Tkinter is usually included with Python installations. If you encounter issues, you can install it using:
   - For Windows: Tkinter is included with the standard Python installation.
   - For Linux: You may need to install it separately using your package manager, e.g., `sudo apt-get install python3-tk`.

3. **Clone the Repository**: Download the Gomoku game files from the repository or copy the provided code into your local directory.

4. **Run the Game**: Navigate to the directory containing the game files and run the following command:
   ```bash
   python main.py
   ```
   or, if you want to use the GUI version:
   ```bash
   python gomoku_gui.py
   ```

## How to Play

### Command Line Interface

1. When you run `main.py`, the game board will be displayed in the terminal.
2. Players take turns entering their moves by specifying the row and column (0-14).
3. The game will announce the winner when a player successfully places five of their markers in a row, either horizontally, vertically, or diagonally.
4. After a game ends, you will be prompted to continue playing or exit.

### Graphical User Interface

1. When you run `gomoku_gui.py`, a window will open displaying the game board.
2. Players take turns clicking on the cells to place their markers (X or O).
3. The status label will indicate whose turn it is and announce the winner when applicable.
4. Use the "Reset Game" button to start a new game at any time.

## Example Gameplay

- **Command Line**:
    ```
    Player X, enter your move row (0-14): 7
    Player X, enter your move column (0-14): 7
    ```

- **GUI**: Click on the cell at row 7, column 7 to place your marker.

## Conclusion

Enjoy playing Gomoku! This implementation provides both a command line and a graphical interface for a fun and engaging experience. If you encounter any issues or have suggestions for improvements, please reach out to the development team.
```

This manual provides a comprehensive overview of the Gomoku game, including installation instructions, gameplay mechanics, and how to run the game in both command line and GUI modes.