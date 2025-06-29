Here's a detailed user manual for the Extended ABC string checker software, formatted in Markdown:

```markdown
# Extended ABC String Checker

A simple application to determine if a given string is an Extended ABC string based on specific criteria.

## Main Functions

The Extended ABC String Checker performs the following main functions:

1. **Input Handling**: Receives a string input consisting of characters 'A', 'B', and 'C'.
2. **Counting Characters**: Initializes counters for 'A', 'B', and 'C' and counts their occurrences in the input string.
3. **Validation**: Checks if the string meets the criteria for being an Extended ABC string:
   - The string must start with 'A' and end with 'C' after the last 'B'.
   - All 'B's must be located between the last 'A' and the first 'C'.
4. **Output**: Returns 'Yes' if the string is an Extended ABC string; otherwise, returns 'No'.

## Installation

To run the Extended ABC String Checker, you need to have Python installed on your machine. Follow the steps below to set up the environment:

1. **Install Python**: Ensure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: Clone the repository containing the code files.
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

3. **Install Dependencies**: If there are any additional dependencies, you can install them using pip. For this application, no external libraries are required, but ensure you have the latest version of Python.

## How to Use

1. **Run the Application**: Navigate to the directory where the `main.py` file is located and run the following command:
   ```bash
   python main.py
   ```

2. **Input the String**: When prompted, enter a string consisting of characters 'A', 'B', and 'C'. For example:
   ```
   Enter a string (A, B, C): ABBCAC
   ```

3. **View the Result**: The application will process the input string and output either 'Yes' or 'No' based on whether the string is an Extended ABC string.

## Example Usage

Here are a few examples of how the application works:

- **Example 1**:
  ```
  Input: ABBCAC
  Output: Yes
  ```

- **Example 2**:
  ```
  Input: AABBC
  Output: No
  ```

- **Example 3**:
  ```
  Input: CBA
  Output: No
  ```

## Conclusion

The Extended ABC String Checker is a straightforward tool for validating strings based on specific character arrangements. For any issues or further inquiries, please contact our support team.

```

This manual provides a comprehensive overview of the software, including its main functions, installation instructions, usage guidelines, and example scenarios to help users understand how to interact with the application effectively.