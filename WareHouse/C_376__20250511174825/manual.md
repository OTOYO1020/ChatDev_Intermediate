Here's a detailed user manual for the Gomoku game software, formatted in Markdown:

```markdown
# Gomoku Game

A simple implementation of the classic Gomoku game, also known as Five in a Row. This game can be played in a command-line interface or with a graphical user interface (GUI) using Tkinter.

## Quick Install

To run the Gomoku game, you need to have Python installed on your machine. You can install the required dependencies using the following command:

```bash
pip install -r requirements.txt
```

## 🤔 What is Gomoku?

Gomoku is a two-player board game in which players take turns placing their marks (X or O) on a 15x15 grid. The objective is to be the first to get five of your marks in a row, either horizontally, vertically, or diagonally.

## 📦 Main Functions

The Gomoku game consists of the following main components:

1. **Game Logic**: The core logic of the game is implemented in `gomoku_game.py`, which handles the game state, player turns, and win conditions.
2. **Command-Line Interface (CLI)**: The game can be played in the terminal using `main.py`, which provides a simple text-based interface for user interaction.
3. **Graphical User Interface (GUI)**: The game can also be played using a GUI implemented in `gomoku_gui.py`, which provides a more user-friendly experience.

## 📥 How to Use/Play

### Command-Line Interface

1. Run the game by executing the following command in your terminal:

   ```bash
   python main.py
   ```

2. The game board will be displayed in the terminal. Players will take turns entering their moves by specifying the row and column numbers (0-14).

3. For example, to place your mark in the first row and first column, enter:

   ```
   0 0
   ```

4. The game will continue until there is a winner or the game ends in a draw. The winner will be announced in the terminal.

### Graphical User Interface

1. To run the GUI version of the game, you need to modify the `main.py` file to include the GUI initialization. You can add the following code to the `main()` function:

   ```python
   import tkinter as tk
   from gomoku_gui import GomokuGUI

   def main():
       game = GomokuGame()
       root = tk.Tk()
       gui = GomokuGUI(root, game)
       root.mainloop()
   ```

2. Run the modified `main.py` file:

   ```bash
   python main.py
   ```

3. A window will open displaying the Gomoku board. Players can click on the buttons to place their marks.

4. A reset button is available to start a new game after one has concluded.

## 📄 Requirements

To ensure the game runs smoothly, make sure you have the following dependencies installed:

- Python 3.x
- Tkinter (usually included with Python installations)

You can specify any additional libraries in the `requirements.txt` file if needed.

## 📚 Documentation

For more information on how to extend or modify the game, please refer to the source code in the respective Python files:

- `gomoku_game.py`: Contains the game logic.
- `main.py`: Entry point for the command-line interface.
- `gomoku_gui.py`: Contains the GUI implementation.

Feel free to explore and enhance the game as you wish!
```

This manual provides a comprehensive overview of the Gomoku game, including installation instructions, gameplay details, and references to the source code for further exploration.