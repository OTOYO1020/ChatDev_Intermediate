Here's a detailed user manual for the Bingo application, formatted in Markdown as requested:

```markdown
# Bingo Application

Welcome to the Bingo Application! This software allows users to play a classic game of Bingo by inputting a 3x3 bingo card and a set of chosen numbers. The application checks for a winning condition and announces whether a Bingo has been achieved.

## Main Functions

- **Input Bingo Card**: Users can input a 3x3 grid of unique numbers to create their Bingo card.
- **Input Chosen Numbers**: Users can input a list of chosen numbers that they have selected.
- **Mark Numbers**: The application marks the numbers on the Bingo card that match the chosen numbers.
- **Check Bingo**: The application checks if there are three marked numbers in a row, column, or diagonal, and announces the result.

## Installation

To run the Bingo application, you need to have Python installed on your system. Follow these steps to set up the environment:

1. **Install Python**: Make sure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: Clone the Bingo application repository to your local machine using the following command:
   ```bash
   git clone <repository-url>
   ```

3. **Navigate to the Directory**: Change to the directory where the Bingo application is located:
   ```bash
   cd bingo-application
   ```

4. **Install Dependencies**: If there are any additional dependencies required, you can install them using pip. For this application, there are no external dependencies, but ensure you have the latest version of Python.

## How to Use/Play

1. **Run the Application**: Start the Bingo application by executing the following command in your terminal:
   ```bash
   python main.py
   ```

2. **Input the Bingo Card**: You will be prompted to enter the 3x3 Bingo card values. Input three rows of three unique integers, separated by spaces. For example:
   ```
   Enter the 3x3 bingo card values (3 rows of 3 unique numbers each, space-separated):
   1 2 3
   4 5 6
   7 8 9
   ```

3. **Input Chosen Numbers**: After entering the Bingo card, you will be prompted to enter the chosen numbers. Input at least one unique integer, separated by spaces. For example:
   ```
   Enter chosen numbers (space-separated):
   1 5 9
   ```

4. **View Results**: The application will process the input and check for Bingo. It will print either "BINGO" if a winning condition is met or "NO BINGO" if not.

## Example Gameplay

```
Enter the 3x3 bingo card values (3 rows of 3 unique numbers each, space-separated):
1 2 3
4 5 6
7 8 9
Enter chosen numbers (space-separated):
1 2 3
BINGO
```

## Troubleshooting

- **Invalid Input**: If you enter an invalid Bingo card or chosen numbers, the application will prompt you to re-enter the values until valid input is provided.
- **Unique Numbers**: Ensure that all numbers in the Bingo card and chosen numbers are unique to avoid errors.

## Conclusion

Enjoy playing Bingo with our application! If you have any questions or feedback, feel free to reach out for support.
```

This manual provides a comprehensive guide for users to install and play the Bingo application, ensuring they have all the necessary information to get started.