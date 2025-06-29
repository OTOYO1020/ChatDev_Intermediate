Here's a detailed user manual for the basic Gomoku game, formatted in Markdown:

```markdown
# Gomoku Game

A simple implementation of the classic Gomoku game, allowing two players to compete against each other on a 15x15 board.

## Quick Install

To run the Gomoku game, ensure you have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

Once Python is installed, you can simply clone the repository or download the `main.py` file.

## 🤔 What is Gomoku?

Gomoku, also known as Five in a Row, is a strategy board game for two players. The objective is to be the first to get an unbroken row of five pieces horizontally, vertically, or diagonally.

## 🛠️ Requirements

This game requires no additional dependencies beyond Python itself. Ensure you have Python 3.x installed.

## 📖 How to Play

1. **Start the Game**: Run the game by executing the `main.py` file in your terminal or command prompt:
   ```bash
   python main.py
   ```

2. **Game Board**: The game board is a 15x15 grid. Players take turns placing their pieces ('X' and 'O') on the board.

3. **Making a Move**:
   - When prompted, enter the row and column numbers (0-14) where you want to place your piece.
   - Example: To place a piece in the first cell of the first row, enter `0` for the row and `0` for the column.

4. **Winning the Game**: The first player to align five of their pieces in a row (horizontally, vertically, or diagonally) wins the game.

5. **Draw Condition**: If the board is full and no player has won, the game ends in a draw.

6. **Invalid Moves**: If you attempt to place a piece in an already occupied cell, you will receive an "Invalid move!" message, and you will be prompted to make another move.

7. **Game Over**: When the game is over, the program will announce the winner or if the game is a draw.

8. **Resetting the Game**: If you want to play again, simply restart the program.

## 🎮 Example Gameplay

```
Player X, enter your move row (0-14): 0
Player X, enter your move column (0-14): 0
```

```
|X| | | | | | | | | | | | | | |
-------------------------------
| | | | | | | | | | | | | | | |
-------------------------------
| | | | | | | | | | | | | | | |
-------------------------------
...
```

## 📜 Additional Notes

- Ensure that your inputs are within the range of the board size (0-14).
- The game is played in the terminal, so make sure your terminal supports standard input and output.

## 📄 License

This Gomoku game is open-source and can be freely used and modified. Please refer to the repository for more details on licensing.

## 🤝 Support

If you encounter any issues or have questions about the game, feel free to reach out for support.

Enjoy playing Gomoku!
```

This manual provides a comprehensive overview of the Gomoku game, including installation instructions, gameplay mechanics, and additional notes for users.