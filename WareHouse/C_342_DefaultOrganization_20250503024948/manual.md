Here's a detailed user manual for the character replacement tool, formatted in Markdown as requested:

```markdown
# Character Replacement Tool

A simple Python application for replacing characters in a string based on user-defined pairs.

## Overview

This tool allows users to input a string and a series of character pairs. The application will replace all occurrences of the first character in each pair with the second character, modifying the original string accordingly.

## Main Functions

- **Input Handling**: Reads an integer for the length of the string and the number of character pairs, followed by the string itself and the character pairs.
- **Character Replacement**: Processes the character pairs and replaces occurrences in the string.
- **Output**: Displays the modified string after all replacements have been made.

## Installation

To run the Character Replacement Tool, ensure you have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

### Dependencies

This tool does not require any external libraries beyond Python's standard library. Ensure you have Python 3.x installed.

## How to Use

1. **Clone the Repository**: If you have the code in a repository, clone it to your local machine.
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Run the Application**: Execute the main application file.
   ```bash
   python main.py
   ```

3. **Input Format**:
   - First, input two integers `N` and `Q`, where `N` is the length of the string and `Q` is the number of character pairs.
   - Next, input the string `S` of length `N`.
   - Finally, input `Q` pairs of characters in the format `c_i d_i`, where `c_i` is the character to be replaced and `d_i` is the character to replace it with.

   Example Input:
   ```
   5 2
   hello
   h y
   e a
   ```

4. **Output**: After entering all inputs, the modified string will be printed to the console.

   Example Output:
   ```
   yallo
   ```

## Error Handling

- If the input for character pairs is not in the correct format (i.e., not two single characters), an error message will prompt the user to re-enter the pair.
- The application will continue to prompt for valid input until it receives it.

## Conclusion

The Character Replacement Tool is a straightforward application that demonstrates basic string manipulation in Python. It can be easily extended or modified for more complex use cases.

For any issues or feature requests, please contact the development team.
```

This manual provides a comprehensive guide for users to understand and effectively use the character replacement tool, covering installation, usage, and error handling.