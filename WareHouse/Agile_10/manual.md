# Hit and Blow Game User Manual

## Introduction

Welcome to the Hit and Blow Game! This game is a fun and challenging guessing game where you have to predict a three-digit number with different digits. The game will provide feedback on your guesses, indicating if you have a hit (correct number and correct position) or a blow (correct number but incorrect position). The goal is to guess the number within seven tries.

## Installation

To play the Hit and Blow Game, you need to have Python installed on your computer. You can download Python from the official website: [Python.org](https://www.python.org/downloads/).

Once you have Python installed, you can follow these steps to install the game:

1. Open a terminal or command prompt.
2. Navigate to the directory where you have saved the game files.
3. Run the following command to install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

   This will install the necessary packages, including tkinter.

## Starting the Game

To start the Hit and Blow Game, follow these steps:

1. Open a terminal or command prompt.
2. Navigate to the directory where you have saved the game files.
3. Run the following command to start the game:

   ```
   python main.py
   ```

   This will launch the game window.

## Gameplay

Once the game window is open, you can start playing the Hit and Blow Game. Here's how the game works:

1. The game will generate a random three-digit number with different digits.
2. You need to enter a three-digit number in the input field and click the "Submit" button.
3. The game will provide feedback on your guess:
   - If both the number and the digit position are correct, it will be counted as a hit.
   - If only the number is correct but the digit position is incorrect, it will be counted as a blow.
4. The game will display the number of remaining lives (tries) you have.
5. If you guess the number correctly within seven tries, you win the game.
6. If you run out of lives without guessing the number correctly, you lose the game.
7. If you enter an invalid input (not a three-digit number or containing duplicate digits), the game will ask you to enter a valid input without reducing the number of lives.

## Ending the Game

The game will end in one of the following ways:

- If you guess the number correctly within seven tries, the game will display a message congratulating you on winning.
- If you run out of lives without guessing the number correctly, the game will display the correct number and inform you that the game is over.

## Have Fun!

That's it! You are now ready to play the Hit and Blow Game. Enjoy the challenge of guessing the number and have fun!