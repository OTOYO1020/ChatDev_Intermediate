Here's a detailed user manual for the Gomoku game, formatted in Markdown:

```markdown
# Gomoku Game

A simple implementation of the classic Gomoku game, also known as Five in a Row. This game allows two players to take turns placing their markers on a 15x15 board, with the objective of being the first to align five markers in a row, either horizontally, vertically, or diagonally.

## Quick Install

To run the Gomoku game, you need to have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

Once Python is installed, you can clone the repository or download the files directly. There are no external dependencies required for this game.

## 🕹️ How to Play

1. **Run the Game:**
   Open your terminal or command prompt, navigate to the directory where `main.py` is located, and run the following command:
   ```bash
   python main.py
   ```

2. **Game Instructions:**
   - The game will display a 15x15 board with empty spaces represented by dots (.) and players' markers represented by X (Player 1) and O (Player 2).
   - Players take turns entering their moves in the format `row,col`, where both `row` and `col` are integers between 0 and 14 (inclusive).
   - For example, to place a marker in the top-left corner, you would enter `0,0`.

3. **Winning the Game:**
   - The first player to align five markers in a row (horizontally, vertically, or diagonally) wins the game.
   - If a player attempts to place a marker in an already occupied space, they will be prompted to try again.

4. **Resetting the Game:**
   - If you wish to reset the game at any point, you can call the `reset_game` method. This will clear the board and allow you to start a new game.

5. **Ending the Game:**
   - Once a player wins, the game will announce the winner, and you will need to reset the game to play again.

## 📜 Game Features

- **Two Players:** The game supports two players who take turns.
- **Dynamic Board Display:** The current state of the board is displayed after each move.
- **Input Validation:** The game checks for valid moves and provides feedback for invalid inputs.

## 🛠️ Requirements

There are no external dependencies required for the Gomoku game. Just ensure you have Python installed.

## 📖 Documentation

For more information on how to modify or extend the game, you can refer to the code comments within `main.py`. The code is structured to be easily understandable, allowing for potential enhancements such as AI opponents or graphical interfaces.

Enjoy playing Gomoku!
```

This manual provides a comprehensive overview of the game, installation instructions, gameplay details, and additional features, ensuring that users can easily understand and enjoy the Gomoku game.