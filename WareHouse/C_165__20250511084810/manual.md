Here's a detailed user manual for the Gomoku game application, formatted in Markdown:

```markdown
# Gomoku Game

A simple Gomoku game application built using Python. Players take turns placing their pieces on a 15x15 board, aiming to connect five of their pieces in a row, either horizontally, vertically, or diagonally.

## Main Functions

- **Play the Game**: Players alternate turns to place their pieces on the board.
- **Check for Winner**: The game checks for a winner after each move.
- **Reset Game**: Start a new game at any time.
- **Graphical User Interface (GUI)**: The game features a user-friendly GUI built with Tkinter.

## Installation

To run the Gomoku game, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. **Install Python**: Download and install Python from [python.org](https://www.python.org/downloads/).
2. **Install Tkinter**: Tkinter is included with most Python installations. If you encounter issues, you can install it using:
   - For Windows: Tkinter is included with the standard Python installation.
   - For macOS: Tkinter is included with the standard Python installation.
   - For Linux: You may need to install it using your package manager. For example:
     ```bash
     sudo apt-get install python3-tk
     ```

3. **Clone the Repository**: Clone the Gomoku game repository to your local machine.
   ```bash
   git clone <repository-url>
   cd gomoku-game
   ```

4. **Run the Application**: You can run the game using the following command:
   ```bash
   python main.py
   ```
   or, if you want to use the GUI version:
   ```bash
   python gomoku_gui.py
   ```

## How to Play

1. **Starting the Game**: When you run the application, the game board will be displayed.
2. **Making a Move**: 
   - For the console version, enter your move as two numbers (row and column) separated by a space (e.g., `7 7`).
   - For the GUI version, click on the cell where you want to place your piece.
3. **Winning the Game**: The game checks for a winner after each move. If a player connects five pieces in a row, a message will display announcing the winner.
4. **Draw Condition**: If the board is full and no player has won, the game will declare a draw.
5. **Resetting the Game**: You can start a new game at any time by clicking the "New Game" button in the GUI.

## Game Rules

- Players take turns placing their pieces (X and O) on the board.
- The first player to connect five of their pieces in a row wins the game.
- Players must choose empty cells for their moves.

## Troubleshooting

- If you encounter any issues running the game, ensure that you have Python and Tkinter installed correctly.
- For any bugs or feature requests, please contact the development team.

## Conclusion

Enjoy playing Gomoku! We hope you have a great time challenging your friends and family. If you have any feedback or suggestions for improvements, feel free to reach out.

```

This manual provides a comprehensive overview of the Gomoku game, including installation instructions, gameplay details, and troubleshooting tips. Let me know if you need any further modifications or additions!