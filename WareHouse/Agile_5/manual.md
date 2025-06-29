# Hit and Blow Game User Manual

## Introduction

The Hit and Blow Game is a fun and challenging game where the player tries to guess a randomly generated three-digit number. The game provides feedback in the form of hits and blows to help the player make correct guesses. The objective is to guess the number within a limited number of attempts.

This user manual provides instructions on how to install the game and play it.

## Installation

To install and run the Hit and Blow Game, follow these steps:

1. Ensure that you have Python installed on your system. If not, you can download and install Python from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. Download the game code from the provided source.

3. Open a terminal or command prompt and navigate to the directory where you downloaded the game code.

4. Install the required dependencies by running the following command:

   ```
   pip install -r requirements.txt
   ```

   This will install the necessary dependencies, including the `tkinter` library.

5. Once the dependencies are installed, you can start the game by running the following command:

   ```
   python main.py
   ```

   This will launch the game window.

## Game Rules

The Hit and Blow Game follows the following rules:

1. The game randomly generates a three-digit number with different digits.

2. The player needs to input a three-digit number as a guess.

3. If both the number and the digit position are the same, it is a hit.

4. If only the number is the same but the digit position is different, it is a blow.

5. The game provides feedback on the number of hits and blows for each guess.

6. The player has a limited number of attempts (lives) to guess the number. The default number of lives is set to seven.

7. The game displays the number of remaining lives after each guess.

8. If the player guesses the number correctly, the game ends and displays a congratulatory message.

9. If the player runs out of lives without guessing the number correctly, the game ends and displays the target number.

10. If the player enters an invalid input, such as a number with duplicate digits or a number that is not three digits long, the game displays an error message and asks for a valid input. The number of lives is not reduced in this case.

## Game Interface

The game interface consists of a window with the following elements:

1. Welcome message: Displays a welcome message at the top of the window.

2. Remaining Lives: Displays the number of remaining lives after each guess.

3. Input Entry: Allows the player to enter their guess as a three-digit number.

4. Submit Button: Submits the guess and triggers the evaluation of hits and blows.

## Playing the Game

To play the Hit and Blow Game, follow these steps:

1. Launch the game by running the `main.py` file.

2. The game window will open, displaying the welcome message and the number of remaining lives.

3. Enter your guess in the input entry field. The guess should be a three-digit number with different digits.

4. Click the submit button to submit your guess.

5. The game will evaluate your guess and display the number of hits and blows.

6. If you guess the number correctly, the game will display a congratulatory message and end.

7. If you run out of lives without guessing the number correctly, the game will display the target number and end.

8. If you enter an invalid input, such as a number with duplicate digits or a number that is not three digits long, the game will display an error message and ask for a valid input. The number of lives will not be reduced in this case.

9. Repeat steps 3 to 8 until you guess the number correctly or run out of lives.

## Conclusion

Congratulations! You are now ready to install and play the Hit and Blow Game. Enjoy the challenge of guessing the randomly generated number and have fun!