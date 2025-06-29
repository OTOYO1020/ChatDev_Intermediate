Here is the user manual for the Gomoku game application, formatted in Markdown:

```markdown
# Gomoku Game

A simple implementation of the classic Gomoku game, also known as Five in a Row.

## Quick Install

To run the Gomoku game, you need to have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

Once you have Python installed, you can run the game directly without any additional dependencies.

## 🤔 What is Gomoku?

Gomoku is a two-player board game in which players take turns placing their pieces (X or O) on a 15x15 grid. The objective is to be the first to get five of your pieces in a row, either horizontally, vertically, or diagonally.

## 🛠️ How to Install Environment Dependencies

1. **Install Python**: Ensure you have Python 3.x installed on your system. You can verify your installation by running:
   ```bash
   python --version
   ```

2. **Clone the Repository**: Clone the repository containing the Gomoku game code to your local machine:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

3. **Run the Game**: You can run the game directly using the command:
   ```bash
   python main.py
   ```

## 🎮 How to Play

1. **Starting the Game**: Run the `main.py` file to start the game in the console. You will see the game board printed in the terminal.

2. **Making a Move**: Players take turns to enter their moves. When prompted, enter the row and column numbers (0-14) separated by a space. For example:
   ```
   Player 1, enter your move (row and column): 7 7
   ```

3. **Winning the Game**: The game will check for a winner after each move. If a player gets five in a row, the game will announce the winner and end.

4. **Invalid Moves**: If you enter a move that is out of bounds or in an already occupied cell, you will be prompted to try again.

## 🖥️ GUI Version

If you prefer a graphical interface, you can run the GUI version of the game by executing:
```bash
python gui.py
```

### GUI Controls

- Click on the grid to place your piece.
- The game will automatically update the board and announce the winner if there is one.

## 📜 Game Rules

- Players alternate turns.
- The first player to align five of their pieces in a row (horizontally, vertically, or diagonally) wins the game.
- If the board is full and no player has won, the game ends in a draw.

## 📞 Support

For any issues or questions, please contact our support team at [support@chatdev.com](mailto:support@chatdev.com).

Enjoy playing Gomoku!
```

This manual provides a comprehensive guide for users to install, run, and play the Gomoku game, ensuring they have all the necessary information to get started.