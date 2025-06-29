Here's a detailed user manual for the Gomoku game, formatted in Markdown as requested:

```markdown
# Gomoku Game

A simple command-line implementation of the classic Gomoku game, also known as Five in a Row. This game allows two players to compete against each other by placing their marks on a 15x15 board.

## Quick Install

To run the Gomoku game, you need to have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

Once Python is installed, you can clone the repository or download the files directly. Make sure you have the following files:

- `main.py`
- `game.py`

No additional dependencies are required to run this game.

## 🤔 What is Gomoku?

Gomoku is a strategy board game for two players. Players take turns placing their marks (X or O) on the board, and the first player to get five of their marks in a row (horizontally, vertically, or diagonally) wins the game.

## 🛠️ How to Use

1. **Run the Game:**
   Open your terminal or command prompt, navigate to the directory where the game files are located, and run the following command:

   ```bash
   python main.py
   ```

2. **Playing the Game:**
   - The game will display the current state of the board.
   - Players take turns entering their moves by specifying the row and column numbers (0 to 14).
   - For example, to place a mark in the first row and first column, enter `0 0`.
   - If a move is invalid (e.g., out of bounds or the cell is already occupied), an error message will be displayed, and the player will be prompted to enter a new move.

3. **Winning the Game:**
   - The game will announce the winner once a player gets five marks in a row.
   - If the board is full and no player has won, the game will declare a draw.

4. **Exiting the Game:**
   - To exit the game at any time, you can simply close the terminal or interrupt the process (usually Ctrl+C).

## 🎮 Game Rules

- The game is played on a 15x15 grid.
- Players alternate turns, with one player using "X" and the other using "O".
- The objective is to be the first to get five of your marks in a row, either horizontally, vertically, or diagonally.
- If all cells are filled and no player has achieved five in a row, the game ends in a draw.

## 📖 Documentation

For more information about the game logic and implementation, you can refer to the source code in the `game.py` file. The main game logic is encapsulated in the `GomokuGame` class, which handles moves, checks for winners, and manages the game state.

Feel free to modify the code to enhance the game or add new features!

## 🛠️ Troubleshooting

- **Python Not Found:** Ensure that Python is installed and added to your system's PATH.
- **Invalid Input:** Make sure to enter two integers separated by a space, and that they are within the range of 0 to 14.

Enjoy playing Gomoku!
```

This manual provides a comprehensive overview of the Gomoku game, including installation instructions, gameplay mechanics, and troubleshooting tips. Let me know if you need any further modifications or additional information!