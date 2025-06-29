```markdown
# Submission Results Calculator

A simple application for processing programming contest submissions and calculating results based on verdicts.

## Overview

The Submission Results Calculator allows users to input programming contest submissions and receive feedback on the number of correct answers and total penalties incurred. The application is built using Python and utilizes a graphical user interface (GUI) for ease of use.

## Main Functions

- **Input Submissions**: Users can enter submissions in the format `problem_id verdict` (e.g., `1 AC` or `2 WA`).
- **Calculate Results**: The application calculates the total number of correct answers and the total penalties based on the submissions provided.
- **Display Results**: Results are displayed in the GUI after calculations are performed.

## Installation

To run the Submission Results Calculator, you need to have Python installed on your machine. Follow the steps below to set up the environment:

1. **Install Python**: Ensure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **Install Required Libraries**: Open your terminal or command prompt and run the following command to install the required libraries:

   ```bash
   pip install tkinter
   ```

   Note: `tkinter` is usually included with Python installations, but if you encounter any issues, you may need to install it separately based on your operating system.

## How to Use the Application

1. **Run the Application**: Execute the `main.py` file to start the application. You can do this by navigating to the directory where the file is located and running:

   ```bash
   python main.py
   ```

2. **Input Submissions**:
   - In the text area, enter your submissions in the format `problem_id verdict`, one per line.
   - Example:
     ```
     1 AC
     2 WA
     1 WA
     3 AC
     ```

3. **Enter N and M**:
   - Enter the total number of problems (N) in the corresponding input field.
   - Enter the maximum number of submissions (M) allowed.

4. **Calculate Results**: Click the "Calculate Results" button to process the submissions.

5. **View Results**: The results will be displayed below the input fields, showing the number of correct answers and total penalties.

## Example Usage

- **Input**:
  ```
  1 AC
  2 WA
  1 WA
  3 AC
  ```
  - N: 3
  - M: 4

- **Output**:
  ```
  Correct Answers: 2
  Total Penalties: 2
  ```

## Troubleshooting

- **Invalid Input Format**: Ensure that each submission is entered correctly in the format `problem_id verdict`.
- **Value Errors**: If you enter non-integer values for N or M, the application will prompt you to enter valid integers.

## Conclusion

The Submission Results Calculator is a straightforward tool for evaluating programming contest submissions. By following the installation and usage instructions, users can easily calculate their results and gain insights into their performance.
```