Here is the user manual for the unique sums calculator software, formatted in Markdown as requested:

```markdown
# Unique Sums Calculator

A software tool designed to calculate unique sums of selected integers based on user-defined parameters.

## Overview

The Unique Sums Calculator allows users to input two integers, N and K, and computes the number of unique sums that can be formed by selecting subsets of integers ranging from \(10^{100}\) to \(10^{100} + N\). The sums are calculated for all subset sizes from K to N, and the results are displayed in a user-friendly interface.

## Main Functions

- **Input Handling**: Users can enter values for N and K through a graphical user interface (GUI).
- **Sum Calculation**: The software calculates unique sums based on the provided integers and stores them in a set to ensure uniqueness.
- **Output Display**: The results, including the count of unique sums, are displayed in the GUI.

## Installation

To run the Unique Sums Calculator, you need to have Python installed on your system. Follow these steps to set up the environment:

1. **Install Python**: Ensure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **Install Required Dependencies**: Open your terminal or command prompt and run the following command to install the necessary dependencies:

   ```bash
   pip install tkinter
   ```

   Note: Tkinter is included with most Python installations, but if you encounter any issues, ensure it is installed.

## How to Use

1. **Run the Application**: Execute the `main.py` file to start the application. You can do this by navigating to the directory containing the file in your terminal and running:

   ```bash
   python main.py
   ```

2. **Input Values**: In the GUI that appears, enter the values for N and K:
   - **N**: The upper limit for generating integers (must be a non-negative integer).
   - **K**: The minimum size of subsets to consider (must be a non-negative integer).

3. **Submit Values**: After entering the values, the application will process the input and calculate the unique sums.

4. **View Results**: The count of unique sums will be displayed in the output section of the GUI.

## Example Usage

- If you enter `N = 5` and `K = 2`, the application will generate integers from \(10^{100}\) to \(10^{100} + 5\) and calculate the unique sums for all combinations of these integers with sizes ranging from 2 to 6.

## Troubleshooting

- **Invalid Input**: If you enter non-integer values or negative integers, an error message will be displayed in the GUI.
- **Performance Issues**: The application limits N to a maximum of 100 to ensure performance. If you enter a value greater than 100, an error message will prompt you to enter a smaller value.

## Conclusion

The Unique Sums Calculator is a powerful tool for exploring combinations of large integers and their sums. With its intuitive GUI and straightforward functionality, users can easily compute and analyze unique sums based on their input parameters.

For further assistance or feedback, please contact our support team.
```

This manual provides a comprehensive guide for users to understand the software's functionality, installation process, and usage instructions.