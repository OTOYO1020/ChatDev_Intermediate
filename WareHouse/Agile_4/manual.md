# Hit and Blow Game User Manual

## Introduction

The Hit and Blow Game is a number guessing game where the player tries to predict a randomly generated three-digit number. The game provides feedback in the form of hits and blows to help the player make correct guesses. The objective is to guess the number within a limited number of attempts.

This user manual provides instructions on how to install the game and play it on your computer.

## Installation

To install and run the Hit and Blow Game, follow these steps:

1. Ensure that you have Python installed on your computer. If not, download and install Python from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. Download the game files from the repository: [https://github.com/ChatDevOrg/hit-and-blow-game](https://github.com/ChatDevOrg/hit-and-blow-game)

3. Extract the downloaded files to a directory of your choice.

4. Open a terminal or command prompt and navigate to the directory where the game files are located.

5. Install the required dependencies by running the following command:

   ```
   pip install -r requirements.txt
   ```

   This will install the necessary packages, including tkinter and random2.

## How to Play

Once you have installed the game, follow these steps to play:

1. Open a terminal or command prompt and navigate to the directory where the game files are located.

2. Run the following command to start the game:

   ```
   python main.py
   ```

3. A window will open with the game interface. The window will display a label asking you to enter a three-digit number.

4. Enter a three-digit number using the keyboard and press the "Submit" button.

5. The game will provide feedback in the form of hits and blows. A hit means that both the number and the digit position are correct, while a blow means that only the number is correct but the digit position is different.

6. The game will display the number of remaining lives, which represents the number of attempts you have left.

7. Continue guessing the number by entering new three-digit numbers until you either guess the number correctly or run out of lives.

8. If you guess the number correctly, the game will display a congratulatory message.

9. If you run out of lives without guessing the number correctly, the game will display the secret number and end the game.

10. You can close the game window at any time to exit the game.

## Game Rules

To ensure a fair and enjoyable gaming experience, the Hit and Blow Game follows these rules:

- The secret number is a randomly generated three-digit number with different digits.

- The player can only enter three-digit numbers. Any other input will be considered invalid.

- If the player enters a number with duplicate digits or a number that is not three digits long, it will be considered an incorrect input and the player will be asked to enter a valid number again. The number of lives will not be reduced in this case.

- The player has a total of seven lives, representing the number of attempts they can make to guess the number.

- If the player guesses the number correctly halfway through the game (i.e., two hits and no blows), the game will end and display a congratulatory message.

- The game will display the number of remaining lives after each guess.

## Conclusion

Congratulations! You are now ready to install and play the Hit and Blow Game. Enjoy the challenge of guessing the secret number and have fun! If you have any questions or encounter any issues, please feel free to reach out to our support team for assistance.