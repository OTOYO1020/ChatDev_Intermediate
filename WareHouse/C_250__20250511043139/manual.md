Here is the user manual for the Gomoku game application, formatted in Markdown as requested:

```markdown
# Gomoku Game

A simple and interactive Gomoku game implemented in Python.

## Quick Install

To run the Gomoku game, you need to have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

Once Python is installed, you can clone the repository or download the files directly. Make sure you have the following dependencies installed:

```bash
pip install tkinter
```

## 🤔 What is Gomoku?

Gomoku, also known as Five in a Row, is a traditional board game where two players take turns placing their marks (X and O) on a 15x15 grid. The objective is to be the first to get five of your marks in a row, either horizontally, vertically, or diagonally.

## 📖 How to Play

### Starting the Game

1. Run the application by executing the `main.py` file in your terminal or command prompt:

   ```bash
   python main.py
   ```

2. The game will display the current board in the terminal and prompt you to enter the row and column where you want to place your mark.

### Making Moves

- Players take turns entering their moves. The current player will be displayed in the terminal.
- Enter the row (0-14) and column (0-14) for your move.
- If the cell is already occupied, you will receive an "Invalid move!" message, and you can try again.

### Winning the Game

- The game checks for a winner after each move. If a player gets five marks in a row, the game will announce the winner in the terminal.
- To reset the game, you can restart the application.

### GUI Version

If you prefer a graphical interface, you can run the `gomoku_gui.py` file:

```bash
python gomoku_gui.py
```

This will open a window where you can click on the cells to make your moves. The current player and game status will be displayed at the bottom of the window.

### Resetting the Game

- In the GUI version, you can reset the game at any time by clicking the "Reset Game" button.
- In the terminal version, you will need to restart the application to reset the game.

## 🎮 Enjoy Playing!

Have fun playing Gomoku! Challenge your friends or play against yourself to improve your strategy.
```

This manual provides a comprehensive overview of the Gomoku game, including installation instructions, gameplay mechanics, and how to use both the terminal and GUI versions of the game. Let me know if you need any further modifications or additional information!