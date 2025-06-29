Here’s a detailed user manual for the basic Gomoku game developed in Python. This manual includes an introduction to the game, installation instructions, and how to play.

```markdown
# Gomoku Game

A simple command-line implementation of the classic Gomoku game, also known as Five in a Row.

## Quick Install

To run the Gomoku game, you need to have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

Once Python is installed, you can run the game directly without any additional dependencies. Just ensure you have a terminal or command prompt available.

## 🤔 What is Gomoku?

Gomoku is a traditional board game that is played on a grid. The objective of the game is to be the first player to get five of their marks in a row, either horizontally, vertically, or diagonally. In this implementation, players take turns placing their marks on a 15x15 board.

## 🎮 How to Play

1. **Start the Game**: Run the `main.py` file in your terminal or command prompt:
   ```bash
   python main.py
   ```

2. **Game Board**: The game board will be displayed in the terminal. Empty spaces are represented by dots (.), while player marks are represented by "X" and "O".

3. **Making a Move**: Players take turns to enter their moves. When prompted, enter the row and column numbers (0-14) where you want to place your mark.

4. **Winning the Game**: The game checks for a winner after each move. If a player gets five marks in a row, a message will indicate that the player has won.

5. **Game Over**: Once a player wins, the game will prompt whether you want to play again. Enter 'y' to reset the game or 'n' to exit.

## 📜 Game Rules

- Players alternate turns, with Player X going first.
- A valid move must be within the bounds of the board (0 to 14 for both row and column).
- Players cannot place their mark on a cell that is already occupied.
- The game ends when one player achieves five marks in a row or when the players decide to exit.

## 🛠️ Troubleshooting

- **Invalid Input**: If you enter a value that is not a number or is out of bounds, the game will prompt you to enter a valid move.
- **Game Over**: If you try to make a move after the game has ended, you will receive a message indicating that no more moves can be made.

## 📞 Support

For any issues or feedback, please contact our support team at support@chatdev.com.

Enjoy playing Gomoku!
```

This manual provides a comprehensive overview of the game, installation instructions, and gameplay guidelines, ensuring that users can easily understand and enjoy the Gomoku game.