```markdown
# Gomoku Game

A simple Gomoku game application built in Python, allowing two players to compete against each other on a 15x15 board.

## Main Functions

- **Play the Game**: Players take turns placing their markers (X and O) on the board.
- **Win Detection**: The game checks for a winner after each move, declaring the player who connects five markers in a row (horizontally, vertically, or diagonally) as the winner.
- **Reset Game**: Players can reset the game to start a new match at any time.

## Installation

To run the Gomoku game, you need to have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Environment Dependencies

1. **Install Python**: Ensure you have Python 3.x installed.
2. **Install Tkinter**: Tkinter is included with most Python installations. If you encounter issues, you may need to install it separately depending on your operating system.

### Running the Game

1. **Clone the Repository**: If you have the code in a repository, clone it to your local machine.
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Run the Game**: Execute the `main.py` file to start the game.
   ```bash
   python main.py
   ```

## How to Play

1. **Starting the Game**: When you run the game, the board will be displayed in the console.
2. **Making a Move**: 
   - Enter the row (0-14) and column (0-14) where you want to place your marker.
   - Example: To place your marker in the center of the board, you would enter `7` for the row and `7` for the column.
3. **Winning the Game**: The game will automatically check for a winner after each move. If a player connects five markers in a row, a message will be displayed announcing the winner.
4. **Resetting the Game**: After a game ends, you will be prompted to play again. Enter 'y' to reset the game or 'n' to exit.

## GUI Version

For a graphical user interface (GUI) version of the Gomoku game, you can run the `gui.py` file. This version provides a visual representation of the board and allows players to click on the grid to make their moves.

### Running the GUI

1. **Run the GUI**: Execute the `gui.py` file to start the GUI version of the game.
   ```bash
   python gui.py
   ```

2. **Interacting with the GUI**: Click on the squares of the board to place your marker. Use the "Reset Game" button to start a new game.

## Conclusion

Enjoy playing Gomoku! This game is a great way to challenge your strategic thinking and have fun with a friend. If you encounter any issues or have suggestions for improvements, please reach out to our support team.
```