```markdown
# Gomoku Game

A simple console-based Gomoku game implemented in Python, allowing two players to compete against each other by placing their marks on a 15x15 board.

## Quick Install

To run the Gomoku game, you need to have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

Once Python is installed, you can clone the repository or download the files directly. Ensure you have the following files in your project directory:

- `main.py`
- `gomoku_game.py`

## 🤔 What is Gomoku?

Gomoku, also known as Five in a Row, is a strategy board game for two players. Players take turns placing their marks (X or O) on a grid. The first player to get five of their marks in a row (horizontally, vertically, or diagonally) wins the game.

## 📖 How to Play

1. **Start the Game:**
   - Run the game by executing the following command in your terminal:
     ```bash
     python main.py
     ```

2. **Making Moves:**
   - Players take turns entering their moves. The game will prompt each player to enter the row and column where they want to place their mark.
   - Valid input for row and column is an integer between 0 and 14.

3. **Winning the Game:**
   - The game checks for a winner after each move. If a player gets five marks in a row, the game will announce the winner.
   - If the board is full and no player has won, the game will declare a draw.

4. **Playing Again:**
   - After a game ends, players will be asked if they want to play again. Enter 'y' to continue or 'n' to exit.

## 🛠️ Dependencies

This application does not require any external dependencies beyond Python itself. Ensure you have Python 3.x installed.

## 📜 Game Logic

- The game board is a 15x15 grid initialized with empty spaces.
- Players alternate turns, starting with Player X.
- The game checks for valid moves and updates the board accordingly.
- The game logic includes checks for winning conditions and board fullness.

## 📞 Support

For any issues or questions regarding the game, please reach out to our support team via the contact information provided in the repository.

Enjoy playing Gomoku!
```