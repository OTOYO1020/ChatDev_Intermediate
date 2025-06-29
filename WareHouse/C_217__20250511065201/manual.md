Here's a detailed user manual for the Gomoku game, formatted in Markdown as requested:

```markdown
# Gomoku Game

A simple command-line implementation of the classic Gomoku game, also known as Five in a Row.

## Quick Install

To run the Gomoku game, you need to have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

Once Python is installed, you can run the game without any additional dependencies. Simply clone the repository or download the files and navigate to the directory containing the game files.

## 🤔 What is Gomoku?

Gomoku is a traditional board game where two players take turns placing their markers (X and O) on a 15x15 grid. The objective is to be the first to get five of your markers in a row, either horizontally, vertically, or diagonally.

## 📦 Installation

1. **Download the Game Files:**
   - Clone the repository or download the `main.py` and `gomoku_game.py` files.

2. **Navigate to the Game Directory:**
   Open your terminal or command prompt and navigate to the directory where the game files are located.

3. **Run the Game:**
   Execute the following command:
   ```bash
   python main.py
   ```

## 🎮 How to Play

1. **Starting the Game:**
   - When you run the game, the board will be displayed, and it will be Player X's turn.

2. **Making a Move:**
   - Enter your move by specifying the row and column numbers (0-14) separated by a space. For example, to place your marker in the first row and first column, you would enter:
     ```
     0 0
     ```

3. **Winning the Game:**
   - The game checks for a winner after each move. If a player gets five markers in a row, the game will announce the winner and reset the board for a new game.

4. **Invalid Moves:**
   - If you enter a move that is out of bounds or in an already occupied cell, the game will prompt you to enter a valid move.

5. **Ending the Game:**
   - The game will automatically end when a player wins. You can restart the game by following the prompts.

## 📜 Game Rules

- Players take turns placing their markers on the board.
- The first player to align five markers in a row (horizontally, vertically, or diagonally) wins the game.
- If a player attempts to place a marker outside the 15x15 grid or in an occupied cell, an error message will be displayed.

## 🛠️ Technical Details

- **Game Logic:** The game logic is implemented in `gomoku_game.py`, which handles the board state, player turns, and win conditions.
- **User Interface:** The game is played via a command-line interface, with the board printed in the terminal.

## 📞 Support

For any issues or questions, please reach out to our support team at support@chatdev.com.

Enjoy playing Gomoku!
```

This manual provides a comprehensive overview of the Gomoku game, including installation instructions, gameplay rules, and support information. Let me know if you need any further modifications or additional sections!