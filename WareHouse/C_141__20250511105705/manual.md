# Gomoku Game User Manual

## Introduction

Welcome to the Gomoku Game! This is a simple yet engaging two-player game where players take turns placing their pieces on a 15x15 board. The objective is to be the first to get five of your pieces in a row, either horizontally, vertically, or diagonally. 

## Main Functions

### 1. Game Initialization
- The game starts with an empty 15x15 board.
- Players are designated as Player 1 (X) and Player 2 (O).

### 2. Making Moves
- Players take turns to enter their moves by specifying the row and column indices (0-14).
- The game checks for valid moves and updates the board accordingly.

### 3. Winning Condition
- The game checks after each move if the current player has achieved five consecutive pieces in any direction.
- If a player wins, the game announces the winner and offers the option to play again.

### 4. Resetting the Game
- After a game concludes, players can choose to reset the board and start a new game.

## Installation Instructions

To run the Gomoku game, you need to have Python installed on your machine. Follow these steps to set up the environment:

### Step 1: Install Python
Make sure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).

### Step 2: Install Dependencies
Create a `requirements.txt` file with the following content (if you plan to add dependencies in the future):

```
# Add any future dependencies here
```

You can install any required dependencies using pip:

```bash
pip install -r requirements.txt
```

### Step 3: Run the Game
Once you have the environment set up, you can run the game by executing the following command in your terminal:

```bash
python main.py
```

## How to Play

1. **Start the Game**: Run the `main.py` file to start the game.
2. **Enter Moves**: Players will be prompted to enter their moves. Specify the row and column numbers (0-14) for your move.
   - Example: To place your piece in the first row and first column, enter `0` for row and `0` for column.
3. **Invalid Moves**: If you try to place a piece in an already occupied cell or outside the board, you will be prompted to enter a valid move.
4. **Winning the Game**: The game will announce the winner as soon as one player gets five pieces in a row.
5. **Play Again**: After a game ends, you will be asked if you want to play again. Enter `y` for yes or `n` for no.

## Conclusion

Enjoy playing Gomoku! This game is a great way to challenge your strategic thinking and have fun with a friend. If you have any questions or feedback, feel free to reach out to our support team. Happy gaming!