# Gomoku Game User Manual

Welcome to the Gomoku Game! This manual provides a comprehensive guide on how to install the necessary environment, understand the main functions of the software, and play the game.

## Quick Install

To run the Gomoku game, you need to have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

Once Python is installed, you can clone the repository or download the files directly. Make sure you have the following dependencies installed:

```bash
pip install tkinter
```

## What is Gomoku?

Gomoku, also known as Five in a Row, is a classic board game where two players take turns placing their markers (X and O) on a 15x15 grid. The objective is to be the first player to get five of their markers in a row, either horizontally, vertically, or diagonally.

## Main Functions of the Software

The Gomoku game consists of three main components:

1. **Game Logic (`gomoku.py`)**: This module manages the game state, including the board, player turns, and win conditions.
   - **make_move(x, y)**: Places a marker on the board at the specified coordinates.
   - **check_win()**: Checks if the current player has won the game.
   - **reset_game()**: Resets the game state for a new game.
   - **display_board()**: Displays the current state of the board in the console.

2. **Graphical User Interface (`gomoku_gui.py`)**: This module handles the GUI components and user interactions.
   - **draw_board()**: Draws the game board on the GUI.
   - **on_click(event)**: Handles user clicks on the board and updates the game state accordingly.
   - **update_status()**: Updates the status label to indicate whose turn it is.

3. **Main Entry Point (`main.py`)**: This is the main script that initializes the game and starts the text-based interaction loop.

## How to Play

### Text-Based Version

1. Run the `main.py` file in your terminal:
   ```bash
   python main.py
   ```
2. Follow the prompts to enter your moves. Players take turns entering their moves in the format `row column` (e.g., `7 7`).
3. The game will display the board after each move and announce the winner when a player gets five in a row.
4. After the game ends, you will be prompted to play again.

### GUI Version

1. Run the `gomoku_gui.py` file:
   ```bash
   python gomoku_gui.py
   ```
2. A window will open displaying the game board.
3. Click on the squares to place your markers. Player X starts first.
4. The status label will indicate whose turn it is and announce the winner when a player wins.
5. If you want to start a new game, you can reset the game state by closing and reopening the GUI.

## Conclusion

Enjoy playing Gomoku! If you have any questions or need further assistance, feel free to reach out for support. Happy gaming!