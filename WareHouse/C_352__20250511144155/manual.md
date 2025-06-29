Here's a detailed user manual for the Gomoku game application, formatted in Markdown as requested.

```markdown
# Gomoku Game

A simple and interactive Gomoku game built using Python and Tkinter.

## Quick Install

To run the Gomoku game, you need to have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

Once Python is installed, you can install the required dependencies using pip:

```bash
pip install tk
```

## 🤔 What is Gomoku?

Gomoku, also known as Five in a Row, is a classic board game where two players take turns placing their pieces (X and O) on a 15x15 grid. The objective is to be the first to get five of your pieces in a row, either horizontally, vertically, or diagonally.

## 🎮 How to Play

1. **Start the Game**: Run the `main.py` file to start the game. You can do this by executing the following command in your terminal:

   ```bash
   python main.py
   ```

2. **Game Interface**: The game window will open, displaying a 15x15 grid. Player 1 (X) will start first.

3. **Making Moves**: Click on the grid to place your piece. The game will alternate turns between Player 1 (X) and Player 2 (O).

4. **Winning the Game**: The game will check for a winner after each move. If a player gets five pieces in a row, a message will display indicating the winner.

5. **Resetting the Game**: If you wish to play again, click the "Reset Game" button to clear the board and start a new game.

## 🛠️ Game Features

- **Interactive GUI**: The game features a graphical user interface built with Tkinter, making it easy to play.
- **Game Logic**: The game logic is implemented in the `gomoku.py` file, ensuring that the game rules are followed correctly.
- **Reset Functionality**: Players can reset the game at any time to start over.

## 📖 Documentation

For more detailed information about the code structure and how the game works, you can refer to the following files:

- **`main.py`**: The main entry point for the application.
- **`gomoku.py`**: Contains the game logic, including move validation and win checking.
- **`gui.py`**: Manages the graphical user interface and user interactions.

## 🐞 Troubleshooting

- **Game is Over**: If you try to make a move after the game has ended, you will receive a message indicating that the game is over. Please reset the game to play again.
- **Out of Bounds Click**: If you click outside the grid, a message will inform you that your click is out of bounds.

## 💬 Support

If you encounter any issues or have questions about the game, feel free to reach out for support.

Enjoy playing Gomoku!
```

This manual provides a comprehensive overview of the Gomoku game, including installation instructions, gameplay mechanics, and troubleshooting tips. Let me know if you need any modifications or additional information!