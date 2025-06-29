Here's the user manual for the Gomoku game, formatted in Markdown:

```markdown
# Gomoku Game

A simple command-line implementation of the classic Gomoku game, where two players take turns placing their marks on a 15x15 board. The first player to align five of their marks in a row (horizontally, vertically, or diagonally) wins the game.

## Quick Install

To run the Gomoku game, you need to have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

Once Python is installed, you can clone the repository or download the files directly. Ensure you have the following files in your project directory:

- `main.py`
- `gomoku_logic.py`

## 🤔 What is this?

Gomoku is a traditional board game that is played on a grid. The objective is to be the first player to get five of their marks in a row. This implementation allows two players to play against each other in a console environment.

## 🛠️ How to Install Environment Dependencies

This game does not require any additional dependencies beyond Python itself. Just ensure you have Python 3.x installed.

## 🎮 How to Use/Play

1. **Run the Game:**
   Open your terminal or command prompt, navigate to the directory where your `main.py` file is located, and run the following command:
   ```bash
   python main.py
   ```

2. **Game Instructions:**
   - The game will display a 15x15 board in the console.
   - Players take turns entering their moves. The current player is indicated by 'X' or 'O'.
   - To make a move, enter the coordinates of the cell where you want to place your mark. The coordinates should be two integers separated by a space (e.g., `7 7` for the center of the board).

3. **Winning the Game:**
   - The game checks for a winner after each move. If a player aligns five marks in a row, a message will announce the winner.
   - If the board is full and no player has won, the game will declare a draw.

4. **Invalid Moves:**
   - If a player attempts to place a mark in an already occupied cell, the game will notify them of the invalid move and prompt for another input.
   - Players must also ensure their coordinates are within the range of the board (0 to 14).

## 📖 Documentation

For more details on the game logic, you can refer to the `gomoku_logic.py` file, which contains the core functionality of the game, including:

- **Board Management:** How the board is initialized and updated.
- **Move Validation:** Ensuring moves are valid and checking for occupied cells.
- **Win Conditions:** Logic to determine if a player has won or if the game is a draw.

Enjoy playing Gomoku!
```

This manual provides a comprehensive overview of the game, installation instructions, and gameplay details, ensuring that users can easily understand and enjoy the Gomoku game.