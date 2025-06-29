```markdown
# Max Score Calculator

A Python application designed to calculate the maximum score based on user-defined sequences and queries.

## Overview

The Max Score Calculator allows users to input parameters for generating non-decreasing sequences and evaluate them against a set of queries to determine the maximum score. The application is built using Python and provides both a command-line interface and a graphical user interface (GUI) for ease of use.

## Main Functions

- **Input Parameters**: Users can input the values for N (length of the sequence), M (maximum value in the sequence), and Q (number of queries).
- **Queries**: Users can enter queries in the format `a,b,c,d`, where:
  - `a`: starting index of the sequence
  - `b`: ending index of the sequence
  - `c`: the difference to check between the sequence values
  - `d`: the score to add if the condition is met
- **Score Calculation**: The application calculates the maximum score based on the valid sequences and queries provided.

## Installation

To run the Max Score Calculator, you need to have Python installed on your system. Follow these steps to set up the environment:

1. **Install Python**: Download and install Python from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: Clone the repository containing the application code.
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

3. **Install Dependencies**: Use pip to install any required dependencies.
   ```bash
   pip install -r requirements.txt
   ```

## How to Use

### Command-Line Interface

1. Run the application:
   ```bash
   python main.py
   ```

2. Follow the prompts to enter values for N, M, and Q.

3. Enter the queries in the specified format (one per line), and finish by pressing Enter on an empty line.

4. The application will display the maximum score calculated based on the input.

### Graphical User Interface (GUI)

1. Run the application:
   ```bash
   python gui.py
   ```

2. Fill in the input fields for N, M, and Q.

3. Enter the queries in the format `a,b,c,d;...` in the provided input field.

4. Click the "Calculate Max Score" button to compute the maximum score.

5. The result will be displayed below the button.

## Example Usage

- **Input**:
  ```
  N: 3
  M: 5
  Q: 2
  Queries:
  1,2,1,10
  2,3,2,20
  ```

- **Output**:
  ```
  Max Score: 30
  ```

## Troubleshooting

- Ensure that all input values are positive integers.
- Check the query format; it should be `a,b,c,d` and separated by semicolons for multiple queries.
- If you encounter any errors, please refer to the error messages displayed in the console or GUI for guidance.

## Support

For further assistance or to report issues, please contact the support team or refer to the documentation provided within the application.

```
