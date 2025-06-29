# Gomoku Game User Manual

## Introduction

Welcome to the Gomoku Game! This application allows you to play the classic board game Gomoku, also known as Five in a Row. The game is played on a 15x15 board where two players take turns placing their pieces (X for Player 1 and O for Player 2) with the objective of getting five of their pieces in a row, either horizontally, vertically, or diagonally.

## Main Functions

- **make_move(x, y)**: Places a move on the board for the current player at the specified coordinates (x, y).
- **check_winner()**: Checks the board for a winner by examining all possible directions.
- **reset_game()**: Resets the game board to the initial state.
- **print_board()**: Prints the current state of the game board.

## Installation

To run the Gomoku game, you need to have Python installed on your machine. Follow these steps to set up your environment:

1. **Install Python**: If you haven't already, download and install Python from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: If you have the code in a repository, clone it using:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

3. **Install Dependencies**: This game does not require any additional dependencies beyond Python itself. Ensure you have Python 3.x installed.

## How to Play

1. **Run the Game**: Open your terminal or command prompt, navigate to the directory where `main.py` is located, and run the following command:
   ```bash
   python main.py
   ```

2. **Game Instructions**:
   - The game will display the current state of the board.
   - Players take turns entering their moves. Player 1 uses 'X' and Player 2 uses 'O'.
   - Enter your move as two integers separated by a space, representing the row and column indices (0-indexed). For example, to place a piece in the top-left corner, enter `0 0`.
   - The game will notify you if your move is invalid (e.g., if the cell is already occupied or out of bounds).

3. **Winning the Game**: The game checks for a winner after each move. If a player gets five pieces in a row, the game will announce the winner and display the final board state.

4. **Resetting the Game**: If you wish to play again, simply restart the game by running `python main.py` again.

## Conclusion

Enjoy playing Gomoku! This game is a great way to challenge your strategic thinking and have fun with friends or family. If you encounter any issues or have suggestions for improvements, please feel free to reach out. Happy gaming!