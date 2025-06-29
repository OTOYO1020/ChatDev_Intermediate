Here’s a detailed user manual for the Gomoku game application, formatted in Markdown as requested:

```markdown
# Gomoku Game

A simple implementation of the classic Gomoku game (also known as Five in a Row) in Python.

## Quick Install

To run the Gomoku game, you need to have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

Once Python is installed, you can clone the repository or download the files directly. Ensure you have the following files:

- `main.py`
- `gomoku_game.py`

No additional dependencies are required for this basic version of the game.

## 🤔 What is Gomoku?

Gomoku is a two-player board game where players take turns placing their markers (X or O) on a 15x15 grid. The objective is to be the first to get five of your markers in a row, either horizontally, vertically, or diagonally.

## 🛠️ How to Install Environment Dependencies

1. **Install Python**: Make sure you have Python 3.x installed on your system.
2. **Clone the Repository**: If you have Git installed, you can clone the repository using:
   ```bash
   git clone <repository-url>
   ```
   Alternatively, download the files directly from the repository.

3. **Navigate to the Game Directory**:
   ```bash
   cd path/to/gomoku-game
   ```

## 🎮 How to Play

1. **Run the Game**: Open your terminal or command prompt and run the following command:
   ```bash
   python main.py
   ```

2. **Game Interface**: The game will display the board in the terminal. Empty cells are represented by a dot (.), while occupied cells will show either X or O.

3. **Making a Move**:
   - You will be prompted to enter your move by specifying the row and column (both between 0 and 14).
   - For example, to place your marker in the first cell of the first row, enter `0` for row and `0` for column.

4. **Winning the Game**: The game checks for a winner after each move. If a player gets five in a row, a message will display indicating the winner, and the game will reset.

5. **Invalid Input**: If you enter an invalid move (e.g., out of bounds or a cell that is already occupied), you will receive an error message prompting you to enter a valid move.

## 📜 Game Logic

- The game board is a 15x15 grid.
- Players alternate turns, starting with Player X.
- The game checks for a win condition after each move by checking horizontal, vertical, and diagonal lines for five consecutive markers.

## 🔄 Resetting the Game

After a win, the game automatically resets, allowing players to start a new game without needing to restart the application.

## 📞 Support

For any issues or questions, please reach out to our support team at [support@chatdev.com](mailto:support@chatdev.com).

Enjoy playing Gomoku!
```

This manual provides a comprehensive guide for users to install, run, and play the Gomoku game, ensuring they have all the necessary information to enjoy the application.