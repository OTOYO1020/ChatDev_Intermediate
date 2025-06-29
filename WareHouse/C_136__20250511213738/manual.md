Here is the `manual.md` file for the Gomoku game application, detailing the main functions, installation instructions, and how to play the game.

```markdown
# Gomoku Game

Welcome to the Gomoku Game application! This is a simple implementation of the classic board game Gomoku, where two players take turns placing their pieces on a 15x15 grid. The first player to align five of their pieces in a row (horizontally, vertically, or diagonally) wins the game.

## Main Functions

- **Play in Console**: Start a game in the console where players can input their moves by specifying the row and column of their desired position on the board.
- **Graphical User Interface (GUI)**: Play the game using a user-friendly GUI built with Tkinter, allowing players to click on the board to make their moves.
- **Game Logic**: The game checks for valid moves, handles turn-taking between players, and determines when a player has won.

## Installation Instructions

To run the Gomoku game, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. **Install Python**: If you haven't already, download and install Python from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: Clone the repository containing the Gomoku game code to your local machine.
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

3. **Install Dependencies**: Create a virtual environment (optional but recommended) and install the required dependencies. You can create a virtual environment using `venv`:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

   Then, install the dependencies listed in `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

## How to Play

### Console Version

1. Run the game by executing the `main.py` file:
   ```bash
   python main.py
   ```

2. Follow the prompts in the console to enter your moves. Players take turns entering their desired row and column (0-14) to place their pieces.

3. The game will display the board after each move and announce the winner when a player aligns five pieces.

### GUI Version

1. To play using the GUI, you can modify the `main.py` to instantiate the `GomokuGUI` class instead of the console game. Here’s how you can do that:
   ```python
   from gomoku_gui import GomokuGUI

   if __name__ == "__main__":
       game = GomokuGame()
       gui = GomokuGUI(game)
       gui.run()
   ```

2. Run the modified `main.py` file:
   ```bash
   python main.py
   ```

3. Click on the buttons in the GUI to place your pieces. The current player will be displayed at the bottom, and a message box will inform you when a player wins.

## Future Enhancements

This application is designed to be extensible. Future enhancements may include:
- Adding an AI opponent for single-player mode.
- Implementing different board sizes.
- Adding a scoring system or player statistics.

Enjoy playing Gomoku!
```

This manual provides clear instructions on how to install and play the game, ensuring that users can easily understand and engage with the application.