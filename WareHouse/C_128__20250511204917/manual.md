Here’s a detailed user manual for the Gomoku game application, formatted in Markdown as requested:

```markdown
# Gomoku Game

A simple command-line implementation of the classic Gomoku game, where two players take turns placing their marks on a 15x15 board. The first player to align five of their marks in a row (horizontally, vertically, or diagonally) wins the game.

## Quick Install

To run the Gomoku game, you need to have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

Once Python is installed, you can clone the repository or download the files directly. Make sure you have the following files in your project directory:

- `main.py`
- `gomoku.py`
- `cell.py`

## 🤔 What is Gomoku?

Gomoku is a traditional board game that is played on a grid. The objective is to be the first player to get five of their marks in a row. Players alternate turns, and the game can be played by two players.

## 📦 Dependencies

The Gomoku game does not require any external libraries beyond Python's standard library. Ensure you have Python 3.x installed.

## 🎮 How to Play

1. **Run the Game:**
   Open your terminal or command prompt, navigate to the directory where your game files are located, and run the following command:
   ```bash
   python main.py
   ```

2. **Game Instructions:**
   - The game will display the current state of the board, with empty cells represented by a dot (`.`).
   - Players are prompted to enter the row and column numbers (0-14) to place their marks (`X` for Player 1 and `O` for Player 2).
   - If a player attempts to place a mark in an already occupied cell, they will be prompted to try again.

3. **Winning the Game:**
   - The game checks for a win after each move. If a player aligns five marks in a row, a message will be displayed announcing the winner.
   - If the board is filled without any player winning, the game will declare a draw.

4. **Invalid Inputs:**
   - If a player enters an invalid row or column number, or if the input is not a number, the game will prompt them to enter valid inputs.

## 📖 Documentation

For further details on the game logic and implementation, you can refer to the source code in the `gomoku.py` and `cell.py` files. The main game logic is handled in the `GomokuGame` class, while the `Cell` class represents individual cells on the board.

### Game Logic Overview

- **Board Size:** The game is played on a 15x15 board.
- **Players:** Two players alternate turns, using `X` and `O`.
- **Winning Condition:** A player wins by placing five of their marks consecutively in any direction (horizontal, vertical, diagonal).

## Support

If you encounter any issues or have questions about the game, please feel free to reach out for support.

Happy gaming!
```

This manual provides a comprehensive overview of the Gomoku game, including installation instructions, gameplay details, and a brief explanation of the game logic. Let me know if you need any modifications or additional information!