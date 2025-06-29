Here's the user manual for the Gomoku game, formatted in Markdown:

```markdown
# Gomoku Game

A simple implementation of the classic Gomoku game, playable both in a console and with a graphical user interface (GUI) using Tkinter.

## Main Functions

- **Play the Game**: Players take turns placing their pieces (X and O) on a 15x15 board.
- **Win Condition**: The first player to align five of their pieces horizontally, vertically, or diagonally wins the game.
- **Reset Game**: Players can reset the game at any time to start over.

## Installation

To run the Gomoku game, you need to have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Environment Dependencies

You will need the Tkinter library for the GUI version. Tkinter is included with most Python installations. If you encounter any issues, you can install it using the following command:

```bash
pip install tk
```

## How to Use/Play the Game

### Console Version

1. **Run the Game**: Open your terminal and navigate to the directory where `main.py` is located. Run the following command:

   ```bash
   python main.py
   ```

2. **Make Moves**: Players will be prompted to enter their moves by specifying the row and column (0-14). For example, entering `7` for row and `8` for column places a piece in the cell at (7, 8).

3. **Winning the Game**: The game will announce when a player has won after making a valid move.

4. **Play Again**: After a game ends, players will be asked if they want to play again. Enter `y` to continue or `n` to exit.

### GUI Version

1. **Run the Game**: Open your terminal and navigate to the directory where `gomoku_gui.py` is located. Run the following command:

   ```bash
   python gomoku_gui.py
   ```

2. **Game Interface**: A window will open displaying the Gomoku board. Players can click on the buttons to place their pieces.

3. **Current Player**: The current player is displayed at the top of the window. The game alternates between players X and O.

4. **Winning the Game**: When a player wins, a message will be displayed indicating the winner.

5. **Reset Game**: Click the "Reset Game" button to start a new game at any time.

## Conclusion

Enjoy playing Gomoku! If you have any questions or feedback, feel free to reach out to our support team.
```

This manual provides a comprehensive overview of the Gomoku game, including installation instructions, gameplay mechanics, and how to run both the console and GUI versions.