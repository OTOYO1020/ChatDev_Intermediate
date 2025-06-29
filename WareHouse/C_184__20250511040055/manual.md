Here's a detailed user manual for the Gomoku game, formatted in Markdown as requested:

```markdown
# Gomoku Game

A simple implementation of the classic Gomoku game, also known as Five in a Row. This game allows two players to compete against each other by placing their markers on a 15x15 board.

## Quick Install

To run the Gomoku game, you need to have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

Once you have Python installed, you can clone the repository or download the files directly. Ensure you have the following files in the same directory:

- `gomoku.py`
- `main.py`

## 🤔 What is Gomoku?

Gomoku is a strategy board game for two players. The objective is to be the first to get an unbroken row of five pieces horizontally, vertically, or diagonally. Players take turns placing their markers (X or O) on the board.

## 🛠️ How to Install Environment Dependencies

No additional dependencies are required to run the Gomoku game. The game is implemented in pure Python and should work with any standard Python installation.

## 🎮 How to Play

1. **Start the Game**: Run the game by executing the `main.py` file. You can do this from the command line:
   ```bash
   python main.py
   ```

2. **Game Interface**: The game will display the current state of the board in the console. Empty cells are represented by a dot (.), player 1's moves by an X, and player 2's moves by an O.

3. **Making a Move**: Players take turns entering their moves. To make a move, input the row and column numbers separated by a space (e.g., `7 7` to place a marker in the center of the board).

4. **Winning the Game**: The game checks for a winner after each move. If a player successfully places five of their markers in a row (horizontally, vertically, or diagonally), the game will announce the winner.

5. **Exiting the Game**: To exit the game at any time, type `exit` and press Enter.

6. **Resetting the Game**: If you want to reset the game, you can call the `reset_game()` method from the command line interface, although this feature is not directly exposed in the current implementation.

## 📜 Game Rules

- The game is played on a 15x15 grid.
- Players alternate turns.
- The first player to align five of their markers in a row wins.
- If a player attempts to place a marker in an occupied cell or out of bounds, they will be prompted to try again.

## 📖 Documentation

For further details about the code structure and functions, you can refer to the comments within the `gomoku.py` and `main.py` files. The core logic of the game is encapsulated in the `GomokuGame` class, which handles the game state, player moves, and win condition checks.

Enjoy playing Gomoku!
```

This manual provides a comprehensive overview of the game, including installation instructions, gameplay mechanics, and rules. Let me know if you need any further modifications or additional information!