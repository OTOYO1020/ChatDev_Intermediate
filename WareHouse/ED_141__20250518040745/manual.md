Here's a detailed user manual for the software, formatted in Markdown as requested:

```markdown
# Repeated Substring Finder

A simple application to find the maximum length of a non-empty substring that occurs twice or more in a given string.

## Overview

The Repeated Substring Finder is designed to help users identify the longest repeated substring within a string input. This application is particularly useful for text analysis, data processing, and other scenarios where substring repetition is relevant.

## Main Functions

- **max_length_repeated_substring(S: str) -> int**: This function encapsulates the logic for finding the maximum length of a non-empty substring that occurs twice or more in the input string `S`. It returns the length of the longest repeated substring.

## Installation

To run the application, you need to have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

### Environment Dependencies

1. **Python**: Make sure you have Python 3.x installed.
2. **No additional libraries are required** for this application, as it uses built-in Python functionality.

## How to Use

1. **Clone the Repository**: Start by cloning the repository to your local machine.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Run the Application**: You can run the application by executing the `main.py` file.

   ```bash
   python main.py
   ```

3. **Input Handling**: When prompted, enter a string that you want to analyze. The application requires a string with at least two characters.

   ```
   Enter a string: your_input_string_here
   ```

4. **Output**: The application will output the maximum length of the repeated substring found in the input string.

   ```
   3  # Example output indicating the length of the longest repeated substring
   ```

## Example Usage

- **Input**: `banana`
- **Output**: `3` (The substring `ana` is repeated)

- **Input**: `abcabc`
- **Output**: `3` (The substring `abc` is repeated)

## Error Handling

- If the input string is empty or has less than two characters, the application will prompt an error message:

   ```
   Input Error: Please enter a string with at least two characters.
   ```

## Conclusion

The Repeated Substring Finder is a straightforward tool for identifying repeated substrings in a given string. With its simple interface and efficient logic, it can be a valuable asset for anyone needing to analyze text for repeated patterns.

For any questions or support, please contact the development team at ChatDev.
```

This manual provides a comprehensive guide for users to understand the functionality, installation, and usage of the Repeated Substring Finder application.