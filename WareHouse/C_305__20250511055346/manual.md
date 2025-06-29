# Gomoku Game

A simple implementation of the classic Gomoku game, allowing two players to compete against each other either via a console interface or a graphical user interface (GUI).

## Quick Install

To run the Gomoku game, you need to have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

Once Python is installed, you can install the required dependencies using pip:

```bash
pip install tkinter
```

## 🤔 What is Gomoku?

Gomoku, also known as Five in a Row, is a strategy board game for two players. The objective of the game is to be the first to get an unbroken row of five pieces horizontally, vertically, or diagonally.

## 📖 Main Functions of the Software

The Gomoku game consists of two main components:

1. **Console Mode**: A text-based interface where players input their moves via the command line.
2. **GUI Mode**: A graphical interface built using Tkinter, allowing players to click on the board to make their moves.

### Game Logic

The game logic is encapsulated in the `GomokuGame` class, which handles:

- Board initialization
- Player turns
- Move validation
- Win condition checks
- Game reset functionality

### User Interface

- **Console Mode**: Players are prompted to enter their moves by specifying the row and column indices (0-14).
- **GUI Mode**: Players click on the board to place their pieces, and the game updates the display accordingly.

## How to Use/Play

### Console Mode

1. Run the `main.py` file in your terminal:
   ```bash
   python main.py
   ```
2. Follow the prompts to enter your moves. Players take turns entering the row and column where they want to place their piece.
3. The game will announce the winner when one player achieves five in a row. You can choose to play again or exit.

### GUI Mode

1. Run the `gui.py` file in your terminal:
   ```bash
   python gui.py
   ```
2. A window will open displaying the Gomoku board.
3. Click on the squares to place your pieces. The current player will be displayed at the top.
4. The game will announce the winner when one player achieves five in a row.

### Example of Play

- Player X starts by entering `7` for row and `7` for column, placing their piece in the center of the board.
- Player O follows by entering `7` for row and `8` for column, placing their piece next to Player X's piece.
- The game continues until one player wins or all cells are filled.

## Conclusion

Enjoy playing Gomoku with friends or family! Whether you prefer a console experience or a graphical interface, this implementation provides a fun way to engage in this classic game. If you encounter any issues or have suggestions for improvements, feel free to reach out for support.