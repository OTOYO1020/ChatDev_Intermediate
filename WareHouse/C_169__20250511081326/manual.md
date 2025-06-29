# Gomoku Game User Manual

Welcome to the Gomoku Game! This manual will guide you through the installation process, main functions of the software, and how to play the game.

## Quick Install

To run the Gomoku game, you need to have Python installed on your machine. If you haven't installed Python yet, please download it from [python.org](https://www.python.org/downloads/).

Once Python is installed, you can set up the environment and run the game by following these steps:

1. **Clone the repository or download the files**:
   - Clone the repository using Git:
     ```bash
     git clone <repository-url>
     ```
   - Or download the files directly and extract them.

2. **Navigate to the project directory**:
   ```bash
   cd path/to/gomoku
   ```

3. **Install any required dependencies** (if applicable):
   - For this basic version, there are no external dependencies. The game runs on standard Python libraries.

## 🤔 What is Gomoku?

Gomoku, also known as Five in a Row, is a classic board game where two players take turns placing their markers (X and O) on a 15x15 grid. The objective is to be the first player to get five of their markers in a row, either horizontally, vertically, or diagonally.

## 📖 Main Functions

### Game Components

- **Board**: The game board is represented as a 15x15 grid where players can place their markers.
- **Cell**: Each cell on the board can either be empty or occupied by a player's marker (X or O).

### Game Flow

1. **Start the Game**: The game starts automatically when you run the `main.py` file.
2. **Display the Board**: The current state of the board is displayed after each turn.
3. **Player Turns**: Players take turns entering their moves by specifying the row and column numbers (0 to 14).
4. **Check for Winner**: After each move, the game checks if there is a winner or if the game is a draw.
5. **Play Again**: At the end of the game, players are prompted to play again or exit.

## 🎮 How to Play

1. **Run the Game**:
   - Open your terminal or command prompt.
   - Navigate to the directory where the game files are located.
   - Run the game using the command:
     ```bash
     python main.py
     ```

2. **Make Your Move**:
   - When prompted, enter your move in the format `row column` (e.g., `7 7` for the center of the board).
   - Ensure that your input is two integers separated by a space.

3. **Winning the Game**:
   - The first player to align five of their markers in a row wins the game.
   - If the board is full and no player has won, the game ends in a draw.

4. **Restart or Exit**:
   - After a game concludes, you will be asked if you want to play again. Enter `y` to restart or `n` to exit.

## 📞 Support

If you encounter any issues or have questions about the game, please reach out to our support team via the contact information provided in the repository.

Enjoy playing Gomoku! May the best player win!