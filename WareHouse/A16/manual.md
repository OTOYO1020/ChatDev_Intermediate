# Hit and Blow Game User Manual

## Introduction

Welcome to the Hit and Blow Game! This game is a fun and challenging number guessing game where you have to predict a three-digit number. The game will provide you with feedback on your guesses, and you have a limited number of attempts to guess the correct number.

## Installation

To play the Hit and Blow Game, you need to have Python installed on your computer. You can download Python from the official website: [Python.org](https://www.python.org/downloads/).

Once you have Python installed, you can follow these steps to install the game:

1. Open a terminal or command prompt.
2. Navigate to the directory where you have saved the game files.
3. Run the following command to install the required dependencies:

```
pip install -r requirements.txt
```

## How to Play

1. Open a terminal or command prompt.
2. Navigate to the directory where you have saved the game files.
3. Run the following command to start the game:

```
python main.py
```

4. A window will open with the game interface.
5. The game will generate a random three-digit number with different digits.
6. Enter a three-digit number in the input field and click the "Submit" button.
7. The game will provide feedback on your guess:
   - If both the number and the digit position are correct, it's a "hit".
   - If only the number is correct but the digit position is wrong, it's a "blow".
8. The game will display the number of hits and blows.
9. You have a total of seven lives (attempts) to guess the correct number.
10. If you guess the number correctly, the game will end and display a congratulatory message.
11. If you run out of lives without guessing the correct number, the game will end and display the target number.
12. You can play the game again by restarting the program.

## Rules and Tips

- The number you enter must be a three-digit number with different digits. If you enter an invalid input, you will be prompted to enter a valid number.
- The game will not deduct lives for invalid inputs.
- Try to use the feedback from the game to make educated guesses and improve your chances of guessing the correct number.
- If you guess the number correctly halfway through, the game will end as if you answered correctly.

Have fun playing the Hit and Blow Game!