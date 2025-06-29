# Hit and Blow Game User Manual

## Introduction

Welcome to the Hit and Blow Game! This game is a fun and challenging number guessing game where you have to predict a randomly generated three-digit number. The game will provide you with feedback on your guesses, allowing you to improve your strategy and try to guess the number correctly.

## Installation

To play the Hit and Blow Game, you need to have Python installed on your computer. You can download Python from the official website: [Python.org](https://www.python.org/downloads/)

Once you have Python installed, you can follow these steps to install the game:

1. Open a command prompt or terminal.
2. Navigate to the directory where you have saved the game files.
3. Run the following command to install the required dependencies:

```
pip install tkinter
```

## How to Play

1. Open a command prompt or terminal.
2. Navigate to the directory where you have saved the game files.
3. Run the following command to start the game:

```
python main.py
```

4. A window will open with the game interface.
5. The game will generate a random three-digit number with different digits.
6. Enter a three-digit number in the input field and click the "Submit" button.
7. The game will provide feedback on your guess:
   - If both the number and the digit position are correct, it will be counted as a "hit".
   - If only the number is correct but the digit position is wrong, it will be counted as a "blow".
8. The game will display the number of remaining lives.
9. Keep guessing until you either guess the number correctly or run out of lives.
10. If you guess the number correctly, the game will end and display a congratulatory message.
11. If you run out of lives, the game will end and display the correct number.

## Game Rules

- You have a total of seven lives to guess the number.
- If you guess the number correctly halfway through, the game will end as if you answered correctly.
- If you enter an invalid input, such as a number with duplicate digits or a number that is not three digits long, the game will ask you to enter a valid input without reducing your remaining lives.

## Conclusion

Enjoy playing the Hit and Blow Game! Test your guessing skills and see if you can predict the randomly generated number. Have fun and challenge yourself to improve your score with each play.