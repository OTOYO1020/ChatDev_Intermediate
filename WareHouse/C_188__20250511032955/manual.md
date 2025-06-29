Here's the user manual for the Gomoku game application in Markdown format:

```markdown
# Gomoku Game

A simple implementation of the classic Gomoku game, also known as Five in a Row.

## Quick Install

To run the Gomoku game, you need to have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Dependencies

No additional dependencies are required for this game. Just ensure you have Python 3.x installed.

## 🤔 What is Gomoku?

Gomoku is a traditional board game played on a 15x15 grid where two players take turns placing their pieces (X and O) on the board. The objective is to be the first player to get five of their pieces in a row, either horizontally, vertically, or diagonally.

## 📖 How to Play

1. **Start the Game**: Run the `main.py` file to start the game.
   ```bash
   python main.py
   ```

2. **Game Board**: The game board will be displayed in the console. Empty cells are represented by a dot (`.`), while occupied cells will show either `X` or `O`.

3. **Making a Move**: Players will be prompted to enter their move in the format `row column` (e.g., `7 7` for the center of the board). Each player takes turns making their move.

4. **Winning the Game**: The game checks for a winner after each move. If a player gets five pieces in a row, a message will be displayed announcing the winner. If the board is full and no player has won, the game will declare a draw.

5. **Resetting the Game**: If you wish to play again, you can reset the game by running the `reset_game` method in the code. This will clear the board and start a new game.

## 🎮 Game Controls

- **Input Format**: Enter your move as two integers separated by a space (e.g., `3 4`).
- **Invalid Moves**: If you try to place a piece in an occupied cell or outside the board boundaries, an error message will be displayed.

## 📜 Code Structure

- `main.py`: The main entry point for the Gomoku game application.
- `board.py`: Contains the `Board` class that manages the game logic, including placing pieces, checking for winners, and displaying the board.

## 🛠️ Example of Running the Game

```bash
$ python main.py
Enter your move (row and column): 7 7
. . . . . . . . . . . . . . .
. . . . . . . . . . . . . . .
. . . . . . . . . . . . . . .
. . . . . . . . . . . . . . .
. . . . X . . . . . . . . . .
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

## 📞 Support

If you encounter any issues or have questions about the game, please reach out to our support team at support@chatdev.com.

Enjoy playing Gomoku!
```

This manual provides a comprehensive overview of the Gomoku game, including installation instructions, gameplay mechanics, and code structure, ensuring users can easily understand and enjoy the game.