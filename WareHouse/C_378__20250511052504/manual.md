Here's a detailed user manual for the Gomoku game software, formatted in Markdown as requested:

```markdown
# Gomoku Game

A simple implementation of the classic Gomoku game (also known as Five in a Row) using Python.

## Quick Install

To run the Gomoku game, you need to have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

Once you have Python installed, you can clone the repository or download the files directly. Make sure you have the following files:

- `main.py`
- `gomoku_game.py`

There are no additional dependencies required for this basic implementation.

## 🤔 What is Gomoku?

Gomoku is a two-player board game in which players take turns placing their pieces (X or O) on a 15x15 grid. The objective is to be the first player to get five of their pieces in a row, either horizontally, vertically, or diagonally.

## 🛠️ How to Use/Play

1. **Run the Game**:
   Open your terminal or command prompt, navigate to the directory where your files are located, and run the following command:
   ```bash
   python main.py
   ```

2. **Game Instructions**:
   - The game will prompt you to enter your move by specifying the row and column (both between 0 and 14).
   - Player X goes first, followed by Player O.
   - Input your move in the format:
     ```
     Player X, enter your move row (0-14): [your_row]
     Player X, enter your move column (0-14): [your_column]
     ```

3. **Winning the Game**:
   - The game will automatically check for a win after each move.
   - If a player gets five pieces in a row, the game will announce the winner and display the final board.

4. **Invalid Moves**:
   - If you try to place a piece in an already occupied cell or outside the board boundaries, the game will notify you and prompt for a new move.

5. **Resetting the Game**:
   - To reset the game, simply restart the program.

## 🎮 Example Gameplay

```
Player X, enter your move row (0-14): 7
Player X, enter your move column (0-14): 7
```

The board will update, and it will be Player O's turn.

## 📖 Documentation

For more information on how the game logic works, you can refer to the source code in `gomoku_game.py`. The main functions include:

- `make_move(row, col)`: Places a piece on the board and checks for a win.
- `check_win(row, col)`: Checks if the current player has won after their move.
- `reset_game()`: Resets the game to its initial state.

Feel free to modify the code to enhance the game or add new features!

## 🛠️ Troubleshooting

- **Python Not Found**: Ensure that Python is installed and added to your system's PATH.
- **Invalid Input**: Make sure to enter integers only for row and column inputs.

Enjoy playing Gomoku!
```

This manual provides a comprehensive guide for users to understand how to install, run, and play the Gomoku game, along with a brief overview of the game's functionality.