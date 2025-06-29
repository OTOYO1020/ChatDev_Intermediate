# Hit and Blow Game User Manual

## Introduction

Welcome to the Hit and Blow Game! This game is a fun and challenging number guessing game where you have to predict a three-digit number with different digits. You will receive feedback in the form of hits and blows to help you make your guesses. The goal is to guess the number correctly within seven tries.

## Installation

To play the Hit and Blow Game, you need to have Python installed on your computer. You can download Python from the official website: [Python.org](https://www.python.org/downloads/)

Once you have Python installed, you can follow these steps to install the game:

1. Download the game files from the [ChatDev repository](https://github.com/ChatDevOrg/Hit-and-Blow-Game).

2. Extract the downloaded files to a folder on your computer.

3. Open a terminal or command prompt and navigate to the folder where you extracted the game files.

4. Run the following command to install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

   This will install the necessary packages, including tkinter and random.

## How to Play

1. Open a terminal or command prompt and navigate to the folder where you extracted the game files.

2. Run the following command to start the game:

   ```
   python main.py
   ```

3. A new window will open with the game interface.

4. The game will generate a random three-digit number with different digits. Your task is to guess this number.

5. Enter a three-digit number in the input field and click the "Click Me" button to make a guess.

6. The game will provide feedback in the form of hits and blows:

   - If both the number and the digit position are correct, it is a hit.
   - If only the number is correct but the digit position is wrong, it is a blow.

7. The game will display the number of hits, blows, and the remaining lives after each guess.

8. Keep making guesses until you guess the number correctly or run out of lives.

9. If you guess the number correctly, a message will be displayed congratulating you on your win.

10. If you run out of lives without guessing the number correctly, a message will be displayed indicating that the game is over and revealing the correct number.

11. You can close the game window at any time to exit the game.

## Tips and Rules

- The number you enter must be a three-digit number with different digits. If you enter an invalid number, you will be prompted to enter a valid number.

- Duplicate guesses are not allowed. If you enter a number that you have already guessed, you will be prompted to enter a different number.

- You have a total of seven lives to guess the number. The number of remaining lives will be displayed after each guess.

- If you guess the number correctly before using all seven lives, the game will end and you will be declared the winner.

- If you run out of lives without guessing the number correctly, the game will end and the correct number will be revealed.

- Have fun and enjoy the game!

## Conclusion

Congratulations on completing the installation and learning how to play the Hit and Blow Game! We hope you have a great time playing and challenging yourself to guess the correct number. If you have any questions or encounter any issues, feel free to reach out to our support team for assistance. Happy gaming!