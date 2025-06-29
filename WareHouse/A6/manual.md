# Hit and Blow Game User Manual

## Introduction

The Hit and Blow game is a number guessing game where the player tries to guess a randomly generated three-digit number. The objective is to guess both the number and the digit position correctly. If the player guesses the number and the digit position correctly, it is considered a "hit". If the player guesses only the number correctly but the digit position is wrong, it is considered a "blow". The game provides feedback on the number of hits and blows after each guess.

## Installation

To play the Hit and Blow game, you need to have Python installed on your computer. You can download Python from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

Once you have Python installed, you can proceed with the following steps:

1. Open a terminal or command prompt.
2. Install the required dependencies by running the following command:

   ```
   pip install tkinter
   ```

3. Download the game code from the following GitHub repository: [https://github.com/ChatDev/Hit-and-Blow-Game](https://github.com/ChatDev/Hit-and-Blow-Game)
4. Extract the downloaded ZIP file to a location of your choice.

## Usage

To start the Hit and Blow game, follow these steps:

1. Open a terminal or command prompt.
2. Navigate to the directory where you extracted the game code.
3. Run the following command to start the game:

   ```
   python main.py
   ```

4. A new window will open with the game interface.

## Game Rules

1. The game randomly generates a three-digit number with different digits.
2. The player needs to input a three-digit number and click the "Submit" button.
3. If both the number and the digit position are correct, it is a "hit".
4. If only the number is correct but the digit position is wrong, it is a "blow".
5. The game provides feedback on the number of hits and blows after each guess.
6. The player has a total of seven lives (guesses) to find the correct number.
7. The remaining lives are displayed on the screen.
8. If the player guesses the correct number halfway through (after three guesses), the game ends.
9. If the player runs out of lives or guesses the correct number, the game ends.
10. If the player enters an invalid input (not a three-digit number or contains duplicate digits), they will be asked to enter again without reducing the number of lives.

## Game Interface

The game interface consists of the following elements:

- Label: Displays the remaining lives and game status.
- Input Entry: Allows the player to enter a three-digit number.
- Submit Button: Submits the player's guess.

## Example Gameplay

1. The game starts with seven remaining lives.
2. The player enters a three-digit number and clicks the "Submit" button.
3. The game displays the number of hits and blows, as well as the remaining lives.
4. The player continues to guess until they find the correct number or run out of lives.
5. If the player guesses the correct number halfway through, the game ends with a congratulatory message.
6. If the player runs out of lives, the game ends with a game over message.

## Conclusion

The Hit and Blow game is an entertaining number guessing game that challenges your logical thinking and deduction skills. Enjoy playing the game and have fun trying to find the secret number!