Here's a detailed user manual for the Gomoku game application, formatted in Markdown:

```markdown
# Gomoku Game

A simple and engaging Gomoku game application built using Python. This application allows two players to compete against each other by placing their marks on a 15x15 board, aiming to get five in a row.

## Main Functions

- **Two-player Mode**: Play against another human player.
- **Game Logic**: The game checks for valid moves and determines the winner.
- **Graphical User Interface (GUI)**: An intuitive interface using Tkinter for easy interaction.
- **Reset Game**: Option to reset the game at any time.

## Installation

To run the Gomoku game, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. **Install Python**: Download and install Python from the [official website](https://www.python.org/downloads/).

2. **Install Tkinter**: Tkinter is usually included with Python installations. If not, you can install it using the following command:
   - For Windows: Tkinter is included with the standard Python installation.
   - For macOS: Tkinter is included with the standard Python installation.
   - For Linux: You may need to install it separately. Use the command:
     ```bash
     sudo apt-get install python3-tk
     ```

3. **Clone the Repository**: Clone the repository containing the game files.
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

4. **Run the Game**: You can run the game using the following command:
   ```bash
   python main.py
   ```
   or, if you want to use the GUI version:
   ```bash
   python gomoku_gui.py
   ```

## How to Play

1. **Starting the Game**: Launch the application by running `main.py` for console mode or `gomoku_gui.py` for GUI mode.

2. **Making Moves**:
   - In console mode, players will be prompted to enter their moves by specifying the row and column (0-14).
   - In GUI mode, simply click on the desired cell on the board to place your mark.

3. **Winning the Game**: The first player to align five of their marks (either 'X' or 'O') in a row, either horizontally, vertically, or diagonally, wins the game.

4. **Resetting the Game**: You can reset the game at any time by clicking the "Reset Game" button in the GUI. In console mode, you can restart the game by running the application again.

5. **Exiting the Game**: In console mode, you can exit the game by typing 'n' when prompted to continue playing. In GUI mode, simply close the application window.

## Additional Information

For any issues or feature requests, please contact our support team at [support@chatdev.com](mailto:support@chatdev.com).

Enjoy playing Gomoku!
```

This manual provides a comprehensive guide for users to understand the functionality of the Gomoku game application, installation steps, and gameplay instructions.