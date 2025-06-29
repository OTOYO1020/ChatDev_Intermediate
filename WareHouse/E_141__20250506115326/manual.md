Here's a detailed user manual for the substring finder application, formatted in Markdown as requested:

```markdown
# Substring Finder Application

## Overview

The Substring Finder Application is designed to efficiently identify the maximum length of non-overlapping substrings that occur at least twice within a given string. This tool is particularly useful for developers and data analysts who need to analyze string patterns in their datasets.

## Main Functions

- **Input Handling**: The application reads an integer `N` and a string `S` from standard input.
- **Substring Analysis**: It analyzes the string `S` to find the maximum length of contiguous substrings that appear at least twice without overlapping.
- **Output**: The application prints the maximum length of the identified non-overlapping substring.

## Installation

To run the Substring Finder Application, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. **Install Python**: Ensure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: If you haven't already, clone the repository containing the application files.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

3. **Install Dependencies**: The application does not have any external dependencies beyond Python's standard library, so no additional installations are required.

## Usage

To use the Substring Finder Application, follow these steps:

1. **Run the Application**: Open your terminal or command prompt, navigate to the directory where the application files are located, and run the following command:

   ```bash
   python main.py
   ```

2. **Input the Data**: The application will prompt you to enter an integer `N` (the length of the string) and then the string `S`. Make sure that the length of `S` is at least `N`.

   ```
   Enter an integer N (length of the string): 5
   Enter a string S: ababc
   ```

3. **View the Result**: After entering the inputs, the application will process the data and print the maximum length of the non-overlapping substring found.

   ```
   Max Length of non-overlapping substring: 2
   ```

## Example

Here’s a quick example of how to use the application:

1. Run the application:

   ```bash
   python main.py
   ```

2. Input the following when prompted:

   ```
   Enter an integer N (length of the string): 6
   Enter a string S: abcabc
   ```

3. The output will be:

   ```
   Max Length of non-overlapping substring: 3
   ```

## Conclusion

The Substring Finder Application is a powerful tool for analyzing string patterns and can be easily integrated into larger data processing workflows. For any issues or feature requests, please reach out to the development team.

```

This manual provides a comprehensive guide for users to understand the functionality of the Substring Finder Application, how to install it, and how to use it effectively.