# Hit and Blow Game User Manual

## Introduction

Welcome to the Hit and Blow Game User Manual. This manual will guide you on how to install and use the Hit and Blow Game application developed by ChatDev. The Hit and Blow Game is a fun and challenging game where you need to guess a randomly generated three-digit number with different digits.

## Installation

To install the Hit and Blow Game application, please follow the steps below:

1. Make sure you have Python installed on your computer. You can download Python from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. Download the source code of the Hit and Blow Game from the repository: [https://github.com/ChatDev/hit-and-blow-game](https://github.com/ChatDev/hit-and-blow-game)

3. Extract the downloaded source code to a directory of your choice.

4. Open a terminal or command prompt and navigate to the directory where you extracted the source code.

5. Install the required dependencies by running the following command:

   ```
   pip install -r requirements.txt
   ```

   This will install the necessary dependencies, including the tkinter library.

## Usage

To play the Hit and Blow Game, please follow the steps below:

1. Open a terminal or command prompt and navigate to the directory where you extracted the source code.

2. Run the following command to start the game:

   ```
   python main.py
   ```

3. A graphical user interface window will appear with the title "Hit and Blow Game".

4. Enter a three-digit number with different digits in the input field.

5. Click the "Submit" button to submit your guess.

6. The game will display the number of hits, blows, and remaining lives.

   - If both the number and the digit position are the same, it is a hit.
   - If only the number is the same but the digit position is different, it is a blow.

7. Continue guessing until you correctly guess the number or run out of lives.

   - If you answer correctly halfway through, the game will end as if you answered correctly.

8. If you enter an incorrect input, such as a number with the same digit or a number that is not three digits, the game will ask you to enter it again without reducing the number of lives.

9. The game will display a message when you win or lose.

10. You can play the game again by closing the window and running the `python main.py` command again.

## Conclusion

Congratulations! You have successfully installed and played the Hit and Blow Game. Enjoy the game and have fun guessing the randomly generated three-digit number. If you have any questions or need further assistance, please don't hesitate to contact us.