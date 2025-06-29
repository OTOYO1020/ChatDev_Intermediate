Here's a detailed user manual for the Gomoku game application, formatted in Markdown:

```markdown
# Gomoku Game

A simple implementation of the classic Gomoku game, also known as Five in a Row. This application allows two players to take turns placing their pieces on a 15x15 board, with the goal of being the first to align five pieces in a row, either horizontally, vertically, or diagonally.

## Quick Install

To run the Gomoku game, you need to have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

Once you have Python installed, you can run the game without any additional dependencies. Simply clone or download the repository containing the game files.

## 🤔 What is Gomoku?

Gomoku is a traditional board game that is played on a grid. The objective is to be the first player to get five of their pieces in a row. Players take turns placing their pieces on the board, and the game ends when one player wins or when the board is completely filled, resulting in a draw.

## 📦 How to Install and Run the Game

1. **Clone or Download the Repository:**
   You can clone the repository using Git or download the ZIP file from the repository page.

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Game Directory:**
   Open your terminal or command prompt and navigate to the directory where the game files are located.

   ```bash
   cd path/to/gomoku
   ```

3. **Run the Game:**
   Execute the main game file using Python.

   ```bash
   python main.py
   ```

## 🎮 How to Play

1. **Starting the Game:**
   When you run the game, it will announce that a new game has started and that Player X goes first.

2. **Making a Move:**
   Players take turns entering the coordinates of the cell where they want to place their piece. The coordinates should be in the format `row column`, where both row and column are integers between 0 and 14 (inclusive).

   Example input:
   ```
   Enter row and column (0-14) separated by space: 7 7
   ```

3. **Game Rules:**
   - Players alternate turns, with Player X starting first.
   - If a player tries to place a piece in an already occupied cell, they will be prompted to choose another cell.
   - The game checks for a winner after each move. If a player aligns five pieces in a row, they win the game.
   - If the board is completely filled without a winner, the game ends in a draw.

4. **Ending the Game:**
   When a player wins or if the game ends in a draw, the game will announce the result and reset for a new game.

## 📜 Game Logic

- The game board is a 15x15 grid.
- Players are represented by 'X' and 'O'.
- The game checks for winning conditions in horizontal, vertical, and diagonal directions.
- The game will announce if a player wins or if the game is a draw.

## 📞 Support

For any issues or questions regarding the Gomoku game, please reach out to our support team at [support@chatdev.com](mailto:support@chatdev.com).

Enjoy playing Gomoku!
```

This manual provides a comprehensive overview of the Gomoku game, including installation instructions, gameplay rules, and support information. It should help users understand how to use the software effectively.