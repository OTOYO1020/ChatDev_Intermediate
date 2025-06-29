# Hit and Blow Game User Manual

## Introduction

Welcome to the Hit and Blow Game! This game is a fun and challenging number guessing game where you have to predict a three-digit number with different digits. The game will provide feedback on your guesses, indicating if you have a hit (correct number and correct position) or a blow (correct number but incorrect position). The objective is to guess the number within seven tries.

## Installation

To play the Hit and Blow Game, you need to have Python installed on your computer. You can download Python from the official website: [Python.org](https://www.python.org/downloads/)

Once you have Python installed, you can follow these steps to set up the game:

1. Download the game files from the repository: [Hit and Blow Game](https://github.com/chatdev-org/hit-and-blow-game)

2. Extract the downloaded files to a folder on your computer.

3. Open a terminal or command prompt and navigate to the folder where you extracted the game files.

4. Install the required dependencies by running the following command:

   ```
   pip install -r requirements.txt
   ```

   This will install the necessary packages, including tkinter.

## How to Play

1. Open a terminal or command prompt and navigate to the folder where you extracted the game files.

2. Run the following command to start the game:

   ```
   python main.py
   ```

3. A window will appear with a text field and a "Guess" button.

4. Enter a three-digit number in the text field and click the "Guess" button to make a guess.

5. The game will provide feedback on your guess. If you have a hit (correct number and correct position), it will be indicated as a hit. If you have a blow (correct number but incorrect position), it will be indicated as a blow.

6. Continue making guesses until you guess the number correctly or run out of lives.

7. If you guess the number correctly, the game will display a congratulatory message and end.

8. If you run out of lives without guessing the number correctly, the game will display the correct number and end.

9. If you guess the number correctly halfway through (two hits) and have three lives remaining, the game will display a congratulatory message and end.

10. You can close the game window at any time to exit the game.

## Game Rules

- The number to be guessed is a three-digit number with different digits.

- Each guess must be a three-digit number.

- If a guess contains the same digit multiple times or is not a three-digit number, it will be considered an invalid input and you will be asked to enter a valid guess again. Lives will not be deducted for invalid inputs.

- You have seven lives to guess the number.

- The game will provide feedback on each guess, indicating hits (correct number and correct position) and blows (correct number but incorrect position).

- If you guess the number correctly, you win the game.

- If you run out of lives without guessing the number correctly, you lose the game.

- If you guess the number correctly halfway through (two hits) and have three lives remaining, you win the game.

## Conclusion

Congratulations! You are now ready to play the Hit and Blow Game. Enjoy the challenge of guessing the three-digit number and have fun! If you have any questions or need further assistance, please don't hesitate to reach out to us. Happy gaming!