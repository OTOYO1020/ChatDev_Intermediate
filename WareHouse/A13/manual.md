# Hit and Blow Game User Manual

## Introduction

Welcome to the Hit and Blow Game! This game is a fun and challenging number guessing game where you have to predict a three-digit number with different digits. You will receive feedback in the form of hits and blows to help you guess the correct number. The game provides a user-friendly interface and allows you to play multiple rounds.

## Installation

To play the Hit and Blow Game, you need to have Python installed on your computer. You can download Python from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

Once you have Python installed, you can follow these steps to set up the game:

1. Download the game code from the following GitHub repository: [https://github.com/ChatDevTeam/hit-and-blow-game](https://github.com/ChatDevTeam/hit-and-blow-game)

2. Extract the downloaded ZIP file to a location of your choice.

3. Open a terminal or command prompt and navigate to the extracted folder.

4. Install the required dependencies by running the following command:
   ```
   pip install -r requirements.txt
   ```

## How to Play

1. Open a terminal or command prompt and navigate to the folder where you extracted the game code.

2. Run the game by executing the following command:
   ```
   python main.py
   ```

3. A graphical user interface (GUI) window will appear with a label asking you to enter a three-digit number.

4. Enter a three-digit number using the keyboard and click the "Submit" button.

5. The game will provide feedback in the form of hits and blows. A hit means that both the number and the digit position are correct, while a blow means that only the number is correct but the digit position is wrong.

6. The game will display the number of hits, blows, and the remaining lives (chances) you have.

7. Keep guessing the number by entering new three-digit numbers until you either guess the correct number or run out of lives.

8. If you guess the correct number, the game will display a congratulatory message and end.

9. If you run out of lives without guessing the correct number, the game will display the correct number and end.

## Game Rules

- You can only enter three-digit numbers with different digits. If you enter an invalid input, such as a number with repeated digits or a number with a different length, the game will prompt you to enter a valid input.

- You have a total of seven lives (chances) to guess the correct number. The remaining lives will be displayed after each guess.

- If you guess the correct number halfway through the game, the game will end as if you answered correctly.

- The game will not reduce the number of lives if you enter an invalid input.

## Conclusion

Congratulations! You are now ready to play the Hit and Blow Game. Have fun guessing the numbers and challenging yourself to improve your score. If you have any questions or encounter any issues, please feel free to reach out to our support team for assistance. Enjoy the game!