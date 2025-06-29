Here's a detailed user manual for the Gomoku game, formatted in Markdown as requested:

```markdown
# Gomoku Game

A simple command-line implementation of the classic Gomoku game, where two players take turns placing their marks on a 15x15 board. The first player to align five of their marks horizontally, vertically, or diagonally wins the game.

## Quick Install

To run the Gomoku game, ensure you have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

Once Python is installed, you can run the game directly from the source code provided.

## 🤔 What is Gomoku?

Gomoku, also known as Five in a Row, is a traditional board game that is played on a grid. Players take turns placing their marks (X or O) on the board, and the objective is to be the first to get five of their marks in a row, either horizontally, vertically, or diagonally.

## 🛠️ How to Set Up the Environment

1. **Install Python**: Make sure you have Python 3.x installed. You can verify this by running the following command in your terminal or command prompt:

   ```bash
   python --version
   ```

2. **Download the Game Code**: Copy the provided code into a file named `main.py`.

3. **Run the Game**: Open your terminal or command prompt, navigate to the directory where `main.py` is located, and run the following command:

   ```bash
   python main.py
   ```

## 🎮 How to Play

1. **Starting the Game**: When you run the game, the board will be displayed, and it will be Player X's turn to make a move.

2. **Making a Move**: Players take turns entering their moves. To make a move, input the row and column indices separated by a space (e.g., `7 7` to place a mark in the center of the board).

3. **Valid Moves**: 
   - Ensure that the cell you are trying to occupy is empty. If the cell is already occupied, you will receive feedback indicating that the move is invalid.
   - The indices must be within the range of the board size (0 to 14).

4. **Winning the Game**: The game will check for a winning condition after each move. If a player aligns five marks in a row, a message will be displayed indicating that the player has won.

5. **Draw Condition**: If the board is completely filled without any player winning, the game will declare a draw.

6. **Resetting the Game**: If you wish to play again, you can restart the game by running the `main.py` file again.

## 📜 Game Rules

- Players alternate turns, starting with Player X.
- The game is played on a 15x15 grid.
- The first player to get five of their marks in a row wins.
- If all cells are filled and no player has won, the game ends in a draw.

## 📞 Support

For any issues or questions regarding the game, please reach out to our support team at support@chatdev.com.

Enjoy playing Gomoku!
```

This manual provides a comprehensive guide for users to understand the game, set it up, and play effectively. Let me know if you need any modifications or additional information!