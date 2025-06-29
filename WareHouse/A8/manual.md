# Hit and Blow Game User Manual

## Introduction

Welcome to the Hit and Blow Game User Manual! This manual will guide you through the installation process and explain how to use and play the Hit and Blow game developed by ChatDev.

The Hit and Blow game is a number guessing game where the player tries to predict a randomly generated three-digit number. The game provides feedback in the form of "hits" and "blows" to help the player make correct guesses. The player has a limited number of lives to complete the game.

## Installation

To install and run the Hit and Blow game, please follow these steps:

1. Ensure that you have Python installed on your computer. If not, you can download and install Python from the official website: [Python.org](https://www.python.org/).

2. Download the source code for the Hit and Blow game from the provided link.

3. Open a terminal or command prompt and navigate to the directory where you downloaded the source code.

4. Create a virtual environment (optional but recommended) by running the following command:

   ```
   python -m venv env
   ```

5. Activate the virtual environment by running the appropriate command for your operating system:

   - For Windows:

     ```
     env\Scripts\activate
     ```

   - For macOS and Linux:

     ```
     source env/bin/activate
     ```

6. Install the required dependencies by running the following command:

   ```
   pip install -r requirements.txt
   ```

7. Once the dependencies are installed, you can start the game by running the following command:

   ```
   python main.py
   ```

   The game window should open, and you can start playing!

## How to Play

1. When the game starts, you will see a window with a label asking you to enter a three-digit number.

2. Enter your guess in the entry field provided.

   - The guess should be a three-digit number with different digits.
   - If you enter an incorrect input (e.g., a number with repeating digits or a number with a different length), you will be prompted to enter a valid guess.

3. Click the "Guess" button to submit your guess.

4. The game will provide feedback in the form of "hits" and "blows" to help you make correct guesses.

   - A "hit" means that both the number and the digit position are correct.
   - A "blow" means that the number is correct, but the digit position is different.

5. The number of remaining lives will be displayed on the screen.

6. Keep guessing until you either guess the correct number or run out of lives.

   - If you guess the correct number, you will see a congratulatory message.
   - If you run out of lives, the game will end, and the correct number will be revealed.

7. You can play the game multiple times by restarting the application.

## Conclusion

Congratulations! You have successfully installed and learned how to play the Hit and Blow game developed by ChatDev. Enjoy playing the game and have fun guessing the numbers!