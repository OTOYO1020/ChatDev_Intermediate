```markdown
# Gomoku Game

A simple console-based Gomoku game implemented in Python.

## Introduction

Gomoku, also known as Five in a Row, is a classic board game where two players take turns placing their marks (X and O) on a 15x15 grid. The objective is to be the first to get five of your marks in a row, either horizontally, vertically, or diagonally.

This application allows you to play Gomoku in a console environment, providing a straightforward interface for two players to compete against each other.

## Main Functions

- **Start a New Game**: The game starts with an empty board, and players take turns making moves.
- **Display Board**: The current state of the board is displayed after each move.
- **Check for Winner**: The game checks for a winner after each move, announcing the winner if one is found.
- **Replay Option**: After a game concludes, players are prompted to play again or exit.

## Installation

To run the Gomoku game, you need to have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Environment Dependencies

Currently, there are no additional dependencies required for this game. However, ensure you have Python 3.x installed.

## How to Use/Play

1. **Clone the Repository**: If you have the code in a repository, clone it to your local machine. If you have the files, ensure they are in the same directory.

2. **Navigate to the Directory**: Open your terminal or command prompt and navigate to the directory where the game files are located.

3. **Run the Game**: Execute the following command to start the game:
   ```bash
   python main.py
   ```

4. **Make Moves**: Players will be prompted to enter their moves in the format `row column` (e.g., `7 7` for the center of the board). Ensure that the coordinates are between 0 and 14.

5. **Winning the Game**: The game will automatically check for a winner after each move. If a player wins, their name will be displayed.

6. **Replay Option**: After a game ends, you will be asked if you want to play again. Enter `y` to continue or `n` to exit.

## Example of Gameplay

```
Player X, enter your move (row and column): 7 7
. . . . . . . . . . . . . . .
. . . . . . . . . . . . . . .
. . . . . . . . . . . . . . .
. . . . . . . . . . . . . . .
. . . . X . . . . . . . . . .
. . . . . . . . . . . . . . .
. . . . . . . . . . . . . . .
. . . . . . . . . . . . . . .
. . . . . . . . . . . . . . .
. . . . . . . . . . . . . . .
. . . . . . . . . . . . . . .
. . . . . . . . . . . . . . .
. . . . . . . . . . . . . . .
. . . . . . . . . . . . . . .
. . . . . . . . . . . . . . .
Player X's turn
```

## Conclusion

Enjoy playing Gomoku! If you encounter any issues or have suggestions for improvements, feel free to reach out for support.
```