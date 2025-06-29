Here is the `manual.md` file for the string shift application:

```markdown
# String Shift Application

A simple application to compute the lexicographically smallest and largest strings from all possible left and right shifts of a given non-empty string.

## Main Functions

The String Shift Application provides the following functionalities:

- **Left Shift**: Computes all possible left shifts of the input string and determines the smallest and largest strings.
- **Right Shift**: Computes all possible right shifts of the input string and updates the smallest and largest strings accordingly.
- **Input Handling**: Prompts the user for a non-empty string and handles input errors gracefully.

## Installation

To run the String Shift Application, you need to have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Environment Dependencies

This application requires no external libraries beyond the standard Python library. Simply ensure you have Python 3.x installed.

## How to Use

1. **Clone the Repository**: If you have the source code in a repository, clone it to your local machine. If you don't have it yet, you can create two files: `main.py` and `shift_utils.py` with the provided code.

2. **Run the Application**:
   - Open your terminal or command prompt.
   - Navigate to the directory where your `main.py` file is located.
   - Run the application using the following command:
     ```bash
     python main.py
     ```

3. **Input a String**: When prompted, enter a non-empty string. The application will then compute the smallest and largest strings from all possible shifts.

4. **View Results**: After processing, the application will print the lexicographically smallest and largest strings.

### Example Usage

```plaintext
Enter a non-empty string: hello
Smallest: ehllo, Largest: ohell
```

## Error Handling

- If you enter an empty string, the application will prompt you with an error message:
  ```plaintext
  Input Error: Please enter a non-empty string.
  ```

## Conclusion

The String Shift Application is a straightforward tool for exploring string manipulations through shifts. It provides a clear interface for users to input their strings and receive immediate feedback on the smallest and largest shifts.

For any issues or feature requests, please reach out to the development team.
```

This manual provides a comprehensive guide for users to understand the application, its functionality, and how to get started.