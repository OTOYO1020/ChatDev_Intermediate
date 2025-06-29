Here's the user manual for the Gomoku game application, formatted in Markdown:

```markdown
# Gomoku Game

A simple implementation of the classic Gomoku game, also known as Five in a Row. This application allows players to compete against each other in either console or graphical user interface (GUI) mode.

## Main Functions

- **Two Modes of Play**: Choose between console mode for a text-based experience or GUI mode for a more interactive experience.
- **Game Logic**: The game supports two players, X and O, and checks for win conditions or draws.
- **Reset Game**: Players can reset the game at any time to start a new match.
- **User-Friendly Interface**: The GUI provides buttons for each cell on the board, making it easy to make moves.

## Installation

To run the Gomoku game, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. **Install Python**: Download and install Python from [python.org](https://www.python.org/downloads/).

2. **Install Tkinter**: Tkinter is included with most Python installations. If you encounter issues, you can install it using:
   - For Windows: Tkinter is included with the standard Python installation.
   - For macOS: Tkinter is included with the standard Python installation.
   - For Linux: You may need to install it separately. Use the following command:
     ```bash
     sudo apt-get install python3-tk
     ```

3. **Clone the Repository**: Clone the repository containing the Gomoku game code.
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

4. **Run the Game**: You can run the game by executing the following command:
   ```bash
   python main.py
   ```

## How to Play

1. **Choose Game Mode**: When prompted, select the mode you want to play:
   - Enter `1` for Console mode.
   - Enter `2` for GUI mode.

2. **Making Moves**:
   - In **Console Mode**: You will be prompted to enter your move as two numbers (row and column) separated by a space. For example, entering `7 7` places your mark in the center of the board.
   - In **GUI Mode**: Click on the buttons corresponding to the cells on the board to make your move.

3. **Winning the Game**: The first player to align five of their marks (either X or O) in a row (horizontally, vertically, or diagonally) wins the game. If all cells are filled and no player has won, the game ends in a draw.

4. **Resetting the Game**: You can reset the game at any time by clicking the "Reset Game" button in the GUI.

5. **End of Game**: When the game ends, a message box will display the result (either a win or a draw).

## Conclusion

Enjoy playing Gomoku! This simple yet engaging game can be played with friends or family, providing hours of entertainment. If you encounter any issues or have suggestions for improvements, please reach out to the development team.
```

This manual provides a comprehensive overview of the Gomoku game application, including its main functions, installation instructions, and gameplay details. Let me know if you need any further modifications or additional information!