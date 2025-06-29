Here's the `manual.md` file for the Gomoku game application:

```markdown
# Gomoku Game

A simple implementation of the classic Gomoku game, also known as Five in a Row.

## Quick Install

To run the Gomoku game, you need to have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

Once Python is installed, you can run the game directly without any additional dependencies. Just ensure you have the following files in the same directory:

- `main.py`
- `gomoku_logic.py`

## 🤔 What is Gomoku?

Gomoku is a traditional board game where two players take turns placing their stones (X and O) on a grid. The objective is to be the first to get five of your stones in a row, either horizontally, vertically, or diagonally.

## 🛠️ How to Play

1. **Start the Game**: Run the `main.py` file using the command line:
   ```bash
   python main.py
   ```

2. **Game Board**: The game board is a 15x15 grid. Each cell can be empty (represented by `.`), occupied by Player 1's stone (represented by `X`), or occupied by Player 2's stone (represented by `O`).

3. **Making a Move**: Players take turns entering their moves. When prompted, enter your move as two numbers separated by a space, representing the row and column (0-indexed). For example, to place a stone in the top-left corner, you would enter:
   ```
   0 0
   ```

4. **Winning the Game**: The game checks for a winner after each move. If a player gets five stones in a row, the game announces the winner.

5. **Draw Condition**: If the board is full and no player has won, the game will declare a draw.

6. **Playing Again**: After a game concludes, players will be prompted to play again. Enter `y` to start a new game or `n` to exit.

## 📖 Game Logic

The game logic is handled in the `gomoku_logic.py` file, which manages the game state, checks for winning conditions, and resets the board when needed.

### Key Functions:

- `place_stone(x, y, player)`: Places a stone for the current player at the specified coordinates.
- `is_winner(player)`: Checks if the specified player has won the game.
- `reset()`: Resets the game board for a new game.
- `is_board_full()`: Checks if the board is full, indicating a draw.

## 🎮 Enjoy Playing!

Have fun playing Gomoku! If you encounter any issues or have suggestions for improvements, feel free to reach out.
```

This manual provides a comprehensive overview of the Gomoku game, including installation instructions, gameplay mechanics, and a brief explanation of the game logic. Let me know if you need any further modifications or additional information!