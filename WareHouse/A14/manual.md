# Hit and Blow Game User Manual

## Introduction

Welcome to the Hit and Blow Game! This game is a fun and challenging guessing game where you have to predict a three-digit number with different digits. You will have a limited number of attempts to guess the correct number, and the game will provide feedback on your guesses.

## Installation

To play the Hit and Blow Game, you need to have Python installed on your computer. You can download Python from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

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

Once you start the game, you will see a window with a text input field and a "Guess" button. The game will generate a random three-digit number with different digits, and your task is to guess that number.

To make a guess, enter a three-digit number in the text input field and click the "Guess" button. The game will provide feedback on your guess:

- If both the number and the digit position are correct, it is a "hit".
- If only the number is correct but the digit position is wrong, it is a "blow".

The game will display the number of remaining lives, which is initially set to seven. If you guess the correct number before using all your lives, you win the game. If you run out of lives without guessing the correct number, you lose the game.

If you enter an incorrect input, such as a number with duplicate digits or a number that is not three digits long, the game will ask you to enter a valid input without reducing your remaining lives.

## Ending the Game

The game will end in one of the following ways:

- If you guess the correct number, the game will display a message saying "Congratulations! You guessed the number correctly!" and the "Guess" button will be disabled.
- If you run out of lives without guessing the correct number, the game will display a message saying "Game Over! The number was [correct number]" and the "Guess" button will be disabled.

## Conclusion

Enjoy playing the Hit and Blow Game! Test your guessing skills and see if you can predict the correct number within the given number of lives. Have fun and challenge yourself to improve your score with each play!