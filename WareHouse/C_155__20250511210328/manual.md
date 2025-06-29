# Gomoku Game User Manual

## Introduction

Welcome to the Gomoku Game! This application allows you to play the classic board game Gomoku, also known as Five in a Row. You can choose to play in console mode or graphical user interface (GUI) mode. The objective of the game is to be the first player to get five of your pieces in a row, either horizontally, vertically, or diagonally.

## Main Functions

- **Game Logic**: The `GomokuGame` class handles all the game logic, including making moves, checking for a winner, and resetting the game.
- **Graphical User Interface**: The `GomokuGUI` class provides a user-friendly interface for playing the game with visual feedback.
- **Console Mode**: The application allows you to play in a text-based console mode for a more traditional experience.

## Installation

To run the Gomoku game, you need to have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

### Environment Dependencies

You will need the `tkinter` library for the GUI mode. It usually comes pre-installed with Python. If you encounter any issues, you can install it using the following command:

```bash
pip install tk
```

### Clone the Repository

Clone the repository containing the Gomoku game code:

```bash
git clone <repository-url>
cd gomoku-game
```

## How to Use/Play

### Running the Game

1. **Navigate to the Game Directory**: Open your terminal or command prompt and navigate to the directory where the game files are located.

2. **Start the Game**: Run the main application file:

   ```bash
   python main.py
   ```

3. **Choose Your Mode**: You will be prompted to choose your mode:
   - Enter `1` for Console mode.
   - Enter `2` for GUI mode.

### Playing in Console Mode

- After selecting Console mode, the game board will be displayed in the terminal.
- Players will take turns entering their moves by specifying the row and column numbers (0-indexed).
- The game will continue until one player wins or the board is full.

### Playing in GUI Mode

- After selecting GUI mode, a window will open displaying the game board.
- Click on the cells to place your pieces (X or O).
- The current player's turn will be displayed at the top.
- You can reset the game at any time by clicking the "Reset Game" button.

### Game Rules

- Players take turns placing their pieces on the board.
- The first player to align five pieces in a row (horizontally, vertically, or diagonally) wins the game.
- If a player attempts to place a piece in an already occupied cell, an error message will be displayed.

## Conclusion

Enjoy playing Gomoku! Whether you prefer the simplicity of the console or the interactivity of the GUI, this game offers a fun way to challenge your friends or practice your skills. If you have any questions or feedback, feel free to reach out!