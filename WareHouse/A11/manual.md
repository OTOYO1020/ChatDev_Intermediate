# Hit and Blow Game User Manual

Welcome to the Hit and Blow Game User Manual! This manual will guide you on how to install and use the Hit and Blow game developed by ChatDev.

## Table of Contents
1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Game Rules](#game-rules)
4. [How to Play](#how-to-play)
5. [Troubleshooting](#troubleshooting)

## 1. Introduction <a name="introduction"></a>
The Hit and Blow game is a number guessing game where the player tries to predict a randomly generated three-digit number. The game provides feedback in the form of hits and blows to help the player make accurate guesses. The objective is to guess the number correctly within a limited number of attempts.

## 2. Installation <a name="installation"></a>
To install and run the Hit and Blow game, please follow these steps:

1. Ensure you have Python installed on your computer. If not, you can download it from the official Python website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. Clone the ChatDev repository from GitHub using the following command:
   ```
   git clone https://github.com/ChatDev/Hit-And-Blow-Game.git
   ```

3. Navigate to the cloned repository:
   ```
   cd Hit-And-Blow-Game
   ```

4. Install the required dependencies by running the following command:
   ```
   pip install -r requirements.txt
   ```

5. Run the game by executing the `main.py` file:
   ```
   python main.py
   ```

## 3. Game Rules <a name="game-rules"></a>
The Hit and Blow game follows these rules:

- The game generates a random three-digit number with different digits.
- The player has a limited number of attempts (lives) to guess the number.
- If the player's guess has both the correct number and digit position, it is a hit.
- If the player's guess has the correct number but the digit position is different, it is a blow.
- The game provides feedback on the number of hits and blows after each guess.
- If the player guesses the number correctly within the given number of attempts, the game ends.
- If the player guesses the number correctly halfway through the attempts, the game ends.
- If the player runs out of attempts without guessing the number correctly, the game ends.

## 4. How to Play <a name="how-to-play"></a>
Follow these steps to play the Hit and Blow game:

1. Launch the game by running the `main.py` file.

2. The game window will appear with a "Click Me" button.

3. Click the "Click Me" button to start the game.

4. The game will display the number of remaining lives.

5. Enter a three-digit number in the input field and click the "Submit" button.

6. The game will provide feedback on the number of hits and blows.

7. Continue guessing until you either guess the number correctly or run out of lives.

8. If you guess the number correctly, the game will display a congratulatory message.

9. If you run out of lives without guessing the number correctly, the game will display the target number and end.

10. You can play the game again by relaunching the `main.py` file.

## 5. Troubleshooting <a name="troubleshooting"></a>
If you encounter any issues while installing or playing the Hit and Blow game, please try the following troubleshooting steps:

- Ensure you have Python installed and the correct version (Python 3.6 or higher).
- Double-check that you have installed the required dependencies by running `pip install -r requirements.txt`.
- Make sure you are running the game from the correct directory (`Hit-And-Blow-Game`).
- If the game window does not appear, check if there are any error messages in the terminal.
- If the game crashes or freezes, try restarting the game by relaunching the `main.py` file.

If the issue persists, please reach out to our support team for further assistance.

Enjoy playing the Hit and Blow game!