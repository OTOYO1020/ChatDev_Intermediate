```markdown
# Gomoku Game

A simple implementation of the classic Gomoku game, allowing players to compete against each other in a console or graphical user interface (GUI) format.

## Quick Install

To run the Gomoku game, you need to have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

Once Python is installed, you can clone the repository or download the files directly. Make sure you have the following dependencies installed:

```bash
pip install tkinter
```

## 🤔 What is Gomoku?

Gomoku, also known as Five in a Row, is a board game traditionally played with black and white stones on a 15x15 grid. The objective is to be the first player to get five of their stones in a row, either horizontally, vertically, or diagonally.

## 🛠️ Main Functions

The Gomoku game consists of two main modes:

1. **Console Version**: Play the game in a terminal/command prompt.
2. **Graphical User Interface (GUI)**: Play the game using a simple graphical interface.

### Console Version

- Players take turns entering their moves by specifying the row and column numbers.
- The game board is displayed after each move.
- The game announces the winner when a player gets five in a row.

### GUI Version

- Players click on the board to place their stones.
- The game displays the board visually, with black and white stones.
- A reset button allows players to start a new game after one has finished.

## 📖 How to Play

### Console Version

1. Run the `main.py` file:
   ```bash
   python main.py
   ```
2. Follow the prompts to enter your moves. Input the row and column numbers separated by a space (e.g., `7 7`).
3. The game will display the board after each move and announce the winner when applicable.
4. After a game ends, you can choose to play again or exit.

### GUI Version

1. Run the `gomoku_gui.py` file:
   ```bash
   python gomoku_gui.py
   ```
2. Click on the board to place your stone (black for Player X and white for Player O).
3. The game will notify you when a player wins and will reset the board automatically.
4. Use the "Reset Game" button to start a new game at any time.

## 📝 Additional Information

- The game board is a 15x15 grid.
- Players alternate turns, starting with Player X.
- The game checks for a win condition after each move.

For any issues or feature requests, please contact our support team.

Thank you for playing Gomoku!
```