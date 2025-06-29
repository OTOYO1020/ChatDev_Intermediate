Here's the user manual for the Gomoku game application, formatted in Markdown as requested:

```markdown
# Gomoku Game

A simple implementation of the classic Gomoku game (also known as Five in a Row) using Python.

## Quick Install

To run the Gomoku game, you need to have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

Once you have Python installed, you can clone the repository or download the files directly. Ensure you have the following files:

- `main.py`
- `gomoku_game.py`

You do not need any additional dependencies for this basic version of the game.

## 🤔 What is Gomoku?

Gomoku is a two-player board game in which players take turns placing their pieces (X or O) on a 15x15 grid. The objective is to be the first to get five of your pieces in a row, either horizontally, vertically, or diagonally.

## 📖 How to Play

1. **Start the Game**: Run the `main.py` file. You can do this by navigating to the directory where the file is located and executing the following command in your terminal or command prompt:

   ```bash
   python main.py
   ```

2. **Making Moves**: 
   - Players take turns entering their moves.
   - Input your move as two numbers separated by a space, representing the row and column (0-indexed). For example, entering `7 7` places your piece in the center of the board.
   - To exit the game at any time, type `-1`.

3. **Winning the Game**: The game checks for a winner after each move. If a player gets five pieces in a row, a message will display indicating the winner.

4. **Playing Again**: After a game ends, you will be prompted to play again. Enter `y` to restart or `n` to exit.

## 🛠️ Game Logic

The game logic is contained in the `gomoku_game.py` file. Here are the main functions:

- **`make_move(x, y)`**: Places a piece on the board and checks for a winner.
- **`check_winner()`**: Checks if the current player has won the game.
- **`reset_game()`**: Resets the game board for a new game.
- **`display_board()`**: Displays the current state of the game board in the console.

## 🎮 Example of Gameplay

```
Player X, enter your move (row and column separated by space) or type -1 to exit: 7 7
. . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . 
. . . . . X . . . . . . . . . 
. . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . 
```

## 📞 Support

For any issues or questions, please reach out to our support team at support@chatdev.com.

Enjoy playing Gomoku!
```

This manual provides a comprehensive overview of the Gomoku game, including installation instructions, gameplay mechanics, and support information, ensuring users can easily understand and enjoy the game.