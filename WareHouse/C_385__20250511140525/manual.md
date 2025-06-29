# Gomoku Game User Manual

Welcome to the Gomoku Game! This manual will guide you through the installation process, main functions of the game, and how to play.

## Quick Install

To run the Gomoku game, you need to have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

Once Python is installed, you can clone the repository or download the game files. There are no additional dependencies required for this game, so you can run it directly.

## What is Gomoku?

Gomoku, also known as Five in a Row, is a classic board game where two players take turns placing their pieces (X and O) on a grid. The objective is to be the first player to get five of their pieces in a row, either horizontally, vertically, or diagonally.

## Main Functions of the Software

### 1. Game Initialization
- The game initializes a 15x15 board.
- Player 1 starts the game.

### 2. Board Display
- The current state of the board is printed after each move.

### 3. Player Moves
- Players enter their moves in the format "x y", where x is the column and y is the row.
- Players can reset the game at any time by entering 'r'.

### 4. Win and Draw Conditions
- The game checks for a winner after each move.
- If all cells are filled without a winner, the game declares a draw.

### 5. Reset Game
- Players can reset the game to start over at any time.

## How to Play

1. **Start the Game**: Run the `main.py` file using Python.
   ```bash
   python main.py
   ```

2. **Make a Move**: Enter your move in the format "x y". For example, to place a piece in the first column and first row, you would enter:
   ```
   0 0
   ```

3. **Reset the Game**: If you wish to reset the game at any point, simply type:
   ```
   r
   ```

4. **Winning the Game**: The game will announce the winner when a player successfully places five of their pieces in a row. If the board is full and no player has won, the game will declare a draw.

5. **Play Again**: After a game ends, you will be prompted to play again. Enter 'y' to continue or 'n' to exit.

## Example of Gameplay

```
Enter your move (x y) or 'r' to reset: 0 0
X |   |   |   |   |   |   |   |   |   |   |   |   |   |  
---------------------------------------------------------
  |   |   |   |   |   |   |   |   |   |   |   |   |   |  
---------------------------------------------------------
  |   |   |   |   |   |   |   |   |   |   |   |   |   |  
---------------------------------------------------------
...
```

## Conclusion

Enjoy playing Gomoku! If you have any questions or feedback, feel free to reach out. Happy gaming!