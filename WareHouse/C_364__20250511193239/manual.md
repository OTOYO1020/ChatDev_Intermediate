Here's a detailed user manual for the Gomoku game, formatted in Markdown as requested:

```markdown
# Gomoku Game

A simple implementation of the classic Gomoku game, also known as Five in a Row.

## Quick Install

To run the Gomoku game, you need to have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

Once you have Python installed, you can clone the repository or download the files directly. Make sure you have the following files in your project directory:

- `main.py`
- `board.py`
- `piece.py`

## 🤔 What is Gomoku?

Gomoku is a traditional board game played with two players. The objective is to be the first to get five of your pieces in a row, either horizontally, vertically, or diagonally.

## 📦 Dependencies

This game does not require any external libraries, as it is built using standard Python features. Just ensure you have Python 3.x installed.

## 🎮 How to Play

1. **Run the Game**: Open your terminal or command prompt, navigate to the directory where the game files are located, and run the following command:

   ```bash
   python main.py
   ```

2. **Game Interface**: The game will display a 15x15 board in the terminal. Empty cells are represented by a dot (`.`), black pieces by `B`, and white pieces by `W`.

3. **Making a Move**: Players take turns to place their pieces on the board. To make a move, enter the row and column numbers separated by a space (e.g., `7 7` to place a piece in the center of the board).

4. **Exiting the Game**: If you wish to quit the game at any time, type `exit` and press Enter.

5. **Winning the Game**: The game will automatically check for a winner after each move. If a player gets five pieces in a row, the game will announce the winner and display the final board.

6. **Draw Condition**: If the board is full and no player has won, the game will declare a draw.

## 🛠️ Example of Play

```
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
. . . . . . . . . . . . . . .
. . . . . . . . . . . . . . .
. . . . . . . . . . . . . . .
. . . . . . . . . . . . . . .
. . . . . . . . . . . . . . .
```

- Player 1 (Black) enters `7 7`
- Player 2 (White) enters `7 8`
- The game continues until a player wins or the board is full.

## 📖 Documentation

For further details on the game logic and code structure, you can refer to the source files:

- `main.py`: The main entry point for running the game.
- `board.py`: Contains the logic for the game board and piece placement.
- `piece.py`: Defines the Piece class used to represent the game pieces.

Feel free to modify and enhance the game as you see fit!
```

This manual provides a comprehensive overview of the Gomoku game, including installation instructions, gameplay mechanics, and a brief explanation of the code structure. Let me know if you need any further modifications or additional information!