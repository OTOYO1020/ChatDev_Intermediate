Here's a detailed user manual for the Gomoku game, formatted in Markdown as requested:

```markdown
# Gomoku Game

A simple console-based implementation of the classic Gomoku game, also known as Five in a Row.

## Quick Install

To run the Gomoku game, ensure you have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

Once Python is installed, you can run the game directly from the provided `main.py` file without any additional dependencies.

## 🤔 What is Gomoku?

Gomoku is a strategy board game for two players. The objective of the game is to be the first to get an unbroken row of five pieces, either horizontally, vertically, or diagonally. Players take turns placing their pieces on a 15x15 board, with one player using 'X' and the other using 'O'.

## 🎮 How to Play

1. **Start the Game**: Run the `main.py` file using Python. You can do this by navigating to the directory containing the file in your terminal and executing:
   ```bash
   python main.py
   ```

2. **Game Board**: The game board will be displayed in the console. Empty cells are represented by a dot (.), player 1's pieces are represented by 'X', and player 2's pieces are represented by 'O'.

3. **Making a Move**: Players will be prompted to enter their move in the format `row column` (e.g., `7 7` for the center of the board). 

4. **Winning the Game**: After each move, the game checks if the current player has won. If a player gets five pieces in a row, they will be declared the winner.

5. **Resetting the Game**: If you want to start a new game, type 'reset' when prompted. This will clear the board and reset the players.

6. **Exiting the Game**: To exit the game, type 'exit' when prompted.

## 📜 Game Rules

- Players alternate turns.
- A move is valid only if the chosen cell is empty and within the bounds of the board (0-14 for both row and column).
- If a player attempts to place a piece in an occupied cell or out of bounds, they will be prompted to try again.
- The game ends when a player wins or the board is full, resulting in a draw.

## 🛠️ Troubleshooting

- **Invalid Input**: If you enter an invalid move or command, you will receive an error message. Please follow the prompts to enter valid input.
- **Game Not Starting**: Ensure that you have Python installed and that you are running the `main.py` file correctly.

## 📖 Additional Resources

For more information on Gomoku and its strategies, you can refer to the following resources:

- [Wikipedia - Gomoku](https://en.wikipedia.org/wiki/Gomoku)
- [Gomoku Strategies](https://www.gomoku-strategies.com)

Enjoy playing Gomoku!
```

This manual provides a comprehensive overview of the game, including installation instructions, gameplay mechanics, and troubleshooting tips. Let me know if you need any further modifications or additional information!