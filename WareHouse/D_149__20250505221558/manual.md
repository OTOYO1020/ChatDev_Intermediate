Here's a detailed user manual for the Rock-Paper-Scissors game application, formatted in Markdown as requested:

```markdown
# Rock-Paper-Scissors Game Application

Welcome to the Rock-Paper-Scissors Game Application! This software allows you to play a strategic version of the classic game against a machine, optimizing your moves based on previous rounds.

## Main Functions

- **Input Parameters**: The application takes five integers (N, K, R, S, P) and a string (T) representing the machine's moves.
  - **N**: Total number of rounds.
  - **K**: The number of previous moves to consider for restrictions.
  - **R**: Score awarded for winning with Rock.
  - **S**: Score awarded for winning with Scissors.
  - **P**: Score awarded for winning with Paper.
  - **T**: A string of length N consisting of the machine's moves ('R', 'P', 'S').

- **Score Calculation**: The application calculates the maximum score based on the player's optimal moves against the machine's moves while adhering to the restriction of not repeating the same move as in the (i-K)-th round.

- **User Interface**: The application provides a simple graphical user interface (GUI) for user interaction.

## Installation

To run the Rock-Paper-Scissors Game Application, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. **Install Python**: Make sure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **Install Dependencies**: Open your terminal or command prompt and run the following command to install the required dependencies:
   ```bash
   pip install tkinter
   ```

3. **Clone the Repository**: Download or clone the repository containing the application files.

4. **Navigate to the Application Directory**: Use the terminal to navigate to the directory where the application files are located.

## How to Use/Play

1. **Run the Application**: Execute the main application file using Python:
   ```bash
   python main.py
   ```
   or, if you want to use the GUI:
   ```bash
   python game_app.py
   ```

2. **Input Your Parameters**: 
   - If using the console application, you will be prompted to enter the values for N, K, R, S, P, followed by the string T. For example:
     ```
     Enter N, K, R, S, P: 5 2 3 2 1
     Enter the machine's moves (string of length N): RPSRP
     ```

   - If using the GUI, enter the parameters in the provided input field in the format: `N K R S P T` (space-separated) and click the "Start Game" button.

3. **View the Result**: After processing the input, the application will display the maximum score achieved based on your optimal moves against the machine's moves.

## Example

To play a game with the following parameters:
- N = 5 (5 rounds)
- K = 2 (consider the last 2 moves)
- R = 3 (score for winning with Rock)
- S = 2 (score for winning with Scissors)
- P = 1 (score for winning with Paper)
- T = "RPSRP" (machine's moves)

You would input:
```
Enter N, K, R, S, P: 5 2 3 2 1
Enter the machine's moves (string of length N): RPSRP
```
The application will then calculate and display the maximum score based on your optimal strategy.

## Conclusion

Thank you for using the Rock-Paper-Scissors Game Application! We hope you enjoy playing and optimizing your strategy against the machine. For any issues or feedback, please reach out to our support team.
```

This manual provides a comprehensive overview of the application, including its main functions, installation instructions, and usage guidelines. Let me know if you need any further modifications or additional information!