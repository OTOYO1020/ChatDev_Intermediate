Here is the `manual.md` file for the Gomoku game application:

```markdown
# Gomoku Game

A simple and interactive Gomoku game implemented in Python, allowing players to compete against each other in a 15x15 grid.

## Main Functions

- **Two Modes of Play**: Play in either Console Mode or GUI Mode.
- **Game Logic**: The game handles player turns, checks for wins, and detects draws.
- **User Interface**: The GUI provides a visual representation of the game board and player moves.

## Quick Install

To run the Gomoku game, you need to have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Install Dependencies

You will need the `tkinter` library for the GUI. It usually comes pre-installed with Python. If you don't have it, you can install it using:

```bash
sudo apt-get install python3-tk  # For Ubuntu/Debian
```

For Windows, `tkinter` is included with the standard Python installation.

## 🤔 What is Gomoku?

Gomoku, also known as Five in a Row, is a traditional board game where two players take turns placing their markers (X and O) on a 15x15 grid. The objective is to be the first to get five of your markers in a row, either horizontally, vertically, or diagonally.

## How to Use/Play

1. **Clone the Repository**: Download the game files to your local machine.

   ```bash
   git clone <repository-url>
   cd gomoku-game
   ```

2. **Run the Game**: You can choose to play in Console Mode or GUI Mode.

   - For Console Mode, run:

     ```bash
     python main.py
     ```

   - For GUI Mode, run:

     ```bash
     python main.py
     ```

     Then, select '2' when prompted.

3. **Make Moves**:
   - In Console Mode, enter the row and column numbers (0-14) when prompted.
   - In GUI Mode, click on the desired cell in the grid to place your marker.

4. **Winning the Game**: The game will announce the winner once a player has five markers in a row. If the board is full and no player has won, it will declare a draw.

5. **Resetting the Game**: You can restart the game by running the application again.

## Additional Information

For more details on the game logic and implementation, refer to the source code in the `gomoku_game.py` and `gomoku_gui.py` files.

Enjoy playing Gomoku!
```

This manual provides a comprehensive overview of the Gomoku game, including installation instructions, gameplay mechanics, and additional information for users.