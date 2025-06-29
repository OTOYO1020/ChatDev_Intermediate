Here's a detailed user manual for the Gomoku game application, formatted in Markdown:

```markdown
# Gomoku Game

A simple command-line Gomoku game where two players take turns placing stones on a 15x15 board. The first player to align five stones in a row (horizontally, vertically, or diagonally) wins the game.

## Quick Install

To run the Gomoku game, you need to have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

### Environment Dependencies

This application does not require any external libraries, but you need to ensure you have Python 3.x installed. You can check your Python version by running:

```bash
python --version
```

## 🤔 What is Gomoku?

Gomoku, also known as Five in a Row, is a traditional board game played with black and white stones. Players take turns placing their stones on a grid, aiming to be the first to get five of their stones in a row.

## 🎮 How to Play

1. **Start the Game**: Run the `main.py` file to start the game.
   ```bash
   python main.py
   ```

2. **Game Interface**: The game will display the current state of the board in the console. Empty spaces are represented by dots (.), while black and white stones are represented by their initials (B for black and W for white).

3. **Making a Move**: When it's your turn, you will be prompted to enter the row and column where you want to place your stone. The valid range for both row and column is from 0 to 14. For example, to place a stone in the center of the board, you would enter:
   ```
   7 7
   ```

4. **Winning the Game**: The game checks for a winner after each move. If a player aligns five stones in a row, the game will announce the winner.

5. **Draw Condition**: If the board is full and no player has won, the game will declare a draw.

6. **Play Again**: After the game ends, you will be prompted to play again. Enter 'y' to restart or 'n' to exit.

## 📜 Game Rules

- Players alternate turns.
- A player wins by placing five of their stones in a row, either horizontally, vertically, or diagonally.
- If the board is full and no player has won, the game ends in a draw.

## 🛠️ Code Structure

The game consists of two main files:

- **`main.py`**: The main entry point for the game, handling user input and game flow.
- **`game_logic.py`**: Contains the core game logic, including board management, move validation, and win/draw conditions.

## 📖 Documentation

For further details on the game logic and implementation, you can refer to the source code in `game_logic.py` and `main.py`.

## 📝 Feedback

We welcome any feedback or suggestions for improvements. Please feel free to reach out to us!

Enjoy playing Gomoku!
```

This manual provides a comprehensive overview of the Gomoku game, including installation instructions, gameplay mechanics, and a brief explanation of the code structure. It should help users understand how to install and play the game effectively.