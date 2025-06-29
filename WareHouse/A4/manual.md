# Hit and Blow Game User Manual

## Introduction

Welcome to the Hit and Blow Game User Manual! This manual will guide you on how to install and play the Hit and Blow game developed by ChatDev. The Hit and Blow game is a fun and challenging game where you need to guess a three-digit number with different digits. You will receive feedback on your guesses in the form of hits and blows. A hit means that both the number and the digit position are correct, while a blow means that only the number is correct but the digit position is wrong. The objective is to guess the number within seven attempts.

## Installation

To install and run the Hit and Blow game, please follow these steps:

1. Ensure that you have Python installed on your system. If not, you can download and install Python from the official website: [Python.org](https://www.python.org/downloads/)

2. Download the source code for the Hit and Blow game from the ChatDev repository.

3. Open a terminal or command prompt and navigate to the directory where you downloaded the source code.

4. Create a virtual environment (optional but recommended) by running the following command:

   ```
   python -m venv venv
   ```

5. Activate the virtual environment by running the appropriate command for your operating system:

   - For Windows:

     ```
     venv\Scripts\activate
     ```

   - For macOS/Linux:

     ```
     source venv/bin/activate
     ```

6. Install the required dependencies by running the following command:

   ```
   pip install -r requirements.txt
   ```

7. Once the dependencies are installed, you are ready to play the Hit and Blow game!

## How to Play

To play the Hit and Blow game, follow these steps:

1. Open a terminal or command prompt and navigate to the directory where you downloaded the source code.

2. Activate the virtual environment (if you created one) by running the appropriate command as mentioned in the installation steps.

3. Run the main.py file by executing the following command:

   ```
   python main.py
   ```

4. A graphical user interface (GUI) window will open, displaying a label asking you to enter a three-digit number.

5. Enter your guess in the input field and click the "Submit" button.

6. The game will provide feedback on your guess in the form of hits and blows. The number of remaining lives will also be displayed.

7. Continue guessing until you either guess the correct number or run out of lives.

8. If you guess the correct number, a message will be displayed congratulating you. If you run out of lives, the target number will be revealed.

9. You can play the game again by closing the GUI window and running the main.py file again.

## Game Rules

To ensure a fair and enjoyable gaming experience, please note the following rules:

- The target number is a three-digit number with different digits. For example, 123, 456, 789.

- Each guess should also be a three-digit number with different digits.

- If you enter an incorrect input, such as a number with repeating digits or a number with a length other than three digits, you will be prompted to enter a valid input without reducing the number of lives.

- You have a total of seven lives to guess the correct number.

- If you guess the correct number halfway through the game, the game will end as if you answered correctly.

- The game will provide feedback on your guesses in the form of hits and blows. A hit means that both the number and the digit position are correct, while a blow means that only the number is correct but the digit position is wrong.

- The number of remaining lives will be displayed after each guess.

## Conclusion

Congratulations! You have successfully installed and learned how to play the Hit and Blow game developed by ChatDev. Enjoy the game and have fun guessing the target number within seven attempts. If you have any questions or encounter any issues, please feel free to reach out to our support team for assistance. Happy gaming!