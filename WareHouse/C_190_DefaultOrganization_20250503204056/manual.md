Here's a detailed user manual for the software, formatted in Markdown as requested:

```markdown
# Conditions and Actions Evaluator

A simple application to evaluate conditions based on actions taken on dishes.

## Overview

This application allows users to input a number of dishes, conditions, and actions. The main function of the software is to determine how many conditions can be satisfied based on the actions taken. Each condition consists of two dishes, and each action adds balls to specified dishes. The application will count how many conditions are satisfied based on the actions performed.

## Main Functions

1. **Input Dishes, Conditions, and Actions**:
   - Users can input the number of dishes (N), the number of conditions (M), and the number of actions (K).
   - Conditions are input as pairs of integers representing the dishes that must have balls.
   - Actions are input as pairs of integers representing the dishes to which balls will be added.

2. **Count Satisfied Conditions**:
   - The application evaluates how many of the specified conditions are satisfied based on the actions taken.

## Installation

To run the application, you need to have Python installed on your system. You can install the required dependencies using the following steps:

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**:
   Create a `requirements.txt` file with the following content (if you plan to add dependencies in the future):
   ```
   # Future dependencies can be added here
   ```

   Then, install the dependencies using pip:
   ```bash
   pip install -r requirements.txt
   ```

## How to Use the Application

1. **Run the Application**:
   Execute the main application file:
   ```bash
   python main.py
   ```

2. **Input Data**:
   - You will be prompted to enter the number of dishes (N), conditions (M), and actions (K).
   - Input the conditions as pairs of integers separated by commas (e.g., `1,2`).
   - Input the actions similarly as pairs of integers.

3. **View Results**:
   After entering the conditions and actions, the application will output the number of satisfied conditions based on the actions taken.

## Example Usage

1. Start the application:
   ```
   Enter N (number of dishes): 5
   Enter M (number of conditions): 3
   Enter K (number of actions): 4
   ```

2. Enter conditions:
   ```
   Enter conditions (A_i, B_i) as comma-separated pairs (e.g., '1,2'): 1,2
   Enter conditions (A_i, B_i) as comma-separated pairs (e.g., '1,2'): 2,3
   Enter conditions (A_i, B_i) as comma-separated pairs (e.g., '1,2'): 1,3
   ```

3. Enter actions:
   ```
   Enter actions (C_i, D_i) as comma-separated pairs (e.g., '1,2'): 1,2
   Enter actions (C_i, D_i) as comma-separated pairs (e.g., '1,2'): 2,3
   Enter actions (C_i, D_i) as comma-separated pairs (e.g., '1,2'): 3,4
   Enter actions (C_i, D_i) as comma-separated pairs (e.g., '1,2'): 1,3
   ```

4. View the result:
   ```
   Satisfied Conditions: 2
   ```

## Notes

- Ensure that the input values for conditions and actions are within the range of the number of dishes (1 to N).
- Duplicate conditions and actions are not allowed; the application will prompt you to enter unique values.
- The application handles invalid inputs gracefully and will prompt for re-entry.

## Future Enhancements

This application is designed to be extensible. Future enhancements may include:
- Adding a graphical user interface (GUI).
- Implementing more complex condition evaluations.
- Allowing for batch processing of conditions and actions.

For any issues or feature requests, please reach out to the development team.
```

This manual provides a comprehensive guide for users to understand the functionality of the software, how to install it, and how to use it effectively.