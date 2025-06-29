# Gomoku Game User Manual

Welcome to the Gomoku Game! This manual will guide you through the installation, usage, and main functions of the software.

## Quick Install

To run the Gomoku game, you need to have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

Once Python is installed, you can set up the environment and run the game using the following steps:

1. **Clone the Repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Required Dependencies**:
   You don't need any external libraries for this basic version of the Gomoku game, as it uses only built-in Python features. However, ensure you have Python 3.x installed.

## 🤔 What is Gomoku?

Gomoku, also known as Five in a Row, is a traditional board game where two players take turns placing their pieces (black and white) on a 15x15 grid. The objective is to be the first player to get five of their pieces in a row, either horizontally, vertically, or diagonally.

## 🎮 How to Play

1. **Start the Game**:
   Run the `main.py` file to start the game:
   ```bash
   python main.py
   ```

2. **Game Interface**:
   The game will display the current state of the board in the console. Empty cells are represented by a dot (.), while the black and white pieces are represented by 'B' and 'W', respectively.

3. **Player Turns**:
   Players will take turns to place their pieces on the board. The game starts with the Black player.

4. **Input Coordinates**:
   When prompted, enter the row and column numbers (0-14) separated by a space to place your piece. For example, to place a piece in the first row and first column, enter:
   ```
   0 0
   ```

5. **Winning the Game**:
   The game checks for a win condition after each move. If a player successfully places five pieces in a row, the game will announce the winner and display the final board.

6. **Invalid Moves**:
   If a player tries to place a piece in an occupied cell or enters coordinates out of bounds, they will be prompted to enter valid coordinates again.

## 📜 Main Functions

- **`GomokuGame` Class**: The main class that manages the game flow, including player turns and win checking.
- **`Board` Class**: Represents the game board and handles the logic for displaying the board, placing pieces, and checking for win conditions.
- **`Player` Class**: Represents a player in the game, storing their color.

## 📚 Additional Information

For further details on the code structure and logic, you can refer to the source files:
- `main.py`: The entry point for the game.
- `board.py`: Contains the logic for the game board.
- `player.py`: Defines the player class.

Feel free to reach out if you have any questions or need assistance while playing the game. Enjoy your time playing Gomoku!