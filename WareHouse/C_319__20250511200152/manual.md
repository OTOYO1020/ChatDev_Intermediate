```markdown
# Gomoku Game

A simple implementation of the classic Gomoku game, where two players take turns placing their pieces on a 15x15 board. The first player to align five of their pieces in a row (horizontally, vertically, or diagonally) wins the game.

## Main Functions

- **Game Logic**: The `GomokuGame` class handles the core game logic, including making moves, checking for wins, and determining draws.
- **Graphical User Interface**: The `GomokuGUI` class provides a user-friendly interface using Tkinter, allowing players to interact with the game visually.
- **Command Line Interface**: The `main.py` module allows players to play the game via the command line, providing a text-based interface for input and output.

## Installation

To set up the environment for the Gomoku game, follow these steps:

1. **Clone the Repository**: If you haven't already, clone the repository containing the game files.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Python**: Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

3. **Install Dependencies**: There are no external dependencies required for this Gomoku game. However, you need to have Tkinter installed for the GUI version. Tkinter is included with most Python installations. If you encounter issues, you can install it using:

   ```bash
   sudo apt-get install python3-tk  # For Ubuntu/Linux
   ```

4. **Create a Requirements File**: Although there are no external dependencies, you can create a `requirements.txt` file for future reference:

   ```plaintext
   # No external dependencies required for the Gomoku game.
   ```

## How to Use/Play

### Graphical User Interface (GUI)

1. **Run the GUI Application**: To start the GUI version of the game, execute the following command:

   ```bash
   python gomoku_gui.py
   ```

2. **Playing the Game**:
   - The game board will be displayed in a window.
   - Players take turns clicking on the cells to place their pieces (X or O).
   - The status label will indicate whose turn it is and announce the winner or if the game ends in a draw.

### Command Line Interface (CLI)

1. **Run the Command Line Application**: To start the command line version of the game, execute the following command:

   ```bash
   python main.py
   ```

2. **Playing the Game**:
   - The game board will be printed in the terminal.
   - Players will be prompted to enter their moves by specifying the row and column (0-14).
   - The game will continue until a player wins or the game ends in a draw.

### Resetting the Game

- In both versions, you can reset the game by restarting the application. The GUI version does not currently have a reset button, but this can be added in future updates.

## Conclusion

Enjoy playing Gomoku! This implementation provides a basic yet functional experience of the classic game. Feel free to modify and enhance the code to add more features or improve the gameplay experience.
```