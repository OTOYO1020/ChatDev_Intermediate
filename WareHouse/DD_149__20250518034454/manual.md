Here is the `manual.md` file for the Max Score Calculator application:

```markdown
# Max Score Calculator

Calculate the maximum score in a game of Rock, Paper, Scissors against a machine.

## Introduction

The Max Score Calculator is a Python application designed to help users determine the optimal hand to play in a series of Rock, Paper, Scissors rounds against a machine. The application calculates the maximum score based on the user's input of rounds, scoring rules, and the machine's hands.

## Main Functions

- **max_score(N: int, K: int, R: int, S: int, P: int, T: str) -> int**: This function calculates the maximum score based on the number of rounds (N), the last K hands played (K), the scores for Rock (R), Scissors (S), and Paper (P), and the machine's hands (T). It returns the total score after all rounds have been played.

## Installation

To run the Max Score Calculator, you need to have Python installed on your machine. You can install the required dependencies using pip. Follow these steps:

1. **Install Python**: Make sure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: Clone the repository containing the Max Score Calculator code.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

3. **Install Dependencies**: Use pip to install any necessary dependencies (if applicable). For this application, there are no external dependencies required beyond Python itself.

   ```bash
   pip install -r requirements.txt
   ```

   *(Note: If there are no additional dependencies, this step can be skipped.)*

## How to Use/Play

1. **Run the Application**: Execute the main application file to start the Max Score Calculator.

   ```bash
   python main.py
   ```

2. **Input Parameters**: The application will prompt you to enter the following parameters:
   - **Number of Rounds (N)**: The total number of rounds to be played.
   - **Last K Hands (K)**: The number of previous hands to consider when determining the optimal hand.
   - **Score for Rock (R)**: The score awarded for winning with Rock.
   - **Score for Scissors (S)**: The score awarded for winning with Scissors.
   - **Score for Paper (P)**: The score awarded for winning with Paper.
   - **Machine's Hands (T)**: A string representing the machine's hands for each round (e.g., "RPSRSP").

3. **View Results**: After entering the parameters, the application will calculate and display the maximum score based on your inputs.

## Example Usage

```
Number of Rounds (N): 5
Last K Hands (K): 2
Score for Rock (R): 1
Score for Scissors (S): 2
Score for Paper (P): 3
Machine's Hands (T): RPSRP
Maximum Score: 8
```

## Conclusion

The Max Score Calculator is a straightforward tool for determining the best strategy in a game of Rock, Paper, Scissors. By following the instructions above, you can easily set up and use the application to maximize your score against the machine.

For any questions or support, please reach out to our development team.
```

This manual provides a comprehensive guide for users to understand the application, install it, and use it effectively. Let me know if you need any modifications or additional information!