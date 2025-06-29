Here's a detailed user manual for the Gomoku game application, formatted in Markdown as requested:

```markdown
# Gomoku Game

A simple console-based Gomoku game implemented in Python.

## Quick Install

To run the Gomoku game, you need to have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

Once you have Python installed, you can clone the repository or download the source code. Navigate to the directory where the code is located and run the following command to install any required dependencies:

```bash
pip install -r requirements.txt
```

(Note: As of now, there are no additional dependencies required for this basic version of the Gomoku game.)

## 🤔 What is Gomoku?

Gomoku, also known as Five in a Row, is a traditional board game where two players take turns placing their markers (X and O) on a 15x15 grid. The objective is to be the first to get five of your markers in a row, either horizontally, vertically, or diagonally.

## 🕹️ How to Play

1. **Start the Game**: Run the main Python file to start the game.

   ```bash
   python main.py
   ```

2. **Making Moves**: Players will be prompted to enter their moves in the format of row and column indices (both ranging from 0 to 14). For example, entering `7` for the row and `8` for the column will place your marker in the 8th column of the 7th row.

3. **Winning the Game**: The game will automatically check for a winner after each move. If a player gets five markers in a row, a message will be displayed indicating the winner.

4. **Invalid Moves**: If a player attempts to make an invalid move (e.g., placing a marker on an already occupied space or outside the board), the game will prompt them to try again.

5. **Resetting the Game**: The game can be reset by restarting the application, which will clear the board and allow players to start a new game.

## 📜 Game Logic

The game logic is contained within the `gomoku_game.py` module. Key functions include:

- **make_move(row, col)**: Places the current player's marker on the board if the move is valid and checks for a winner.
- **check_winner(row, col)**: Determines if the current player has won after their move.
- **reset_game()**: Resets the game state to allow for a new game.

## 📖 Code Structure

- **main.py**: The main entry point for the application, responsible for handling user input and displaying the game state.
- **gomoku_game.py**: Contains the core logic of the Gomoku game, including board management and win condition checks.
- **gomoku_gui.py**: (Not included in this version as the user requested a console-only application.)

## 🛠️ Troubleshooting

- **Invalid Input**: If you receive an error message regarding invalid input, ensure you are entering numbers between 0 and 14 for both row and column.
- **Game Not Starting**: Ensure that you have Python installed and that you are running the command from the correct directory where `main.py` is located.

## 📞 Support

For any issues or questions, please contact our support team at support@chatdev.com.

Enjoy playing Gomoku!
```

This manual provides a comprehensive overview of the Gomoku game, including installation instructions, gameplay mechanics, and troubleshooting tips. Let me know if you need any further modifications or additional information!