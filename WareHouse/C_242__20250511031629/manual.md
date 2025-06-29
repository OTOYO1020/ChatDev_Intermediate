Here is the user manual for the Gomoku game application, formatted in Markdown:

```markdown
# Gomoku Game

A simple implementation of the classic Gomoku game, also known as Five in a Row. This application allows two players to compete against each other by placing their pieces on a 15x15 board.

## Main Functions

- **Game Board**: The game is played on a 15x15 grid where players take turns placing their pieces.
- **Player Turns**: Players alternate turns, with Player 1 using "X" and Player 2 using "O".
- **Winning Condition**: The first player to align five of their pieces horizontally, vertically, or diagonally wins the game.
- **Game Reset**: After a game concludes, players can choose to play again with a reset board.

## Installation

To run the Gomoku game, you need to have Python installed on your computer. Follow these steps to set up the environment:

1. **Install Python**: Download and install Python from [python.org](https://www.python.org/downloads/).
2. **Clone the Repository**: Clone the repository containing the game files or download them directly.
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```
3. **Install Dependencies**: This game does not require any external libraries, so you can run it directly with Python.

## How to Play

1. **Run the Game**: Open your terminal or command prompt, navigate to the directory containing the game files, and run the following command:
   ```bash
   python main.py
   ```
2. **Game Interface**: The game board will be displayed in the terminal, showing empty cells represented by ".", Player 1's moves as "X", and Player 2's moves as "O".
3. **Making a Move**: Players will be prompted to enter their move in the format "row column" (e.g., "7 7" for the center of the board).
4. **Winning the Game**: The game will announce the winner once a player aligns five pieces. If a player attempts to make a move after the game has concluded, they will be informed that the game is over.
5. **Playing Again**: After a game ends, players can choose to play again by entering "y" when prompted. If they choose "n", the game will exit.

## Example Gameplay

```
Player 1, enter your move (row and column): 7 7
. | . | . | . | . | . | . | . | . | . | . | . | . | . | .
-------------------------------------------------------------
. | . | . | . | . | . | . | . | . | . | . | . | . | . | .
-------------------------------------------------------------
. | . | . | . | . | . | . | . | . | . | . | . | . | . | .
-------------------------------------------------------------
. | . | . | . | . | . | . | . | . | . | . | . | . | . | .
-------------------------------------------------------------
. | . | . | . | . | . | . | . | . | . | . | . | . | . | .
-------------------------------------------------------------
. | . | . | . | . | . | . | . | . | . | . | . | . | . | .
-------------------------------------------------------------
. | . | . | . | . | . | . | . | . | . | . | . | . | . | .
-------------------------------------------------------------
. | . | . | . | . | . | . | X | . | . | . | . | . | . | .
-------------------------------------------------------------
. | . | . | . | . | . | . | . | . | . | . | . | . | . | .
-------------------------------------------------------------
. | . | . | . | . | . | . | . | . | . | . | . | . | . | .
-------------------------------------------------------------
```

## Conclusion

Enjoy playing Gomoku! If you encounter any issues or have suggestions for improvements, please reach out to our support team.
```

This manual provides a comprehensive overview of the Gomoku game, including installation instructions, gameplay mechanics, and an example of how the game interface looks during play.