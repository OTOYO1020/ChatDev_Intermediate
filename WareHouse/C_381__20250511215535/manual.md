Here's a detailed user manual for the Gomoku game application, formatted in Markdown as requested:

```markdown
# Gomoku Game

A simple console-based Gomoku game implemented in Python.

## Quick Install

To run the Gomoku game, you need to have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

Once Python is installed, you can clone the repository or download the source code files. Ensure you have the following files in your project directory:

- `main.py`
- `gomoku.py`

## 🤔 What is Gomoku?

Gomoku, also known as Five in a Row, is a strategy board game for two players. The objective is to be the first to get an unbroken row of five pieces, either horizontally, vertically, or diagonally.

## 📦 Dependencies

This application does not require any external dependencies beyond Python itself. However, it is recommended to run it in a virtual environment to avoid conflicts with other projects.

To create a virtual environment, you can use the following commands:

```bash
# Create a virtual environment
python -m venv gomoku_env

# Activate the virtual environment
# On Windows
gomoku_env\Scripts\activate
# On macOS/Linux
source gomoku_env/bin/activate
```

## 🎮 How to Play

1. **Start the Game**: Run the game by executing the `main.py` file in your terminal or command prompt.

   ```bash
   python main.py
   ```

2. **Game Instructions**:
   - The game board is a 15x15 grid.
   - Players take turns to place their pieces on the board. Player X goes first.
   - To make a move, enter the row and column numbers (both between 0 and 14) when prompted.
   - For example, entering `7` for the row and `7` for the column places your piece in the center of the board.

3. **Winning the Game**: The first player to align five of their pieces in a row (horizontally, vertically, or diagonally) wins the game. The game will announce the winner and terminate.

4. **Invalid Moves**: If you attempt to make an invalid move (e.g., placing a piece outside the board or in an already occupied cell), the game will prompt you to enter a valid move.

5. **Restarting the Game**: To play again, simply restart the application.

## 📜 Game Logic

The game logic is handled in the `gomoku.py` file, which contains the `GomokuGame` class. Key functions include:

- `make_move(row, col)`: Places a piece on the board and checks for a winner.
- `check_winner(row, col)`: Determines if the current player has won after their move.
- `display_board()`: Displays the current state of the game board in the console.

## 🛠️ Troubleshooting

- **Python Not Found**: Ensure Python is installed and added to your system's PATH.
- **Invalid Input**: If you receive an error about invalid moves, ensure you are entering numbers between 0 and 14.

## 📞 Support

For any issues or questions, please reach out to our support team at support@chatdev.com.

Enjoy playing Gomoku!
```

This manual provides a comprehensive overview of the Gomoku game, including installation instructions, gameplay mechanics, and troubleshooting tips. Let me know if you need any further modifications or additional information!