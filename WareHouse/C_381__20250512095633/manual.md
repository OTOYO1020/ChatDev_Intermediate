Here's a detailed user manual for the software that implements the `max_11_22_length` function, formatted in Markdown as requested:

```markdown
# 11/22 String Finder

A Python application to find the maximum length of contiguous substrings that are classified as 11/22 strings.

## Overview

The 11/22 String Finder is designed to analyze a given string and identify the longest contiguous substring that meets the criteria of an 11/22 string. An 11/22 string is defined as having the following properties:
- The first half consists entirely of '1's.
- The middle character is '/'.
- The second half consists entirely of '2's.

## Features

- Efficiently finds the maximum length of valid 11/22 substrings.
- Handles strings of length up to 200,000 characters.
- Provides error handling for invalid inputs.

## Installation

To run the application, ensure you have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

### Dependencies

This application requires no external libraries, as it uses only built-in Python functionalities.

### Running the Application

1. Clone the repository or download the source code files (`main.py` and `utils.py`).
2. Open a terminal or command prompt.
3. Navigate to the directory where the files are located.
4. Run the application using the following command:

   ```bash
   python main.py
   ```

## How to Use

1. When prompted, enter a string that meets the following criteria:
   - Length between 1 and 200,000 characters.
   - Must contain at least one '/' character.
   
   Example input: `111/2222111`

2. The application will process the input and output the maximum length of the contiguous 11/22 substring found. If no valid substring is found, it will inform you accordingly.

### Example Outputs

- Input: `111/2222111`
  - Output: `Max Length: 9`
  
- Input: `111/222`
  - Output: `Max Length: 5`
  
- Input: `123/456`
  - Output: `No valid 11/22 substring found.`

## Error Handling

- If the input string does not meet the length requirements, an error message will be displayed.
- If the input string does not contain a '/', an error message will be displayed.

## Conclusion

The 11/22 String Finder is a powerful tool for analyzing strings based on specific criteria. It is designed for efficiency and ease of use, making it suitable for developers and users who need to process large strings quickly.

For further assistance or inquiries, please contact the support team.
```

This manual provides a comprehensive guide for users to understand the functionality of the software, how to install it, and how to use it effectively.