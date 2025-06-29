Here’s a detailed user manual for the cookie counting software, formatted in Markdown:

```markdown
# Cookie Counter

A simple application to count remaining cookies after marking duplicates based on color.

## Introduction

The Cookie Counter application allows users to input a grid of cookies represented by their colors. The application processes this grid to identify and remove cookies that have duplicates in either rows or columns. The final output is the count of remaining cookies after all duplicates have been marked and removed.

## Main Functions

- **Input Handling**: Accepts a grid of cookies in a user-friendly format.
- **Duplicate Detection**: Iterates through rows and columns to identify cookies with duplicate colors.
- **Cookie Removal**: Removes marked cookies from the grid until no duplicates remain.
- **Remaining Count**: Returns the count of cookies that remain after the removal process.

## Installation

To run the Cookie Counter application, you need to have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

### Dependencies

The application requires no additional dependencies beyond Python's standard library.

## How to Use

1. **Run the Application**: 
   - Open your terminal or command prompt.
   - Navigate to the directory where the `main.py` file is located.
   - Run the application using the command:
     ```bash
     python main.py
     ```

2. **Input Format**:
   - When prompted, enter the cookie grid in the following format:
     - Rows should be separated by a semicolon (`;`).
     - Colors within a row should be separated by a comma (`,`).
   - Example input:
     ```
     red,blue,red;green,green,blue;yellow,red,yellow
     ```

3. **Output**:
   - After processing the input, the application will display the count of remaining cookies.

## Example

### Input
```
red,blue,red;green,green,blue;yellow,red,yellow
```

### Output
```
Remaining Cookies: 3
```

## Error Handling

- If the input grid does not have uniform row lengths, the application will display an error message:
  ```
  Error: All rows must have the same number of columns.
  ```

## Conclusion

The Cookie Counter application is a straightforward tool for counting remaining cookies after removing duplicates. It is designed to be user-friendly and efficient, making it easy for anyone to use. For any further questions or support, please reach out to our development team.
```

This manual provides a comprehensive overview of the application, including installation instructions, usage guidelines, and examples to help users effectively utilize the Cookie Counter software.