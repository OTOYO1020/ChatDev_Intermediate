Here is the user manual for the Gomoku game, formatted in Markdown:

```markdown
# Gomoku Game

A simple implementation of the classic Gomoku game, also known as Five in a Row. This game can be played in both console and GUI modes.

## Quick Install

To run the Gomoku game, you need to have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

Once Python is installed, you can run the game directly without any additional dependencies.

## 🤔 What is Gomoku?

Gomoku is a strategy board game for two players, where the objective is to get five of one's own stones in a row, either horizontally, vertically, or diagonally. The game is played on a 15x15 board.

## 🛠️ How to Use/Play

### Running the Game

1. **Download the Game Files**: Clone or download the repository containing the game files: `gomoku_game.py`, `gomoku_gui.py`, and `main.py`.

2. **Open a Terminal/Command Prompt**: Navigate to the directory where the game files are located.

3. **Run the Game**: Execute the following command:
   ```bash
   python main.py
   ```

4. **Choose Your Mode**: You will be prompted to choose between console (C) or GUI (G) mode:
   - Enter `C` for console mode.
   - Enter `G` for GUI mode.

### Playing in Console Mode

- After choosing console mode, the game board will be displayed in the terminal.
- Players take turns entering their moves by specifying the row and column numbers (0-14).
- The game will announce the winner once a player gets five in a row.
- If you want to play again after the game ends, simply type `yes` when prompted.

### Playing in GUI Mode

- After choosing GUI mode, a window will open displaying the Gomoku board.
- Click on the cells to place your stones (X for Player 1 and O for Player 2).
- The current player's turn will be displayed at the top.
- If a player wins, the game will announce the winner and disable further moves.
- Click the "Reset Game" button to start a new game.

## 🎮 Game Rules

- Players alternate turns placing their stones on the board.
- The first player to align five of their stones in a row (horizontally, vertically, or diagonally) wins the game.
- If a player attempts to place a stone in an already occupied cell, an error message will be displayed.

## 📄 Code Structure

- **gomoku_game.py**: Contains the game logic, including the `GomokuGame` class that manages the game state and rules.
- **gomoku_gui.py**: Manages the graphical user interface for the game using Tkinter.
- **main.py**: The entry point of the application, allowing users to choose between console and GUI modes.

## 📞 Support

If you encounter any issues or have questions about the game, please reach out to our support team at support@chatdev.com.

Enjoy playing Gomoku!
```

This manual provides a comprehensive overview of the Gomoku game, including installation instructions, gameplay details, and code structure. It is designed to help users easily understand how to use the software.