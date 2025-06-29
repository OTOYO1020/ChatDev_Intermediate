Here's the user manual for the Gomoku game, formatted in Markdown:

```markdown
# Gomoku Game

A simple implementation of the classic Gomoku game, also known as Five in a Row. This game allows two players to compete against each other by placing their marks on a 15x15 board, aiming to connect five of their marks in a row.

## Main Functions

- **Game Logic**: The game is played on a 15x15 board where players take turns to place their marks ('X' and 'O').
- **Winning Condition**: The game checks for a winner after each move. A player wins by placing five of their marks consecutively in a row, column, or diagonal.
- **Draw Condition**: The game detects if the board is full, resulting in a draw.
- **Reset Game**: Players can reset the game to start a new match.
- **Print Board**: The current state of the game board is displayed in the console.

## Installation

To run the Gomoku game, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. **Install Python**: Download and install Python from the [official website](https://www.python.org/downloads/).

2. **Clone the Repository**: If you haven't already, clone the repository containing the game files.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

3. **Install Dependencies**: There are no external dependencies required for this game, so you can skip this step. The game runs on standard Python libraries.

## How to Play

1. **Run the Game**: Navigate to the directory containing `main.py` and run the following command in your terminal:

   ```bash
   python main.py
   ```

2. **Game Instructions**:
   - The game will display the current state of the board.
   - Players take turns entering their moves by specifying the row and column (both between 0 and 14).
   - The game will inform players if they have won, if the game is a draw, or if they have made an invalid move.

3. **Example Moves**:
   - Player X: Enter `7` for row and `7` for column to place an 'X' in the center of the board.
   - Player O: Enter `7` for row and `8` for column to place an 'O' next to it.

4. **End of Game**: The game will automatically announce the winner or if the game ends in a draw. You can reset the game by running the program again.

## Conclusion

Enjoy playing Gomoku with your friends! For any issues or feedback, please reach out to our support team.
```

This manual provides a comprehensive overview of the Gomoku game, including its main functions, installation instructions, and gameplay guidelines. Let me know if you need any modifications or additional information!