# Gomoku Game User Manual

Welcome to the Gomoku Game! This manual will guide you through the installation process, main functions of the software, and how to play the game.

## Quick Install

To run the Gomoku game, you need to have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

Once you have Python installed, you can set up the environment and install the necessary dependencies using pip. Open your terminal or command prompt and run the following command:

```bash
pip install -r requirements.txt
```

(Note: If there are no specific dependencies listed, you can skip this step as the game is built using standard Python libraries.)

## 🤔 What is Gomoku?

Gomoku, also known as Five in a Row, is a classic board game played on a grid. The objective of the game is to be the first player to get five of their pieces in a row, either horizontally, vertically, or diagonally.

## 🕹️ How to Play

1. **Starting the Game**: 
   - Run the game by executing the `main.py` file. You can do this by navigating to the directory where the file is located and running:
     ```bash
     python main.py
     ```

2. **Game Interface**:
   - The game will display a 15x15 board in the console. Each cell is represented by a dot (.) if it is empty, an 'X' for Player 1, and an 'O' for Player 2.

3. **Making a Move**:
   - Players take turns entering their moves. When prompted, enter the row and column numbers separated by a space (e.g., `7 7` to place a piece in the center of the board).
   - The game will validate the move. If the move is invalid (e.g., out of bounds or the cell is already occupied), you will be prompted to try again.

4. **Winning the Game**:
   - The game checks for a winner after each move. If a player gets five pieces in a row, the game announces the winner and ends.
   - If the board is full and there is no winner, the game will declare a draw.

5. **Playing Again**:
   - After a game ends, you will be asked if you want to play again. Enter 'y' to restart the game or 'n' to exit.

## 🎮 Main Functions

- **Game Logic**: The game logic is encapsulated in the `GomokuGame` class found in `game.py`. This class handles the board state, player turns, move validation, win checking, and game resetting.
  
- **Display Board**: The `__str__` method in the `GomokuGame` class provides a string representation of the board, which is printed to the console after each turn.

- **Move Handling**: The `make_move` method processes player moves and checks for wins or draws.

- **Reset Functionality**: The `reset_game` method allows players to start a new game without restarting the application.

## 📜 Conclusion

Thank you for choosing the Gomoku Game! We hope you enjoy playing it. If you encounter any issues or have suggestions for improvements, please feel free to reach out to our support team.

Happy gaming!