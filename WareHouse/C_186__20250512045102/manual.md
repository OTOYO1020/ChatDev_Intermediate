Here's a detailed user manual for the software that implements the function `count_integers_without_7`. This manual provides an overview of the software, installation instructions, and usage guidelines.

```markdown
# Count Integers Without 7

A simple application to count integers from 1 to N that do not contain the digit '7' in either their decimal or octal representations.

## Main Functions

The primary function of this software is `count_integers_without_7(N: int) -> int`, which performs the following tasks:

- Iterates through all integers from 1 to N (inclusive).
- Checks if each integer contains the digit '7' in its decimal representation.
- If the integer does not contain '7' in decimal, it checks the octal representation.
- Counts and returns the number of integers that do not contain '7' in both representations.

## Quick Install

To run this application, you need to have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

### Dependencies

This application does not require any external libraries, as it uses built-in Python functionalities.

## How to Use

1. **Clone the Repository**: If you have the code in a repository, clone it to your local machine. If you are starting from scratch, create two files named `main.py` and `counter.py` and copy the provided code into these files.

2. **Run the Application**:
   - Open a terminal or command prompt.
   - Navigate to the directory where your `main.py` file is located.
   - Execute the following command:
     ```bash
     python main.py
     ```

3. **Input**: When prompted, enter an integer value for N (where 1 ≤ N ≤ 100000). The program will validate your input.
   - If the input is valid, it will call the function `count_integers_without_7` and display the count of valid integers.
   - If the input is invalid, it will prompt you to enter a valid integer.

4. **Output**: The application will print the count of integers from 1 to N that do not contain the digit '7' in either their decimal or octal representation.

## Example Usage

```plaintext
Enter an integer N (1 ≤ N ≤ 100000): 20
Count: 17
```

In this example, the application counts the integers from 1 to 20 that do not contain the digit '7' in either representation.

## Error Handling

The application includes basic error handling for invalid inputs:
- If the input is not an integer, it will prompt the user to enter a valid integer.
- If the input integer is outside the range of 1 to 100000, it will notify the user to enter a number within the specified range.

## Conclusion

This application provides a straightforward way to count integers without the digit '7' in their decimal or octal forms. It is designed to be user-friendly and efficient, leveraging Python's built-in capabilities.

For any further questions or support, please reach out to the development team.
```

This manual provides a comprehensive overview of the software, ensuring that users can easily understand how to install and use the application effectively.