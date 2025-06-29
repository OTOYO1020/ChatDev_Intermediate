# Gomoku Game User Manual

Welcome to the Gomoku Game! This manual will guide you through the installation, main functions, and how to play the game.

## Quick Install

To run the Gomoku game, you need to have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

Once you have Python installed, you can clone the repository or download the source code. Make sure you have the following files in your project directory:

- `main.py`
- `game.py`
- `gui.py` (optional for GUI version)

You can run the game directly without any additional dependencies.

## 🤔 What is Gomoku?

Gomoku is a traditional board game that is played on a 15x15 grid. The objective of the game is to be the first player to get five of your pieces in a row, either horizontally, vertically, or diagonally. Players take turns placing their pieces on the board, and the game ends when one player wins or the board is full, resulting in a draw.

## 📖 Main Functions

### Console Mode

- **Start the Game**: Run `main.py` to start the game in console mode.
- **Player Input**: Players are prompted to enter their moves in the format "row column" (e.g., `7 7` for the center of the board).
- **Game Status**: The current state of the board is displayed after each move, along with the current player.
- **Winning Condition**: The game checks for a winner after each move. If a player wins, a message will be displayed, and players can choose to play again or exit.

### GUI Mode (Optional)

- **Start GUI**: If you want to play with a graphical interface, you can modify `main.py` to import and instantiate `GomokuGUI` instead of using the console.
- **Click to Play**: Players can click on the grid to place their pieces.
- **Reset Game**: A reset button is available to start a new game without restarting the application.

## How to Play

1. **Start the Game**: Run the command `python main.py` in your terminal.
2. **Choose Game Mode**: You will be prompted to choose between console mode or quit the game.
3. **Make Moves**: 
   - In console mode, enter your move as two integers separated by a space (e.g., `7 7`).
   - In GUI mode, click on the desired cell in the grid.
4. **Winning the Game**: The game will announce the winner once a player achieves five in a row. If the board is full and no player has won, the game will declare a draw.
5. **Play Again**: After a game ends, you can choose to play again or exit.

## Conclusion

Enjoy playing Gomoku! If you have any questions or need further assistance, feel free to reach out for support. Happy gaming!