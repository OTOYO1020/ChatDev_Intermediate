Here's a detailed user manual for the Gomoku game application, formatted in Markdown as requested:

```markdown
# Gomoku Game

A simple implementation of the classic Gomoku game, also known as Five in a Row. This application allows two players to compete against each other by placing their marks on a 15x15 board.

## Main Functions

- **Play the Game**: Players take turns entering their moves by specifying the row and column on the board.
- **Check for Winner**: The game automatically checks for a winner after each move.
- **Draw Condition**: The game can end in a draw if the board is full without any player winning.
- **Reset Game**: Although not explicitly included in the current implementation, the game can be reset to start a new match.

## Installation

To run the Gomoku game, you need to have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

### Environment Dependencies

No additional dependencies are required for this basic implementation. However, ensure you have Python 3.x installed.

## How to Use/Play the Game

1. **Clone the Repository**: If you haven't already, clone the repository containing the game files.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Run the Game**: Execute the `main.py` file to start the game.

   ```bash
   python main.py
   ```

3. **Make Your Move**: 
   - Players will be prompted to enter their moves in the format of row and column indices (both ranging from 0 to 14).
   - For example, entering `7` for the row and `7` for the column places your mark in the center of the board.

4. **Game Flow**:
   - The game alternates between Player X and Player O.
   - If a player wins, the game will display the winner and terminate.
   - If the board is full and no player has won, the game will declare a draw.

5. **Error Handling**: 
   - The game will prompt you with specific error messages if you attempt to make an invalid move (e.g., out of bounds, cell already occupied).
   - Ensure to enter valid numbers between 0 and 14.

6. **End of Game**: After a win or a draw, you can restart the game by running the `main.py` file again.

## Conclusion

Enjoy playing Gomoku! This simple implementation provides a great way to engage in strategic gameplay with a friend. For any issues or suggestions, feel free to reach out to the development team.

```

This manual provides a comprehensive overview of the Gomoku game, including its main functions, installation instructions, and gameplay guidelines. Let me know if you need any further modifications or additions!