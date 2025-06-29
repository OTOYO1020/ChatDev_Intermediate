Here's a detailed user manual for the Gomoku game application, formatted in Markdown:

```markdown
# Gomoku Game

Welcome to the Gomoku Game! This application allows you to play the classic board game Gomoku (also known as Five in a Row) against another player. The game is played on a 15x15 grid, where players take turns placing their pieces (X and O) on the board. The first player to align five of their pieces in a row (horizontally, vertically, or diagonally) wins the game.

## Main Functions

- **Play the Game**: Players take turns clicking on the board to place their pieces.
- **Reset Game**: Start a new game at any time using the reset button.
- **Game Status**: The current player's turn and game status (ongoing or over) are displayed.

## Installation

To run the Gomoku game, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. **Install Python**: Download and install Python from [python.org](https://www.python.org/downloads/).

2. **Install Dependencies**: Create a `requirements.txt` file with the following content:

   ```
   tkinter
   ```

   Then, install the dependencies using pip:

   ```bash
   pip install -r requirements.txt
   ```

   Alternatively, if you prefer to install `tkinter` explicitly, you can do so with:

   ```bash
   pip install tk
   ```

## How to Use/Play

1. **Run the Application**: Open a terminal or command prompt, navigate to the directory containing the game files, and run the following command:

   ```bash
   python main.py
   ```

2. **Game Interface**: The game window will open, displaying the 15x15 board, the current player's turn, and a reset button.

3. **Making Moves**: Click on an empty cell on the board to place your piece. The pieces will be represented as:
   - **Black Circle**: Player X
   - **White Circle**: Player O

4. **Winning the Game**: The game checks for a winner after each move. If a player aligns five pieces in a row, a message will display indicating that the player has won.

5. **Resetting the Game**: If you wish to start a new game, click the "Reset Game" button. This will clear the board and reset the game status.

## Troubleshooting

- **Game Not Starting**: Ensure that Python and the required dependencies are correctly installed.
- **Invalid Moves**: If you receive an invalid move message, ensure that you are clicking within the board limits and that the cell is not already occupied.

## Conclusion

Enjoy playing Gomoku! If you have any questions or feedback, please reach out to our support team.
```

This manual provides a comprehensive overview of the Gomoku game, including installation instructions, gameplay mechanics, and troubleshooting tips, ensuring that users can easily understand and enjoy the application.