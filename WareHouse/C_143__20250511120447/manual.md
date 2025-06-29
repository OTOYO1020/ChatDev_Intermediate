Here's a detailed user manual for the Gomoku game application, formatted in Markdown:

```markdown
# Gomoku Game

A simple implementation of the classic Gomoku game, also known as Five in a Row.

## Quick Install

To run the Gomoku game, you need to have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

Once you have Python installed, you can run the game directly without any additional dependencies.

## 🤔 What is Gomoku?

Gomoku is a two-player board game in which players take turns placing their markers (X or O) on a 15x15 grid. The objective is to be the first to get five of your markers in a row, either horizontally, vertically, or diagonally.

## 📖 How to Play

1. **Starting the Game**: 
   - Run the `main.py` file to start the game.
   - The game will display an empty board and prompt the first player (X) to make a move.

2. **Making a Move**:
   - Players take turns entering their moves in the format `row col`, where `row` and `col` are integers between 0 and 14 (inclusive).
   - For example, entering `7 7` will place your marker in the center of the board.

3. **Winning the Game**:
   - The game checks for a win after each move. If a player gets five markers in a row, the game will announce the winner and end.

4. **Exiting the Game**:
   - Players can type `exit` at any time to quit the game.

## 🛠️ Game Features

- **2 Player Mode**: Play against another human player.
- **Dynamic Board Display**: The current state of the board is displayed after each move.
- **Input Validation**: The game checks for valid moves and provides feedback for invalid inputs.

## 📦 Game Structure

The game consists of two main files:

- `main.py`: The entry point for the application. It initializes and starts the game.
- `gomoku.py`: Contains the game logic, including board initialization, move handling, win checking, and user interaction.

## 🎮 Example of Play

```
Player X, enter your move as 'row col' (0-14 0-14) or 'exit' to quit: 7 7
 | | | | | | | | | | | | | | | 
-----------------------------
 | | | | | | | | | | | | | | | 
-----------------------------
 | | | | | | | | | | | | | | | 
-----------------------------
 | | | | | | | | | | | | | | | 
-----------------------------
 | | | | | | | | | | | | | | | 
-----------------------------
 | | | | | | | | | | | | | | | 
-----------------------------
 | | | | | | | | | | | | | | | 
-----------------------------
 | | | | | | | | | | | | | | | 
-----------------------------
 | | | | | | | | | | | | | | | 
-----------------------------
 | | | | | | | | | | | | | | | 
-----------------------------
 | | | | | | | | | | | | | | | 
-----------------------------
 | | | | | | | | | | | | | | | 
-----------------------------
 | | | | | | | | | | | | | | | 
-----------------------------
 | | | | | | | | | | | | | | | 
-----------------------------
 | | | | | | | | | | | | | | | 
-----------------------------
Player X wins!
```

## 📞 Support

If you encounter any issues or have questions, please reach out to our support team at support@chatdev.com.

Enjoy playing Gomoku!
```

This manual provides a comprehensive overview of the Gomoku game, including installation instructions, gameplay mechanics, and support information. Let me know if you need any further modifications or additional sections!