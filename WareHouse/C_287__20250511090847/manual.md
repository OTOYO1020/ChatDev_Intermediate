# Gomoku Game User Manual

Welcome to the Gomoku Game! This manual will guide you through the installation process, main functions of the software, and how to play the game.

## Quick Install

To run the Gomoku game, you need to have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

Once Python is installed, you can run the game without any additional dependencies. Simply clone or download the repository containing the game files.

## 🤔 What is Gomoku?

Gomoku, also known as Five in a Row, is a strategy board game for two players. The objective is to be the first to get an unbroken row of five pieces, either horizontally, vertically, or diagonally.

## 📦 Main Functions

### 1. Game Initialization
- The game initializes a 15x15 board with empty spaces.
- Players take turns to place their pieces on the board.

### 2. Making a Move
- Players can input their desired row and column to place their piece.
- The game checks if the move is valid (within bounds and not already occupied).

### 3. Checking for a Winner
- After each move, the game checks if the current player has won by forming a line of five pieces in any direction (horizontal, vertical, or diagonal).

### 4. Resetting the Game
- The game can be reset at any time, clearing the board and starting fresh.

## 🎮 How to Play

1. **Start the Game**: Run the `main.py` file to start the game.
   ```bash
   python main.py
   ```

2. **View the Board**: The current state of the board will be displayed in the console.

3. **Make a Move**:
   - Enter the row number (0-14) where you want to place your piece.
   - Enter the column number (0-14) where you want to place your piece.
   - If the move is valid, your piece will be placed on the board.

4. **Winning the Game**: The game will announce the winner when a player successfully places five pieces in a row.

5. **Invalid Moves**: If you attempt to place a piece in an occupied cell or outside the board boundaries, you will receive an error message, and you can try again.

6. **Resetting the Game**: If you want to start a new game, you can reset the game by running the `main.py` file again.

## 📜 Example of Gameplay

```
Current Board:
  |   |   |   |   |   |   |   |   |   |   |   |   |   |   |  
  |   |   |   |   |   |   |   |   |   |   |   |   |   |   |  
  |   |   |   |   |   |   |   |   |   |   |   |   |   |   |  
  |   |   |   |   |   |   |   |   |   |   |   |   |   |   |  
  |   |   |   |   |   |   |   |   |   |   |   |   |   |   |  
  |   |   |   |   |   |   |   |   |   |   |   |   |   |   |  
  |   |   |   |   |   |   |   |   |   |   |   |   |   |   |  
  |   |   |   |   |   |   |   |   |   |   |   |   |   |   |  
  |   |   |   |   |   |   |   |   |   |   |   |   |   |   |  
  |   |   |   |   |   |   |   |   |   |   |   |   |   |   |  
  |   |   |   |   |   |   |   |   |   |   |   |   |   |   |  
  |   |   |   |   |   |   |   |   |   |   |   |   |   |   |  
  |   |   |   |   |   |   |   |   |   |   |   |   |   |   |  
  |   |   |   |   |   |   |   |   |   |   |   |   |   |   |  
  |   |   |   |   |   |   |   |   |   |   |   |   |   |   |  

Current Player: X
Enter row (0-14): 7
Enter column (0-14): 7
```

## 🛠️ Troubleshooting

If you encounter any issues while running the game, please ensure that:
- You have Python installed correctly.
- You are running the game from the directory where the `main.py` file is located.

For further assistance, feel free to reach out to our support team.

Enjoy playing Gomoku!