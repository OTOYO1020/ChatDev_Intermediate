```markdown
# Gomoku Game

A simple implementation of the classic Gomoku game, also known as Five in a Row. This game allows two players to compete against each other by placing their pieces on a 15x15 board, with the goal of being the first to align five of their pieces in a row, either horizontally, vertically, or diagonally.

## Main Functions

- **Game Logic**: The core logic for the Gomoku game is implemented in the `gomoku_game.py` file. It handles the game state, player turns, and win conditions.
- **Console Mode**: The game can be played in a console mode where players input their moves via the command line.
- **Graphical User Interface (GUI)**: An optional GUI is provided using Tkinter, allowing players to click on the board to make their moves visually.

## Installation

To run the Gomoku game, you need to have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Environment Dependencies

To ensure that all necessary dependencies are installed, create a `requirements.txt` file with the following content:

```
tkinter
```

You can install the dependencies using pip:

```bash
pip install -r requirements.txt
```

## How to Use / Play the Game

### Running the Console Version

1. Open your terminal or command prompt.
2. Navigate to the directory where `main.py` is located.
3. Run the game using the following command:

   ```bash
   python main.py
   ```

4. Follow the on-screen prompts to play the game. Players will take turns entering their moves in the format "row column" (e.g., "7 7" for the center of the board).

### Running the GUI Version

1. Ensure you have the Tkinter library installed (it comes pre-installed with most Python distributions).
2. Open your terminal or command prompt.
3. Navigate to the directory where `gomoku_gui.py` is located.
4. Run the GUI version using the following command:

   ```bash
   python gomoku_gui.py
   ```

5. Click on the board to place your pieces. The current player will be displayed, and the game will announce the winner or if the game ends in a draw.

## Game Rules

- Players take turns placing their pieces (X and O) on the board.
- The first player to align five of their pieces in a row (horizontally, vertically, or diagonally) wins the game.
- If all cells are filled and no player has won, the game ends in a draw.

## Future Enhancements

This implementation can be expanded with additional features such as:

- AI opponent for single-player mode.
- Enhanced GUI with animations and sound effects.
- Online multiplayer functionality.

For any issues or feature requests, please reach out to the development team.

Happy gaming!
```