Here's the user manual for the Gomoku game, formatted in Markdown as requested:

```markdown
# Gomoku Game

A simple implementation of the classic Gomoku game, also known as Five in a Row. This game can be played in a console or with a graphical user interface (GUI).

## Quick Install

To run the Gomoku game, you need to have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

Once you have Python installed, you can run the game without any additional dependencies. Just ensure you have the following files in the same directory:

- `main.py`
- `game.py`
- `gui.py` (optional for GUI version)

## 🤔 What is Gomoku?

Gomoku is a two-player board game in which players take turns placing their pieces (X and O) on a 15x15 grid. The objective is to be the first player to get five of their pieces in a row, either horizontally, vertically, or diagonally.

## 🛠️ How to Play

### Console Version

1. Open your terminal or command prompt.
2. Navigate to the directory where the game files are located.
3. Run the game by executing the following command:

   ```bash
   python main.py
   ```

4. Follow the on-screen instructions to enter your moves. You will be prompted to enter the row and column numbers separated by a space (e.g., `7 7` for the center of the board).
5. The game will display the board after each move, and it will announce the winner when one player gets five in a row.

### GUI Version

1. Ensure you have the same files as mentioned above.
2. Open your terminal or command prompt.
3. Navigate to the directory where the game files are located.
4. Run the GUI version of the game by executing the following command:

   ```bash
   python gui.py
   ```

5. A window will appear with the game board. Click on the cells to place your pieces.
6. The game will display a message box announcing the winner when one player gets five in a row.

## 🎮 Game Rules

- Players take turns placing their pieces on the board.
- The first player to align five of their pieces in a row (horizontally, vertically, or diagonally) wins the game.
- If a player tries to place a piece in an already occupied cell, a warning will be displayed.

## 📖 Documentation

For further information on the game logic and implementation, you can refer to the source code in the `game.py` and `gui.py` files. The game logic is encapsulated in the `GomokuGame` class, which handles moves, checks for winners, and manages the game state.

Enjoy playing Gomoku!
```

This manual provides a comprehensive overview of the Gomoku game, including installation instructions, gameplay details, and rules. Let me know if you need any further modifications or additional information!