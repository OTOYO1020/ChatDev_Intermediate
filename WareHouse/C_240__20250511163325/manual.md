Here's a detailed user manual for the Gomoku game application, formatted in Markdown:

```markdown
# Gomoku Game

A simple implementation of the classic Gomoku game (also known as Five in a Row) using Python.

## Quick Install

To run the Gomoku game, you need to have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

Once you have Python installed, you can run the game directly without any additional dependencies.

## 🤔 What is Gomoku?

Gomoku is a two-player board game in which players take turns placing their marks (X or O) on a 15x15 grid. The objective is to be the first player to get five of their marks in a row, either horizontally, vertically, or diagonally.

## 🛠️ How to Run the Game

1. **Download the Code:**
   - Clone or download the repository containing the `main.py` file.

2. **Navigate to the Directory:**
   - Open your terminal or command prompt and navigate to the directory where `main.py` is located.

3. **Run the Game:**
   - Execute the following command:
     ```bash
     python main.py
     ```

4. **Playing the Game:**
   - The game will prompt you to enter your move in the format `row column` (e.g., `7 7`).
   - Players take turns entering their moves.
   - The game will display the current state of the board after each move.
   - The game ends when one player gets five in a row or if the board is full (resulting in a draw).

## 🎮 Game Rules

- Players alternate turns, with Player X going first.
- A valid move consists of placing your mark in an empty cell on the board.
- The game checks for a winner after each move. If a player wins, a message will be displayed, and the game will end.
- If the board is full and no player has won, the game will declare a draw.

## 📜 Example of Gameplay

```
Player X, enter your move (row and column): 7 7
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
```

## 📖 Documentation

For more information about the game logic and code structure, you can refer to the comments within the `main.py` file. The code is structured to be easily understandable and modifiable for further enhancements.

## 🛠️ Future Improvements

- Implement a graphical user interface (GUI) for a better user experience.
- Add an AI opponent for single-player mode.
- Include options for different board sizes.

Feel free to reach out if you have any questions or need further assistance!
```

This manual provides a comprehensive overview of the Gomoku game, including installation instructions, gameplay rules, and future improvement suggestions. It should serve as a helpful guide for users looking to play the game.