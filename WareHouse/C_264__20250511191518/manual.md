Here's the user manual for the Gomoku game software, formatted in Markdown:

```markdown
# Gomoku Game

A simple and interactive Gomoku game implemented in Python.

## Quick Install

To run the Gomoku game, you need to have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

Once Python is installed, you can clone the repository or download the files directly. Ensure you have the Tkinter library, which is included with most Python installations. If you encounter any issues, you can install it using:

```bash
sudo apt-get install python3-tk  # For Ubuntu/Debian
```

## 🤔 What is Gomoku?

Gomoku, also known as Five in a Row, is a board game where two players take turns placing their markers (X and O) on a 15x15 grid. The objective is to be the first to get five of your markers in a row, either horizontally, vertically, or diagonally.

## 📖 Main Functions

### Game Logic

- **GomokuGame Class**: Contains the core logic for managing the game state, including:
  - `make_move(row, col)`: Places a marker on the board.
  - `check_winner(row, col)`: Checks if the current move resulted in a win.
  - `reset_game()`: Resets the game to its initial state.
  - `print_board()`: Displays the current state of the board in the console.

### Graphical User Interface (GUI)

- **GomokuGUI Class**: Provides a graphical interface for the game using Tkinter, including:
  - A 15x15 grid of buttons representing the game board.
  - A status label indicating the current player or the winner.
  - A reset button to start a new game.

### Main Entry Point

- **main.py**: The main script to run the game in console mode. It allows players to make moves via command line input.

## How to Play

### Using the GUI

1. Run the GUI application by executing:
   ```bash
   python gomoku_gui.py
   ```
2. The game window will open, displaying the board and the current player.
3. Click on a cell to place your marker (X or O). The game alternates turns between the two players.
4. If a player wins, a message will display indicating the winner. If the board is full and no player has won, it will declare a draw.
5. Click the "Reset Game" button to start a new game.

### Using the Console

1. Run the console application by executing:
   ```bash
   python main.py
   ```
2. The current state of the board will be printed in the console.
3. Enter 'reset' to reset the game or 'move' to make a move.
4. Input the row and column numbers (0-14) to place your marker.
5. The game will announce the winner or a draw when applicable.

## Conclusion

Enjoy playing Gomoku! If you have any questions or need further assistance, feel free to reach out.
```

This manual provides a comprehensive overview of the Gomoku game, including installation instructions, gameplay mechanics, and usage of both the GUI and console versions.