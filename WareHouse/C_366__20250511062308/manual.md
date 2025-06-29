Here's the user manual for the Gomoku game, formatted in Markdown as requested:

```markdown
# Gomoku Game

A simple implementation of the classic Gomoku game, also known as Five in a Row. This game allows two players to compete against each other by placing their markers on a 15x15 board.

## Quick Install

To run the Gomoku game, you need to have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

Once Python is installed, you can run the game without any additional dependencies. Simply download the game files and navigate to the directory in your terminal.

## 🕹️ How to Play

1. **Start the Game**: Run the `main.py` file to start the game.
   ```bash
   python main.py
   ```

2. **Game Rules**:
   - Players take turns placing their markers ('X' and 'O') on the board.
   - The first player to align five of their markers horizontally, vertically, or diagonally wins the game.

3. **Making a Move**:
   - When prompted, enter the row and column numbers (0-14) where you want to place your marker.
   - Example: To place your marker in the first row and first column, enter `0` for the row and `0` for the column.

4. **Winning the Game**:
   - The game will automatically check for a win after each move.
   - If a player wins, a message will display indicating the winning player.

5. **Playing Again**:
   - After a game ends, you will be asked if you want to play again. Enter `y` to restart or `n` to exit the game.

## 📜 Game Functions

- **make_move(row, col)**: Places the current player's marker on the board at the specified row and column if the move is valid.
- **check_win()**: Checks if the current player has won the game by aligning five markers.
- **reset_game()**: Resets the game board and starts a new game.
- **print_board()**: Displays the current state of the game board in the console.

## 🛠️ Dependencies

No external dependencies are required to run the Gomoku game. Ensure you have Python installed.

## 📖 Documentation

For further details on the game logic and implementation, you can refer to the source code in the following files:

- `gomoku_game.py`: Contains the game logic and rules.
- `main.py`: The main entry point for running the game.

Feel free to modify the code to enhance the game or add new features!

Enjoy playing Gomoku!
```

This manual provides a comprehensive overview of the game, including installation instructions, gameplay rules, and a brief description of the main functions. Let me know if you need any modifications or additional information!