Here's a detailed user manual for the Gomoku game application, formatted in Markdown as requested:

```markdown
# Gomoku Game

A simple command-line implementation of the classic Gomoku game, also known as Five in a Row.

## Quick Install

To run the Gomoku game, you need to have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

Once you have Python installed, you can clone the repository or download the files directly. Make sure you have the following files:

- `gomoku.py`
- `main.py`

## 🤔 What is Gomoku?

Gomoku is a traditional board game that is played on a 15x15 grid. The objective of the game is to be the first player to get five of their pieces in a row, either horizontally, vertically, or diagonally.

## 🎮 How to Play

1. **Start the Game**: Run the `main.py` file to start the game.
   ```bash
   python main.py
   ```

2. **Game Instructions**:
   - The game will welcome you and display the current state of the board.
   - Players take turns to make their moves. Player 1 uses 'X' and Player 2 uses 'O'.
   - Enter your move by specifying the row and column numbers (0-indexed) separated by a space. For example, to place your piece in the first row and first column, you would enter `0 0`.

3. **Winning the Game**: The game checks for a winner after each move. If a player gets five pieces in a row, the game will announce the winner and end.

4. **Invalid Moves**: If you enter a move that is out of bounds or in an already occupied cell, you will be prompted to enter a valid move.

5. **Resetting the Game**: If you want to play again, you can restart the `main.py` file.

## 📜 Game Features

- **Two Players**: The game supports two players who take turns making moves.
- **Win Detection**: The game automatically checks for a winner after each move.
- **User-Friendly Interface**: The game displays the board in a simple text format, making it easy to follow the game.

## 📦 Dependencies

This application does not require any external dependencies beyond Python itself. Ensure you have Python 3.x installed.

## 🛠️ Troubleshooting

- **Python Not Found**: If you encounter an error stating that Python is not found, ensure that Python is correctly installed and added to your system's PATH.
- **Invalid Input**: If you receive an error when entering your move, ensure that you are entering two integers separated by a space.

## 📞 Support

For any issues or questions regarding the Gomoku game, please contact our support team at support@chatdev.com.

Enjoy playing Gomoku!
```

This manual provides a comprehensive overview of the Gomoku game, including installation instructions, gameplay mechanics, and troubleshooting tips, ensuring that users can easily understand and enjoy the game.