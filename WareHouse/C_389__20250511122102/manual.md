Here's a detailed user manual for the Gomoku game application, formatted in Markdown:

```markdown
# Gomoku Game

A simple and engaging Gomoku game implemented in Python, allowing players to compete against each other on a 15x15 board.

## Quick Install

To run the Gomoku game, you need to have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

Once Python is installed, you can clone the repository or download the source code files. Make sure you have the following files:

- `main.py`
- `gomoku_game.py`

You do not need any additional dependencies for this basic version of the game.

## 🎮 What is Gomoku?

Gomoku, also known as Five in a Row, is a traditional board game where two players take turns placing their marks (X or O) on a grid. The objective is to be the first player to get five of their marks in a row, either horizontally, vertically, or diagonally.

## 📖 How to Play

1. **Start the Game**: Run the `main.py` file to start the game.
   ```bash
   python main.py
   ```

2. **Game Instructions**:
   - Players take turns placing their marks (X or O) on a 15x15 board.
   - Enter your move as two integers representing the row and column (0-14).
   - The first player to get 5 in a row wins the game.

3. **Making a Move**:
   - When prompted, enter the row and column numbers for your move.
   - Example: To place your mark in the first row and first column, enter `0 0`.

4. **Winning the Game**:
   - The game will check for a winner after each move.
   - If a player wins, the game will display the winner and ask if you want to play again.

5. **Restarting or Exiting**:
   - If you want to play again after a game ends, enter `y` when prompted.
   - To exit the game, enter `n`.

## 🛠️ Code Structure

- **main.py**: The main entry point for the Gomoku game application. It handles user input and game flow.
- **gomoku_game.py**: Contains the `GomokuGame` class, which manages the game logic, including board state, player turns, and win conditions.

## 📜 Game Logic

- The game board is a 15x15 grid initialized with empty spaces.
- Players alternate turns, and the game checks for a winner after each move.
- The game can be reset to allow for a new match without restarting the application.

## 📝 Additional Notes

- This version of the Gomoku game is console-based and does not include a graphical user interface (GUI).
- Feel free to modify the code to add more features, such as a GUI or enhanced game rules.

For any questions or support, please contact the development team at ChatDev.

Enjoy playing Gomoku!
```

This manual provides a comprehensive overview of the Gomoku game, including installation instructions, gameplay details, and an explanation of the code structure. It is designed to help users easily understand how to install and play the game.