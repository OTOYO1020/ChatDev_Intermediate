# Gomoku Game User Manual

Welcome to the Gomoku Game! This manual will guide you through the installation process, main functionalities, and how to play the game.

## Quick Install

To run the Gomoku game, you need to have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

Once you have Python installed, you can set up the environment and run the game using the following steps:

1. **Clone the repository or download the files**:
   - Ensure you have the `gomoku.py`, `gomoku_gui.py`, and `main.py` files in the same directory.

2. **Install Tkinter** (if not already installed):
   - Tkinter is usually included with Python installations. If you encounter any issues, you can install it using:
     ```bash
     sudo apt-get install python3-tk  # For Ubuntu/Linux
     ```
   - For Windows, Tkinter should be included with the standard Python installation.

3. **Run the game**:
   - Open your terminal or command prompt.
   - Navigate to the directory where the files are located.
   - Run the following command:
     ```bash
     python main.py
     ```

## 🤔 What is Gomoku?

Gomoku, also known as Five in a Row, is a strategy board game for two players. The objective is to be the first to get an unbroken row of five stones, either horizontally, vertically, or diagonally.

## 🕹️ Main Functions

### Game Modes

1. **Console Version**: Play the game in a text-based interface.
2. **GUI Version**: Play the game using a graphical user interface.

### Game Features

- **Two Players**: Players take turns placing their stones on the board.
- **Winning Condition**: The game checks for a winner after each move.
- **Reset Game**: You can reset the game to start over.
- **Invalid Move Handling**: The game will notify you if you make an invalid move.

## 🎮 How to Play

1. **Choose Game Mode**:
   - When you run the game, you will be prompted to choose between the console version (`1`) or the GUI version (`2`).

2. **Making Moves**:
   - In the console version, you will be asked to enter the row and column numbers (0-14) for your move.
   - In the GUI version, click on the board to place your stone.

3. **Winning the Game**:
   - The game will announce the winner once a player has five stones in a row.

4. **Resetting the Game**:
   - If you want to start a new game, simply restart the application.

## 📖 Documentation

For further details on the game logic and implementation, you can refer to the source code in the `gomoku.py` and `gomoku_gui.py` files. 

Feel free to explore and enjoy the game! If you have any questions or feedback, please reach out to our support team. Happy gaming!