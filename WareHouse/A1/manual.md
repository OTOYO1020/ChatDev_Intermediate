# Hit and Blow Game User Manual

## Introduction
Welcome to the Hit and Blow Game User Manual! This manual will guide you through the installation process and explain how to use and play the Hit and Blow Game developed by ChatDev.

## Table of Contents
1. Installation
2. Game Rules
3. How to Play
4. Troubleshooting
5. Contact Information

## 1. Installation
To install and run the Hit and Blow Game, please follow the steps below:

### Prerequisites
- Python 3.6 or higher installed on your machine

### Steps
1. Clone the repository from GitHub: [https://github.com/ChatDev/hit-blow-game](https://github.com/ChatDev/hit-blow-game)
2. Navigate to the project directory in your terminal.
3. Install the required dependencies by running the following command:
   ```
   pip install -r requirements.txt
   ```
4. Once the installation is complete, you are ready to play the game!

## 2. Game Rules
The Hit and Blow Game is a number guessing game. The objective is to guess a randomly generated three-digit number with different digits. Here are the rules of the game:

- The game generates a secret three-digit number with different digits.
- You have a total of seven lives to guess the number correctly.
- If both the number and the digit position are the same, it is a hit.
- If only the number is the same but the digit position is different, it is a blow.
- If you answer correctly halfway through, the game ends as if you answered correctly.
- If you enter an incorrect input (e.g., a number with duplicate digits or a number that is not three digits), the game will ask you to enter it again without reducing the number of lives.

## 3. How to Play
To play the Hit and Blow Game, follow these steps:

1. Open a terminal and navigate to the project directory.
2. Run the following command to start the game:
   ```
   python main.py
   ```
3. A window will appear with a label asking you to enter a three-digit number.
4. Enter your guess in the entry field and click the "Submit" button.
5. The game will display the result of your guess (e.g., hits, blows, remaining lives).
6. Keep guessing until you either guess the number correctly or run out of lives.
7. If you guess the number correctly, the game will display a congratulatory message and end.
8. If you run out of lives, the game will reveal the secret number and end.

## 4. Troubleshooting
If you encounter any issues while installing or playing the Hit and Blow Game, please try the following troubleshooting steps:

- Make sure you have Python 3.6 or higher installed on your machine.
- Double-check that you have installed all the required dependencies by running the command `pip install -r requirements.txt`.
- Ensure that you are running the game from the correct directory by navigating to the project directory in your terminal.
- If the game window does not appear or freezes, try restarting the game by closing the window and running the command `python main.py` again.

If the issue persists, please contact our support team (see contact information below) for further assistance.

## 5. Contact Information
If you have any questions, feedback, or need assistance with the Hit and Blow Game, please contact our support team:

- Email: support@chatdev.com
- Phone: +1 123-456-7890
- Website: [https://www.chatdev.com](https://www.chatdev.com)

We are here to help and ensure you have an enjoyable gaming experience!

Happy playing!
The ChatDev Team