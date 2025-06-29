# Hit and Blow Game User Manual

## Introduction

Welcome to the Hit and Blow Game! This game is a fun and challenging number guessing game where you have to predict a three-digit number with different digits. You will be given feedback on your guesses, and you have a limited number of lives to complete the game.

## Installation

To play the Hit and Blow Game, you need to have Python installed on your computer. You can download Python from the official website: [Python.org](https://www.python.org/downloads/)

Once you have Python installed, you can follow these steps to install the game:

1. Open a terminal or command prompt.
2. Navigate to the directory where you have downloaded the game files.
3. Run the following command to install the required dependencies:

```
pip install -r requirements.txt
```

## Starting the Game

To start the Hit and Blow Game, follow these steps:

1. Open a terminal or command prompt.
2. Navigate to the directory where you have downloaded the game files.
3. Run the following command to start the game:

```
python main.py
```

## Gameplay

Once you have started the game, you will see a window with a label saying "Welcome to Hit and Blow Game!" and a text box where you can enter your guesses.

To play the game, follow these rules:

1. Enter a three-digit number in the text box.
2. Press the "Submit" button or press Enter to submit your guess.
3. The game will provide feedback on your guess in the form of "Hits" and "Blows".
   - A "Hit" means that both the number and the digit position are correct.
   - A "Blow" means that the number is correct, but the digit position is wrong.
4. The game will display the number of remaining lives.
5. Keep guessing until you either guess the correct number or run out of lives.

## Game Rules

To ensure a fair and enjoyable gameplay experience, the Hit and Blow Game follows these rules:

1. You have a total of seven lives to complete the game.
2. If you guess the correct number halfway through the game, the game will end as if you answered correctly.
3. If you enter an incorrect input, such as a number with duplicate digits or a number that is not three digits long, the game will ask you to enter a valid input without deducting a life.
4. If you run out of lives without guessing the correct number, the game will end and display the correct number.

## Conclusion

Enjoy playing the Hit and Blow Game! Test your logic and deduction skills as you try to guess the correct number. Have fun and challenge yourself to complete the game with as few guesses as possible. Good luck!