# Hit and Blow Game User Manual

Welcome to the Hit and Blow Game! This user manual will guide you through the installation process, explain the main functions of the game, and provide instructions on how to play.

## Table of Contents
1. [Installation](#installation)
2. [Main Functions](#main-functions)
3. [How to Play](#how-to-play)

## 1. Installation <a name="installation"></a>

To install and run the Hit and Blow Game, please follow these steps:

1. Ensure that you have Python installed on your computer. If not, you can download and install Python from the official website: [Python.org](https://www.python.org/downloads/).

2. Download the source code for the game from the [ChatDev GitHub repository](https://github.com/ChatDev/hit-and-blow-game).

3. Extract the downloaded ZIP file to a location of your choice.

4. Open a terminal or command prompt and navigate to the extracted folder.

5. Install the required dependencies by running the following command:

   ```
   pip install -r requirements.txt
   ```

6. Once the dependencies are installed, you can start the game by running the following command:

   ```
   python main.py
   ```

Congratulations! You have successfully installed and launched the Hit and Blow Game.

## 2. Main Functions <a name="main-functions"></a>

The Hit and Blow Game has the following main functions:

- Randomly generates a three-digit number with different digits.
- Allows the user to input a three-digit number.
- Determines if the user's guess is correct.
- Provides feedback on the user's guess, indicating hits and blows.
- Displays the number of remaining lives.
- Ends the game if the user answers correctly or runs out of lives.

## 3. How to Play <a name="how-to-play"></a>

To play the Hit and Blow Game, follow these instructions:

1. After launching the game, a window will appear with a label asking you to enter a three-digit number.

2. Enter a three-digit number using the keyboard.

   - The number should have different digits (e.g., 123, 456, 789).
   - If you enter the same digit multiple times or a number with more or fewer than three digits, it will be considered an incorrect input.

3. Click the "Submit" button or press Enter to submit your guess.

4. The game will provide feedback on your guess:

   - If both the number and the digit position are correct, it will be counted as a hit.
   - If only the number is correct but the digit position is wrong, it will be counted as a blow.

5. The game will display the number of hits, blows, and remaining lives.

6. Continue guessing until you either guess the correct number or run out of lives.

   - If you guess the correct number, the game will display a congratulatory message and end.
   - If you run out of lives, the game will display the correct number and end.

7. You can play the game again by relaunching the application.

Enjoy playing the Hit and Blow Game!