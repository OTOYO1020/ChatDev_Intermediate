Here's a detailed user manual for the Dice Roll application, formatted in Markdown:

```markdown
# Dice Roll Application

A simple application to check for consecutive doublets in dice rolls.

## Introduction

The Dice Roll application allows users to input a specified number of dice rolls and checks for consecutive doublets. A doublet occurs when both dice in a roll show the same number. The application will inform the user if there are at least one set of three consecutive doublets.

## Main Functions

- **Input Validation**: Ensures that the number of rolls (N) is between 3 and 100.
- **Dice Roll Input**: Collects pairs of integers representing the results of each dice roll.
- **Doublet Checking**: Analyzes the rolls to determine if there are three consecutive doublets.
- **Result Output**: Displays "YES" if at least one set of three consecutive doublets is found, otherwise displays "NO".

## Installation

To run the Dice Roll application, you need to have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

### Environment Setup

1. **Clone the Repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**:
   The Dice Roll application does not require any external dependencies beyond Python itself. Ensure you have Python 3.x installed.

## How to Use the Application

1. **Run the Application**:
   Open your terminal or command prompt and navigate to the directory where the `main.py` file is located. Run the following command:
   ```bash
   python main.py
   ```

2. **Input the Number of Rolls**:
   When prompted, enter an integer value for N (the number of rolls) between 3 and 100. If the input is invalid, the application will prompt you to enter a valid number.

   ```
   Enter number of rolls (3-100): 
   ```

3. **Input Dice Rolls**:
   For each roll, you will be prompted to enter two integers separated by a space. These integers represent the results of the two dice. Ensure you enter exactly two integers.

   ```
   Enter roll 1 (two integers separated by space): 
   ```

4. **View the Result**:
   After entering all the rolls, the application will analyze the input and display the result:
   ```
   YES  (if there are at least three consecutive doublets)
   NO   (if there are no consecutive doublets)
   ```

## Example Usage

```
Enter number of rolls (3-100): 5
Enter roll 1 (two integers separated by space): 3 3
Enter roll 2 (two integers separated by space): 4 4
Enter roll 3 (two integers separated by space): 5 5
Enter roll 4 (two integers separated by space): 6 6
Enter roll 5 (two integers separated by space): 6 6
YES
```

## Conclusion

The Dice Roll application is a straightforward tool for checking consecutive doublets in dice rolls. It is designed to be user-friendly and provides clear prompts for input. Enjoy rolling the dice and checking for doublets!
```

This manual provides a comprehensive guide for users to understand the functionality of the Dice Roll application, how to install it, and how to use it effectively.