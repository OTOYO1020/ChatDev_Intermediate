Here's a detailed user manual for the Gomoku game application, formatted in Markdown as requested:

```markdown
# Gomoku Game

A simple and interactive Gomoku game application developed in Python.

## Quick Install

To run the Gomoku game, you need to have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

Once Python is installed, you can clone the repository or download the source code. Navigate to the directory containing the code files and run the following command to install any required dependencies:

```bash
pip install tkinter
```

## 🎮 What is Gomoku?

Gomoku, also known as Five in a Row, is a classic board game where two players take turns placing their marks (X and O) on a 15x15 grid. The objective is to be the first player to get five of their marks in a row, either horizontally, vertically, or diagonally.

## 🛠️ How to Use/Play

### Running the Game

1. **Open a Terminal or Command Prompt**.
2. Navigate to the directory where the game files (`main.py`, `gomoku.py`, `gui.py`) are located.
3. Run the game using the following command:

   ```bash
   python main.py
   ```

   or, if you prefer to use the GUI version:

   ```bash
   python gui.py
   ```

### Game Controls

- **Text-Based Version**:
  - The game will display the board in the terminal.
  - Players will be prompted to enter their moves in the format `row column` (e.g., `7 7`).
  - The game will announce the winner when a player gets five in a row.

- **Graphical User Interface (GUI) Version**:
  - The game window will display a 15x15 grid.
  - Click on the grid to place your mark (X or O).
  - A "Reset Game" button is available to start a new game after one ends.
  - A pop-up will display the winner when the game concludes.

### Game Rules

- Players take turns placing their marks on the board.
- The first player to align five of their marks in a row (horizontally, vertically, or diagonally) wins the game.
- If a player tries to place a mark in an already occupied cell or outside the grid, an error message will be displayed.

## 📖 Documentation

For further details on the game logic and implementation, you can refer to the source code files:

- **`gomoku.py`**: Contains the game logic and state management.
- **`main.py`**: The main entry point for the text-based version of the game.
- **`gui.py`**: Contains the GUI implementation using Tkinter.

## 🛠️ Troubleshooting

If you encounter any issues while running the game, ensure that:

- You have Python installed correctly.
- You have installed the required dependencies.
- You are running the game from the correct directory.

For any further assistance, feel free to reach out to our support team.

Enjoy playing Gomoku!
```

This manual provides a comprehensive overview of the Gomoku game, including installation instructions, gameplay mechanics, and troubleshooting tips. Let me know if you need any further modifications or additional information!