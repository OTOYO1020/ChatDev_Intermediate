Here's the user manual for the basic Gomoku game, formatted in Markdown as requested:

```markdown
# Gomoku Game

A simple text-based implementation of the classic Gomoku game, where two players take turns placing their pieces on a 15x15 board. The first player to align five of their pieces in a row (horizontally, vertically, or diagonally) wins the game.

## Quick Install

To run the Gomoku game, you need to have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

Once Python is installed, you can run the game without any additional dependencies. Simply clone the repository or download the files.

## 🕹️ How to Play

1. **Run the Game**: Open your terminal or command prompt, navigate to the directory where the game files are located, and run the following command:
   ```bash
   python main.py
   ```

2. **Game Instructions**:
   - The game will display the current state of the board.
   - Players take turns entering their moves by specifying the row and column (both between 0 and 14).
   - Player "X" goes first, followed by Player "O".
   - To make a move, enter the row and column numbers when prompted.

3. **Winning the Game**:
   - The game checks for a winner after each move. If a player aligns five pieces in a row, they will be declared the winner.
   - If the board is full and no player has won, the game will end in a draw.

4. **Invalid Moves**:
   - If a player tries to place a piece in an occupied cell or outside the board boundaries, an error message will be displayed, and the player will be prompted to try again.

5. **Game Reset**:
   - The game can be restarted by simply running the `main.py` file again.

## 📖 Documentation

For more information about the game logic and implementation, you can refer to the following files:

- **`gomoku_game.py`**: Contains the core logic of the Gomoku game, including move validation, winner checking, and board management.
- **`main.py`**: The entry point of the application that handles user input and game flow.
- **`gomoku_gui.py`**: This module was initially intended for a graphical user interface but is not currently needed as we are implementing a text-based interface.

## 🛠️ Troubleshooting

- **Python Not Found**: Ensure that Python is installed and added to your system's PATH.
- **Invalid Input**: If you receive an error about invalid input, make sure to enter numbers between 0 and 14 for both row and column.

## 🎉 Enjoy the Game!

We hope you enjoy playing Gomoku! If you have any questions or feedback, feel free to reach out.
```

This manual provides a comprehensive overview of the Gomoku game, including installation instructions, gameplay mechanics, and troubleshooting tips. Let me know if you need any modifications or additional information!