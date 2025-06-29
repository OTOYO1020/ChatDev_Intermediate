Here's a detailed user manual for the Gomoku game application, formatted in Markdown:

```markdown
# Gomoku Game

A simple implementation of the classic Gomoku game, also known as Five in a Row.

## Quick Install

To run the Gomoku game, you need to have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

### Dependencies

This application does not require any external libraries, so you can run it with just Python.

## 🤔 What is Gomoku?

Gomoku is a traditional board game played with two players who take turns placing their pieces (black and white) on a 15x15 grid. The objective is to be the first player to get five of their pieces in a row, either horizontally, vertically, or diagonally.

## 🎮 How to Play

1. **Start the Game**: Run the `main.py` file to start the game.
   ```bash
   python main.py
   ```

2. **Game Board**: The game board will be displayed in the console, where:
   - `B` represents a black piece.
   - `W` represents a white piece.
   - `.` represents an empty cell.

3. **Making a Move**:
   - You will be prompted to enter the row (0-14) where you want to place your piece.
   - After entering the row, you will be prompted to enter the column (0-14).
   - If the cell is empty, your piece will be placed there. If the cell is already occupied, you will receive an "Invalid move" message.

4. **Winning the Game**: The game checks for a winner after each move. If a player gets five pieces in a row, a message will display indicating the winner, and the game will reset.

5. **Ending the Game**: To exit the game at any time, type `exit` when prompted for the row.

## 📜 Game Logic

The game logic is handled in the `gomoku_logic.py` file, which includes:
- **Making Moves**: Players take turns placing their pieces on the board.
- **Checking for Winners**: The game checks for winning conditions after each move.
- **Checking for Draws**: The game checks if the board is full and no player has won.

## 🛠️ Resetting the Game

After a win or a draw, the game automatically resets, and the board is cleared for a new game.

## 📞 Support

If you encounter any issues or have questions about the game, please reach out to our support team at support@chatdev.com.

Enjoy playing Gomoku!
```

This manual provides a comprehensive overview of the Gomoku game, including installation instructions, gameplay mechanics, and support information. Let me know if you need any further modifications or additional details!