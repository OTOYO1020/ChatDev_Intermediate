Here's the `manual.md` file for the Gomoku game, detailing the main functions, installation instructions, and how to play the game.

```markdown
# Gomoku Game

A simple implementation of the classic Gomoku game, also known as Five in a Row.

## 🎮 What is Gomoku?

Gomoku is a strategy board game for two players, where the objective is to be the first to get an unbroken row of five pieces horizontally, vertically, or diagonally on a 15x15 board. Players take turns placing their pieces on the board, with one player using "X" and the other using "O".

## 📦 Quick Install

To run the Gomoku game, you need to have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

### Clone the Repository

First, clone the repository containing the game files:

```bash
git clone <repository-url>
cd gomoku-game
```

### Install Dependencies

No additional dependencies are required for this basic version of the Gomoku game. Just ensure you have Python 3.x installed.

## 🛠️ How to Use / Play the Game

1. **Run the Game**: Open your terminal or command prompt, navigate to the directory where the game files are located, and run the following command:

    ```bash
    python main.py
    ```

2. **Game Instructions**:
   - The game board will be displayed in the terminal.
   - Players take turns entering their moves.
   - To make a move, enter the row and column numbers separated by a space (e.g., `7 7` to place a piece in the center of the board).
   - The valid range for row and column is from `0` to `14`.

3. **Winning the Game**:
   - The game will check for a winner after each move.
   - If a player gets five pieces in a row (horizontally, vertically, or diagonally), a message will be displayed announcing the winner.
   - If the board is full and no player has won, the game will declare a draw.

4. **Resetting the Game**: After a win or a draw, the game will automatically reset, and players can continue playing.

5. **Exiting the Game**: To exit the game at any time, you can press `Ctrl + C`.

## 📜 Game Features

- **Two-player Mode**: Play against another person.
- **Simple Interface**: The game is played in the terminal with a straightforward text-based interface.
- **Automatic Win Detection**: The game automatically checks for a winner after each move.

## 📖 Documentation

For more information about the game mechanics and code structure, you can refer to the source code in `main.py` and `board.py`.

Enjoy playing Gomoku!
```

This manual provides a comprehensive overview of the Gomoku game, including installation instructions, gameplay mechanics, and features. It should help users get started quickly and understand how to play the game effectively.