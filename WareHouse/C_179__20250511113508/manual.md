Here's a detailed user manual for the Gomoku game application, formatted in Markdown:

```markdown
# Gomoku Game

A simple command-line implementation of the classic Gomoku game, also known as Five in a Row.

## Quick Install

To run the Gomoku game, you need to have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Install Dependencies

Currently, there are no external dependencies required for this game. Just ensure you have Python installed.

## 🤔 What is Gomoku?

Gomoku is a traditional board game played on a 15x15 grid. The objective is to be the first player to get five of their marks in a row, either horizontally, vertically, or diagonally. Players take turns placing their marks (X or O) on the board.

## 🕹️ How to Play

1. **Run the Game**: Open your terminal or command prompt, navigate to the directory where the game files are located, and run the following command:
   ```bash
   python main.py
   ```

2. **Make Your Move**: The game will prompt you to enter your move. You will need to provide two numbers:
   - The row number (0-14)
   - The column number (0-14)

   For example, if you want to place your mark in the first row and first column, you would enter:
   ```
   Player X, enter your move row (0-14): 0
   Player X, enter your move column (0-14): 0
   ```

3. **Game Flow**: The game alternates between Player X and Player O. After each move, the game checks for a winner or a draw. If a player wins or if the board is full (resulting in a draw), the game will display the result and end.

4. **Invalid Moves**: If you attempt to make an invalid move (e.g., placing a mark in an already occupied cell or entering a number outside the range), the game will inform you and prompt you to try again.

5. **Restarting the Game**: To play again, you can simply run the game again using the command mentioned above.

## 📖 Game Logic

- The game board is represented as a 15x15 grid.
- Players take turns placing their marks (X or O).
- The game checks for a winner after each move by examining rows, columns, and diagonals for five consecutive marks.
- If the board is full and no player has won, the game declares a draw.

## 🎮 Example Game Flow

```
Player X, enter your move row (0-14): 0
Player X, enter your move column (0-14): 0
. . . . . . . . . . . . . . .
. . . . . . . . . . . . . . .
. . . . . . . . . . . . . . .
. . . . . . . . . . . . . . .
. . . . . . . . . . . . . . .
. . . . . . . . . . . . . . .
. . . . . . . . . . . . . . .
. . . . . . . . . . . . . . .
. . . . . . . . . . . . . . .
. . . . . . . . . . . . . . .
. . . . . . . . . . . . . . .
. . . . . . . . . . . . . . .
. . . . . . . . . . . . . . .
. . . . . . . . . . . . . . .
. . . . . . . . . . . . . . .
```

## 🛠️ Troubleshooting

- **Python Not Found**: Ensure that Python is installed and added to your system's PATH.
- **Invalid Input**: If you receive an error about invalid input, make sure you are entering numbers between 0 and 14.

## 📞 Support

For any issues or questions, please contact our support team at support@chatdev.com.

Enjoy playing Gomoku!
```

This manual provides a comprehensive guide for users to install, run, and play the Gomoku game, ensuring they have all the necessary information to enjoy the application.