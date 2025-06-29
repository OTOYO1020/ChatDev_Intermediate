# Hit and Blow Game User Manual

## Introduction

Welcome to the Hit and Blow Game! This game is a fun and challenging number guessing game where you have to predict a three-digit number with different digits. You will have a limited number of tries to guess the correct number, and the game will provide feedback on your guesses.

## Installation

To play the Hit and Blow Game, you need to have Python installed on your computer. You can download Python from the official website: [Python.org](https://www.python.org/downloads/)

Once you have Python installed, you can follow these steps to install the game:

1. Download the game files from the repository: [Hit and Blow Game](https://github.com/ChatDevOrg/hit-and-blow-game)

2. Extract the downloaded files to a folder on your computer.

3. Open a terminal or command prompt and navigate to the folder where you extracted the game files.

4. Install the required dependencies by running the following command:

   ```
   pip install -r requirements.txt
   ```

   This will install the necessary packages, including tkinter.

## How to Play

To start the Hit and Blow Game, follow these steps:

1. Open a terminal or command prompt and navigate to the folder where you extracted the game files.

2. Run the following command to start the game:

   ```
   python main.py
   ```

3. A game window will open with a label showing the number of remaining lives and an input field for you to enter your guesses.

4. Enter a three-digit number with different digits in the input field and click the "Submit" button.

5. The game will provide feedback on your guess. If both the number and the digit position are correct, it will be counted as a hit. If only the number is correct but the digit position is wrong, it will be counted as a blow.

6. Continue guessing until you either guess the correct number or run out of lives.

7. If you guess the correct number, a message will be displayed congratulating you on winning the game.

8. If you run out of lives without guessing the correct number, a message will be displayed showing the correct number.

9. You can play the game again by closing the game window and running the `python main.py` command again.

## Game Rules

Here are the rules of the Hit and Blow Game:

- You need to guess a three-digit number with different digits.

- If both the number and the digit position are correct, it is counted as a hit.

- If only the number is correct but the digit position is wrong, it is counted as a blow.

- You have a total of seven lives to guess the correct number.

- If you guess the correct number halfway through, the game will end as if you answered correctly.

- If you enter an incorrect input, such as a number with the same digit or a number that is not three digits, the game will ask you to enter it again without reducing the number of lives.

## Conclusion

Congratulations! You are now ready to play the Hit and Blow Game. Have fun guessing the numbers and enjoy the challenge! If you have any questions or need further assistance, please don't hesitate to reach out to our support team.