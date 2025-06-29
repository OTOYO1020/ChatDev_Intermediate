Here's a detailed user manual for the Gomoku game application, formatted in Markdown as requested:

```markdown
# Gomoku Game

A simple console-based Gomoku game where two players can compete against each other.

## Quick Install

To run the Gomoku game, ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

Once Python is installed, you can clone the repository or download the files directly. Make sure you have the following files in your project directory:

- `main.py`
- `gomoku_game.py`

## 🤔 What is Gomoku?

Gomoku, also known as Five in a Row, is a traditional board game played with black and white stones on a grid. The objective is to be the first player to get five of your marks in a row, either horizontally, vertically, or diagonally.

## 🛠️ How to Install Environment Dependencies

This application does not require any external libraries or dependencies beyond Python itself. Simply ensure you have Python 3.x installed.

## 🎮 How to Play

1. **Run the Game**: Open your terminal or command prompt, navigate to the directory where the game files are located, and run the following command:
   ```bash
   python main.py
   ```

2. **Game Instructions**:
   - The game will display a 15x15 board.
   - Players take turns entering their moves.
   - Player X starts first, followed by Player O.
   - Enter the row and column numbers (0-14) for your move when prompted.

3. **Winning the Game**:
   - The first player to align five of their marks in a row (horizontally, vertically, or diagonally) wins the game.
   - If the board is full and no player has won, the game ends in a draw.

4. **Game Over**:
   - Once the game is over, the board will be displayed again, and the winner will be announced or a message indicating a draw will be shown.

5. **Restarting the Game**:
   - To play again, simply rerun the `main.py` file.

## 📖 Documentation

For more details on the game logic and implementation, refer to the source code in `gomoku_game.py`. The main functions include:

- **`make_move(row, col)`**: Places the current player's mark on the board.
- **`check_winner(row, col)`**: Checks if the current player has won after making a move.
- **`display_board()`**: Displays the current state of the game board.
- **`is_game_over()`**: Checks if the game is over (either a win or a draw).

## 📝 Notes

- Ensure to enter valid row and column numbers within the range of 0 to 14.
- The game will prompt you if you make an invalid move, such as entering a number out of range or trying to place a mark in an already occupied cell.

Enjoy playing Gomoku!
```

This manual provides a comprehensive overview of the Gomoku game application, including installation instructions, gameplay mechanics, and documentation references. Let me know if you need any further modifications or additions!