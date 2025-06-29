```markdown
# Gomoku Game

Welcome to the Gomoku Game! This is a simple console-based implementation of the classic board game Gomoku, where two players take turns placing their pieces on a 15x15 grid. The first player to align five of their pieces horizontally, vertically, or diagonally wins the game.

## Main Functions

- **Play in Console**: Start a new game in the console where two players can take turns entering their moves.
- **Game Logic**: The game checks for valid moves and determines the winner after each turn.
- **Display Board**: The current state of the board is displayed after each move.

## Installation

To run the Gomoku game, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. **Install Python**: Download and install Python from [python.org](https://www.python.org/downloads/).
2. **Clone the Repository**: If you have the code in a repository, clone it to your local machine. If you have the files, ensure they are in the same directory.
3. **Install Dependencies**: This game does not require any external libraries, so you can run it directly with Python.

## How to Use/Play

1. **Run the Game**: Open your terminal or command prompt, navigate to the directory where the `main.py` file is located, and run the following command:
   ```bash
   python main.py
   ```

2. **Main Menu**: You will see a welcome message and a prompt to select an option. Currently, the only option available is to play in the console. Type `1` and press Enter.

3. **Making Moves**: Players will take turns entering their moves. The prompt will ask for the row and column of the move in the format `row column` (e.g., `7 7` for the center of the board).

4. **Winning the Game**: The game will automatically check for a winner after each move. If a player aligns five pieces, a message will display indicating the winner, and the final board will be shown.

5. **Invalid Moves**: If a player tries to make an invalid move (outside the board or on an already occupied space), an error message will be displayed, and they will be prompted to enter a valid move again.

6. **Game Over**: Once a player wins, the game will end, and no further moves can be made.

## Example of Gameplay

```
Welcome to Gomoku!
1. Play in Console
Please select an option (1): 1
Player X, enter your move (row and column): 7 7
Player O, enter your move (row and column): 7 8
Player X, enter your move (row and column): 7 6
Player O, enter your move (row and column): 7 5
Player X, enter your move (row and column): 7 4
Player X wins!
```

## Conclusion

Enjoy playing Gomoku! If you have any questions or feedback, feel free to reach out to the development team.
```