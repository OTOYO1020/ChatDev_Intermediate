# Hit and Blow Game User Manual

## Introduction

Welcome to the Hit and Blow Game User Manual! This manual will guide you through the installation process and explain how to use and play the Hit and Blow game developed by ChatDev.

The Hit and Blow game is a number guessing game where the player tries to predict a randomly generated three-digit number. The game provides feedback in the form of hits and blows to help the player make accurate guesses. The goal is to guess the number within a limited number of attempts.

## Installation

To install and run the Hit and Blow game, please follow these steps:

1. Ensure that you have Python installed on your computer. If not, you can download and install Python from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. Download the game files from the ChatDev repository: [https://github.com/ChatDev/Hit-and-Blow-Game](https://github.com/ChatDev/Hit-and-Blow-Game)

3. Extract the downloaded files to a directory of your choice.

4. Open a terminal or command prompt and navigate to the directory where you extracted the game files.

5. Install the required dependencies by running the following command:

   ```
   pip install tkinter
   ```

   This will install the Tkinter library, which is used for the graphical user interface of the game.

## How to Play

Once you have installed the game, you can start playing by following these steps:

1. Open a terminal or command prompt and navigate to the directory where you extracted the game files.

2. Run the following command to start the game:

   ```
   python main.py
   ```

   This will launch the game in the terminal.

3. The game will generate a random three-digit number with different digits as the target number.

4. You will be prompted to enter your guess. Enter a three-digit number and press Enter.

5. The game will provide feedback in the form of hits and blows:

   - If both the number and the digit position are correct, it is a hit.
   - If only the number is correct but the digit position is wrong, it is a blow.

6. Continue guessing until you either guess the correct number or run out of lives.

7. The game will end when one of the following conditions is met:

   - You guess the correct number and digit position (3 hits).
   - You run out of lives (7 incorrect guesses).

8. If you guess the correct number halfway through the game, the game will end as if you answered correctly.

## Game Rules

To ensure a fair and enjoyable gaming experience, please note the following rules:

- You have a total of 7 lives (guesses) to guess the correct number.
- If you enter an invalid input, such as a number with duplicate digits or a number that is not three digits long, the game will prompt you to enter a valid input without reducing your remaining lives.
- The game will display the number of remaining lives after each guess.
- If you guess the correct number halfway through the game, the game will end as if you answered correctly.
- The game will provide feedback in the form of hits and blows to help you make accurate guesses.

## Conclusion

Congratulations! You are now ready to install and play the Hit and Blow game developed by ChatDev. Enjoy the game and have fun guessing the correct number! If you have any questions or encounter any issues, please feel free to reach out to our support team for assistance.

Happy gaming!