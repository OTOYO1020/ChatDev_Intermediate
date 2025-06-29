Here's a detailed user manual for the Gomoku game application, formatted in Markdown:

```markdown
# Gomoku Game

A simple implementation of the classic Gomoku game, also known as Five in a Row.

## Quick Install

To run the Gomoku game, you need to have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

Once Python is installed, you can clone the repository or download the source code files. Ensure you have the following files:

- `main.py`
- `board.py`

## 🤔 What is Gomoku?

Gomoku is a traditional board game where two players take turns placing their marks (X and O) on a 15x15 grid. The objective is to be the first player to get five of their marks in a row, either horizontally, vertically, or diagonally.

## 📦 Requirements

This game does not have any external dependencies beyond Python itself. Make sure you have Python 3.x installed.

## 🎮 How to Play

1. **Start the Game**: Run the `main.py` file to start the game.
   ```bash
   python main.py
   ```

2. **Game Interface**: The game will display the board in the console. Empty cells are represented by a dot (`.`), while filled cells will show either `X` or `O` depending on the player.

3. **Making Moves**: Players will be prompted to enter their move by specifying the row and column numbers (both ranging from 0 to 14). For example:
   ```
   Player X, enter your row (0-14): 7
   Player X, enter your column (0-14): 7
   ```

4. **Winning the Game**: The game checks for a winner after each move. If a player successfully places five of their marks in a row, a message will be displayed announcing the winner. If the board is full and no player has won, the game will declare a draw.

5. **Restarting the Game**: After a game ends, players will be asked if they want to play again. Enter `y` to restart or `n` to exit.

## 📜 Game Rules

- Players take turns placing their marks on the board.
- The first player to align five of their marks in a row (horizontally, vertically, or diagonally) wins the game.
- If all cells are filled without a winner, the game ends in a draw.

## 📖 Documentation

For more information on how the game works, you can refer to the source code in `main.py` and `board.py`. The code is structured to handle the game logic, player turns, and win conditions.

### Code Structure

- **main.py**: The main entry point for the game, handling user input and game flow.
- **board.py**: Contains the `Board` and `Cell` classes that manage the game state and rules.

## 🛠️ Troubleshooting

If you encounter any issues while running the game, ensure that:
- You have Python installed correctly.
- You are running the game from the directory where `main.py` and `board.py` are located.

For any further questions or support, feel free to reach out to our support team.

Enjoy playing Gomoku!
```

This manual provides a comprehensive overview of the Gomoku game application, including installation instructions, gameplay mechanics, and troubleshooting tips.