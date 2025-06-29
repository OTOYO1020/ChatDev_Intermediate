# Gomoku Game User Manual

Welcome to the Gomoku Game! This manual will guide you through the installation, setup, and gameplay of the Gomoku application developed in Python.

## 🛠️ Installation

To run the Gomoku game, you need to have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

### Environment Dependencies

The Gomoku game does not require any external libraries beyond the standard Python library. However, ensure you have Python version 3.6 or higher.

### Steps to Install

1. **Download the Source Code**: Clone or download the repository containing the game files (`main.py`, `board.py`, `player.py`).

2. **Navigate to the Directory**: Open your terminal or command prompt and navigate to the directory where the game files are located.

3. **Run the Game**: Execute the following command to start the game:
   ```bash
   python main.py
   ```

## 🎮 How to Play

### Game Overview

Gomoku is a two-player board game where players take turns placing their symbols (X or O) on a 15x15 grid. The objective is to be the first player to get five of their symbols in a row, either horizontally, vertically, or diagonally.

### Starting the Game

1. **Launch the Game**: Run `main.py` as described in the installation section.
2. **Game Interface**: The game board will be displayed in the terminal, with empty cells represented by dots (.) and occupied cells by the respective player symbols (X or O).

### Making Moves

- Players will take turns to enter their moves.
- When prompted, enter the row index (0-14) for your move.
- Next, enter the column index (0-14) for your move.
- If you wish to exit the game at any time, type `exit`.

### Validating Moves

- The game will check if the entered row and column are within the valid range (0-14).
- If the cell is already occupied, you will be prompted to try again.
- The game will notify you if you have made an invalid move or if the game has ended.

### Winning the Game

- The game checks for a winner after each move.
- If a player successfully places five of their symbols in a row, a message will display indicating the winner.
- If the board is full and no player has won, the game will declare a draw.

### Example Gameplay

```
Player 1, enter your move row (0-14) or type 'exit' to quit: 7
Player 1, enter your move column (0-14): 7
```

The board will update, and it will be Player 2's turn.

## 📚 Additional Information

For any issues or further assistance, please reach out to our support team. We hope you enjoy playing Gomoku!

Happy Gaming!