Here’s a detailed user manual for the Gomoku game application, formatted in Markdown:

```markdown
# Gomoku Game

A simple implementation of the classic Gomoku game (also known as Five in a Row) using Python.

## Quick Install

To run the Gomoku game, you need to have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Clone the Repository

You can clone the repository containing the game code using Git:

```bash
git clone <repository-url>
cd gomoku-game
```

### Install Dependencies

This project does not require any external libraries, but you need to ensure you have Python installed. You can check your Python installation by running:

```bash
python --version
```

## 🤔 What is Gomoku?

Gomoku is a two-player board game in which players take turns placing their symbols (X or O) on a 15x15 grid. The objective is to be the first to get five of your symbols in a row, either horizontally, vertically, or diagonally.

## 📖 How to Play

1. **Start the Game**: Run the main application file to start the game.

   ```bash
   python main.py
   ```

2. **Game Interface**: The game will display the current board state in the console. Empty spaces are represented by a dot (.), while player symbols are represented by X and O.

3. **Making a Move**: To make a move, enter your coordinates in the format `x y`, where `x` is the column number and `y` is the row number (both starting from 0). For example, entering `7 7` places your symbol in the center of the board.

4. **Resetting the Game**: If you want to start a new game, type `reset` and press Enter.

5. **Exiting the Game**: To quit the game at any time, type `exit` and press Enter.

### Example Moves

- To place your symbol at the center of the board, you would enter:
  
  ```
  7 7
  ```

- To reset the game, simply type:

  ```
  reset
  ```

- To exit the game, type:

  ```
  exit
  ```

## 🛠️ Code Structure

The Gomoku game consists of three main files:

- **main.py**: The entry point for the game, handling user input and game flow.
- **board.py**: Contains the `Board` class that manages the game state, including drawing the board, making moves, and checking for a winner.
- **player.py**: Defines the `Player` class, representing each player in the game.

## 📝 Additional Notes

- The game supports two players, X and O, who take turns making moves.
- The game will notify you when a player wins or if the game is over.
- Ensure to enter valid coordinates within the range of the board (0-14).

For any issues or feature requests, please contact the development team.

Enjoy playing Gomoku!
```

This manual provides a comprehensive guide for users to install, run, and play the Gomoku game, ensuring they understand the game mechanics and how to interact with the application.