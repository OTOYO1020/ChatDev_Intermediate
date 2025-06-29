Here's the `manual.md` file that provides a detailed user manual for the software developed to solve the customer's task:

```markdown
# Ball Arrangement Calculator

A command-line application to calculate the number of arrangements of balls using combinatorial methods.

## Overview

This software allows users to input the number of blue and total balls, and it computes the number of ways to arrange these balls based on specified conditions. The application utilizes combinatorial counting to determine valid arrangements, ensuring that the output is efficient and accurate.

## Main Functions

- **Input Handling**: Reads integers K (number of blue balls) and N (total number of balls) from standard input.
- **Arrangement Calculation**: Computes the number of arrangements for each possible number of moves using combinatorial methods.
- **Output**: Displays the number of arrangements for each move count from 1 to K.

## Installation

To run the application, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. **Install Python**: Ensure you have Python 3.6 or higher installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: Clone the repository containing the code to your local machine.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

3. **Install Dependencies**: Create a virtual environment and install the required dependencies. You can use `pip` to install the necessary libraries.

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

## Usage

To use the application, follow these steps:

1. **Run the Application**: Execute the `main.py` file from the command line.

   ```bash
   python main.py
   ```

2. **Input Values**: When prompted, enter the number of blue balls (K) and the total number of balls (N).

   ```
   Enter K (number of blue balls): 3
   Enter N (total number of balls): 5
   ```

3. **View Results**: The application will calculate and display the number of arrangements for each move count from 1 to K.

   ```
   Ways to arrange:
   10
   6
   1
   ```

## Example

For example, if you input K = 3 and N = 5, the output will show the number of ways to arrange the balls with the specified conditions.

## Notes

- The application uses combinatorial methods to ensure efficient calculation of arrangements.
- The results are computed modulo \(10^9 + 7\) to handle large numbers and prevent overflow.

## Future Enhancements

If you anticipate future expansions that may require additional libraries or functionalities, please feel free to reach out for support or suggestions.

For any issues or feature requests, please contact the development team.

```

This manual provides a comprehensive guide for users to understand the software's functionality, installation process, and usage instructions.