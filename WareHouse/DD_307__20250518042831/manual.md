Here's a detailed user manual for the `remove_contiguous_substrings` function, formatted in Markdown as requested:

```markdown
# Remove Contiguous Substrings

A simple utility for processing strings by removing characters enclosed within unmatched parentheses.

## Overview

The `remove_contiguous_substrings` function is designed to take a string input and remove characters that are enclosed within unmatched parentheses. This utility is particularly useful for cleaning up strings that may contain unnecessary or malformed data due to parentheses.

## Main Functions

- **remove_contiguous_substrings(S)**: 
  - **Input**: A string `S` which may contain characters and parentheses.
  - **Output**: A modified string with characters inside unmatched parentheses removed.
  - **Behavior**: 
    - Characters enclosed within matched parentheses are ignored.
    - Characters outside of unmatched parentheses are retained.

## Installation

To run the application, you need to have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Environment Setup

1. **Clone the Repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**:
   Ensure you have the required dependencies installed. You can use `pip` to install any necessary packages. For this application, no external packages are required beyond Python's standard library.

## Usage

1. **Run the Application**:
   - Navigate to the directory where `main.py` is located.
   - Execute the following command in your terminal:
     ```bash
     python main.py
     ```

2. **Input**:
   - When prompted, enter a string that may contain parentheses. For example:
     ```
     Enter a string (parentheses will be processed): a(bc)d(e(f)g)h
     ```

3. **Output**:
   - The application will process the input string and print the modified string. For the above input, the output would be:
     ```
     Modified String: adh
     ```

## Example

### Input:
```
Enter a string (parentheses will be processed): a(bc)d(e(f)g)h
```

### Output:
```
Modified String: adh
```

### Explanation:
In the input string, the characters `bc` and `ef` are enclosed within parentheses and are thus removed from the output.

## Conclusion

The `remove_contiguous_substrings` function is a straightforward utility for cleaning up strings by removing unwanted characters enclosed in unmatched parentheses. It can be easily integrated into larger applications or used as a standalone tool for string processing tasks.

For any questions or support, please contact the development team.
```

This manual provides a comprehensive guide for users to understand the functionality, installation process, and usage of the `remove_contiguous_substrings` function.