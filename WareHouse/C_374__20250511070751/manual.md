Here's a detailed user manual for the Gomoku game application, formatted in Markdown:

```markdown
# Gomoku Game

A simple implementation of the classic board game Gomoku, where two players take turns placing their marks on a 15x15 board. The first player to align five of their marks horizontally, vertically, or diagonally wins the game.

## Quick Install

To run the Gomoku game, ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Dependencies

This application does not require any external libraries, so you can run it with just Python.

## 🤔 What is Gomoku?

Gomoku, also known as Five in a Row, is a strategy board game for two players. Players alternate placing their marks (X or O) on the board, and the goal is to be the first to get five of their marks in a row, either horizontally, vertically, or diagonally.

## 🎮 How to Play

1. **Start the Game**: Run the `main.py` file to start the game.
   ```bash
   python main.py
   ```

2. **Game Instructions**:
   - Players take turns to place their marks (X or O) on the board.
   - Enter your move as two integers (row and column) separated by a space.
   - For example, to place your mark in the first row and first column, enter `0 0`.
   - Enter 'exit' to quit the game.

3. **Winning the Game**:
   - The game checks for a winner after each move. If a player aligns five marks in a row, a message will display indicating the winner.
   - If the board is full and no player has won, the game will declare a draw.

4. **Resetting the Game**: After a win or a draw, the game will automatically reset, and players can continue playing.

## 📖 Game Features

- **Interactive Console**: The game runs in the console, providing real-time feedback on the game state.
- **Player Switching**: Players alternate turns automatically.
- **Input Validation**: The game checks for valid moves and prompts players to enter valid coordinates if their input is incorrect.
- **Game Reset**: The game resets automatically after a win or a draw, allowing for continuous play.

## 🛠️ Troubleshooting

- **Invalid Input**: If you enter an invalid move, the game will prompt you to try again without switching players.
- **Move Out of Bounds**: Ensure that your input coordinates are within the range of the board (0 to 14).

## 📞 Support

For any issues or questions regarding the Gomoku game, please reach out to our support team at support@chatdev.com.

Enjoy playing Gomoku!
```

This manual provides a comprehensive overview of the Gomoku game application, including installation instructions, gameplay details, and support information. Let me know if you need any further modifications or additional sections!