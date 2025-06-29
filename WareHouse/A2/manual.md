# Hit and Blow Game User Manual

## Introduction

Welcome to the Hit and Blow Game! This game is a fun and challenging number guessing game where you have to predict a randomly generated three-digit number. The game will provide feedback on your guesses, telling you if you have a hit (correct number and correct position) or a blow (correct number but incorrect position). The goal is to guess the number within a limited number of tries.

## Installation

To play the Hit and Blow Game, you need to have Python installed on your computer. You can download Python from the official website: [Python.org](https://www.python.org/downloads/)

Once you have Python installed, you can follow these steps to install the game:

1. Open a terminal or command prompt.
2. Navigate to the directory where you want to install the game.
3. Clone the repository by running the following command:
   ```
   git clone https://github.com/ChatDevOrg/hit-and-blow-game.git
   ```
4. Change into the game directory:
   ```
   cd hit-and-blow-game
   ```
5. Install the required dependencies by running the following command:
   ```
   pip install -r requirements.txt
   ```

## How to Play

1. Open a terminal or command prompt.
2. Navigate to the game directory.
3. Run the game by executing the following command:
   ```
   python main.py
   ```
4. A window will appear with the game interface.
5. Read the instructions on the screen and enter a three-digit number in the input field.
6. Click the "Submit" button or press Enter to submit your guess.
7. The game will provide feedback on your guess, indicating the number of hits and blows.
8. Continue guessing until you either guess the correct number or run out of lives.
9. If you guess the correct number, the game will congratulate you and end.
10. If you run out of lives, the game will reveal the correct number and end.

## Game Rules

- The number to guess is a randomly generated three-digit number with different digits.
- Each time you make a guess, the game will tell you the number of hits (correct number and correct position) and blows (correct number but incorrect position).
- You have a total of seven lives to guess the number.
- If you guess the number correctly before using all seven lives, the game will end.
- If you guess the number correctly halfway through (when you have three or fewer lives remaining), the game will end.
- If you enter an invalid input (not a three-digit number or containing duplicate digits), the game will ask you to enter a valid input without reducing your remaining lives.

## Enjoy the Game!

Have fun playing the Hit and Blow Game! Test your guessing skills and see if you can guess the correct number within the given number of lives. Good luck!