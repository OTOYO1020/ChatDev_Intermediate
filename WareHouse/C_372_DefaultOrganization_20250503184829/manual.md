Here's a detailed user manual for the ABC Counter Application, formatted in Markdown as requested:

```markdown
# ABC Counter Application

A simple application to count occurrences of the substring "ABC" in a mutable string, allowing for character replacements based on user queries.

## Main Functions

The ABC Counter Application provides the following main functionalities:

- **Input Handling**: Reads integer values N (length of the string) and Q (number of queries) from the user.
- **String Modification**: Allows users to replace characters in the string S based on specified queries.
- **Counting Substring**: Counts occurrences of the substring "ABC" in the modified string after each query.
- **Validation**: Ensures that user inputs are valid, including bounds checking for indices and character validation.

## Installation

To run the ABC Counter Application, you need to have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

### Dependencies

The application does not require any external libraries beyond Python's standard library. However, ensure you have Python 3.x installed.

## How to Use the Application

1. **Run the Application**:
   - Open your terminal or command prompt.
   - Navigate to the directory where the application files (`main.py` and `counting.py`) are located.
   - Run the application using the command:
     ```bash
     python main.py
     ```

2. **Input Values**:
   - You will be prompted to enter the values for N and Q. Ensure that both are integers and less than or equal to 1000.
   - Next, enter the string S of length N. The string must consist of uppercase English letters only.
   - For each query, you will be prompted to enter an index (X_i) and a character (C_i). The index should be 1-based and must correspond to a valid position in the string S. The character must be an uppercase English letter.

3. **View Results**:
   - After processing each query, the application will output the count of occurrences of the substring "ABC" in the modified string.

### Example Usage

```
Welcome to the ABC Counter Application. Please enter the values as prompted.
Enter N and Q: 5 2
Enter the string S: ABCDE
Enter query (index and character): 3 A
2
Enter query (index and character): 1 B
1
```

## Error Handling

- The application will validate inputs and prompt the user to re-enter values if they are invalid.
- If the index provided for replacement is out of bounds, the application will notify the user and allow them to try again.
- If the maximum number of attempts for input validation is exceeded, the application will exit gracefully.

## Conclusion

The ABC Counter Application is a straightforward tool for counting specific substrings in a mutable string. It is designed to be user-friendly with built-in validation to ensure correct usage. Enjoy counting!
```

This manual provides a comprehensive overview of the application, including its main functions, installation instructions, usage guidelines, and error handling. Let me know if you need any further modifications or additional information!