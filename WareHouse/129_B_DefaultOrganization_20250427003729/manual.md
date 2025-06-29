```markdown
# Climbing Stairs Application

A Python application designed to calculate the number of ways to climb a staircase while considering broken steps.

## Overview

This application allows users to input the total number of steps and the specific steps that are broken. It utilizes dynamic programming to efficiently compute the number of ways to reach the top of the staircase while avoiding broken steps.

## Main Functions

- **Input Handling**: Reads integers `N` (total steps) and `M` (number of broken steps) from the user. It also reads a list of `M` unique broken steps.
- **Dynamic Programming Calculation**: Computes the number of ways to climb the staircase using a dynamic programming approach, taking into account the broken steps.
- **Output**: Displays the total number of ways to reach the N-th step modulo `1,000,000,007`.

## Installation

To run the Climbing Stairs application, ensure you have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

### Dependencies

This application does not require any external libraries, but it is recommended to use Python 3.6 or higher for compatibility.

## How to Use the Application

1. **Clone the Repository**: If you haven't already, clone the repository containing the application files.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Run the Application**: Execute the `main.py` file to start the application.

   ```bash
   python main.py
   ```

3. **Input the Data**: Follow the prompts to enter:
   - The total number of steps (`N`).
   - The number of broken steps (`M`).
   - A list of `M` unique broken steps (space-separated).

   Example input:
   ```
   Enter N (total steps): 5
   Enter M (number of broken steps): 2
   Enter exactly 2 unique broken steps (space-separated): 2 4
   ```

4. **View the Result**: After entering the data, the application will calculate and display the number of ways to reach the N-th step while avoiding the broken steps.

   Example output:
   ```
   3
   ```

## Error Handling

- The application will prompt you to re-enter the broken steps if:
  - The number of broken steps does not match `M`.
  - The broken steps are not unique or are out of the range `0` to `N`.
- If invalid input is provided for `N` or `M`, an error message will be displayed, and the program will exit.

## Conclusion

The Climbing Stairs application is a simple yet effective tool for calculating the number of ways to navigate a staircase with broken steps. It demonstrates the power of dynamic programming in solving combinatorial problems efficiently.

For any questions or support, please reach out to the development team.
```