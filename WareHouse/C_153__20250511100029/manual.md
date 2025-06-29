Here's a detailed user manual for the Gomoku game software, formatted in Markdown:

```markdown
# Gomoku Game

A simple implementation of the classic Gomoku game, allowing players to compete against each other either through a console interface or a graphical user interface (GUI).

## Main Functions

- **Game Logic**: The game is played on a 15x15 board where players take turns placing their markers (X and O). The first player to align five markers in a row (horizontally, vertically, or diagonally) wins the game.
- **Console Mode**: Play the game in a text-based console interface.
- **GUI Mode**: Play the game using a graphical interface built with Tkinter.
- **Reset Game**: Restart the game at any time using the reset functionality.

## Installation

To run the Gomoku game, you need to have Python installed on your machine. Follow these steps to set up your environment:

1. **Install Python**: Download and install Python from [python.org](https://www.python.org/downloads/). Ensure that you check the box to add Python to your PATH during installation.

2. **Clone the Repository**: Clone the repository containing the Gomoku game code to your local machine.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

3. **Install Dependencies**: Create a `requirements.txt` file (if not already provided) and install any necessary dependencies. For this project, you may not need additional packages beyond Python's standard library, but if you do, you can install them using:

   ```bash
   pip install -r requirements.txt
   ```

## How to Play

### Starting the Game

1. **Run the Game**: Navigate to the directory where the game files are located and run the main script.

   ```bash
   python main.py
   ```

2. **Choose Mode**: You will be prompted to choose between two modes:
   - **Console Mode**: Enter `1` to play in the console.
   - **GUI Mode**: Enter `2` to play with the graphical interface.

### Playing in Console Mode

- The game board will be printed in the console.
- Players will be prompted to enter their moves by specifying the row and column (0-14).
- The game will indicate if a move is valid or if a player has won.

### Playing in GUI Mode

- A window will open displaying the game board.
- Players can click on the buttons representing the cells to make their moves.
- The current player's turn will be displayed at the top of the window.
- A reset button is available to start a new game at any time.

### Ending the Game

- The game ends when a player aligns five markers in a row, and a message will indicate the winner.
- Players can reset the game to start over.

## Troubleshooting

- **Invalid Input**: If you enter an invalid move (e.g., out of bounds or occupied cell), the game will notify you.
- **Game Over**: If the game is over, you will not be able to make further moves until the game is reset.

## Conclusion

Enjoy playing Gomoku! Whether you prefer the simplicity of the console or the interactivity of the GUI, this game offers a fun way to challenge your friends or practice your strategy skills.
```

This manual provides a comprehensive overview of the Gomoku game, including installation instructions, gameplay details, and troubleshooting tips, ensuring that users can easily understand and enjoy the software.