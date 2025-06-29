# Hit and Blow Game User Manual

## Introduction

Welcome to the Hit and Blow Game! This game is a fun and challenging number guessing game where you have to predict a three-digit number with different digits. You will have a limited number of tries to guess the correct number. The game will provide feedback on your guesses to help you narrow down the correct answer.

## Installation

To play the Hit and Blow Game, you need to have Python installed on your computer. If you don't have Python installed, you can download it from the official Python website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

Once you have Python installed, you can follow these steps to install the game:

1. Open a terminal or command prompt.
2. Navigate to the directory where you have saved the game files.
3. Run the following command to install the required dependencies:

```
pip install tkinter
```

## How to Play

To start the game, open a terminal or command prompt and navigate to the directory where you have saved the game files. Run the following command:

```
python main.py
```

A window will open with the game interface. The window will display an instruction to enter a three-digit number.

![Game Interface](game_interface.png)

Enter a three-digit number with different digits in the input field and press the "Check" button. The game will validate your input and provide feedback on your guess.

- If both the number and the digit position are correct, it will be counted as a "hit".
- If only the number is correct but the digit position is wrong, it will be counted as a "blow".

The game will display the number of hits and blows for each guess. If you guess the correct number, the game will display a congratulatory message. If you run out of tries without guessing the correct number, the game will display the correct number and end the game.

You have a total of seven tries to guess the correct number. The number of remaining lives will be displayed on the screen.

## Game Rules

- The number to be guessed is a three-digit number with different digits.
- You can only enter a three-digit number with different digits. If you enter an invalid input, such as a number with repeated digits or a number with a different number of digits, the game will display an error message and ask you to enter a valid input.
- If you guess the correct number halfway through the game, the game will end as if you answered correctly.
- If you run out of tries without guessing the correct number, the game will display the correct number and end the game.

## Conclusion

Enjoy playing the Hit and Blow Game! Test your guessing skills and see if you can guess the correct number within the given number of tries. Have fun and challenge yourself to improve your score with each game!