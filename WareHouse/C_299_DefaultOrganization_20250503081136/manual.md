Here’s a detailed user manual for the Dango String Analyzer software, formatted in Markdown:

```markdown
# Dango String Analyzer

## Introduction

The Dango String Analyzer is a Python application designed to analyze strings composed of characters '-' and 'o'. It identifies the greatest level of "dango strings" based on the arrangement of these characters. A dango string is defined by the number of 'o' characters that surround a '-' character, and the level of the dango string is determined by the minimum count of 'o' characters on either side of the '-'.

## Main Functions

- **Input Handling**: The application reads an integer \( N \) and a string \( S \) from the user.
- **Validation**: It checks that the string contains only valid characters ('-' and 'o') and that it is not empty.
- **Dango Level Calculation**: The application calculates the greatest level of dango string found in the input string.
- **Output**: It prints the greatest level of dango string or an error message if no valid dango string is found.

## Installation

To run the Dango String Analyzer, you need to have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

### Dependencies

The application does not have any external dependencies beyond Python itself. Ensure you have Python 3.x installed.

## How to Use

1. **Clone the Repository**: If you have the source code, clone the repository to your local machine.
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Run the Application**: Execute the main application file.
   ```bash
   python main.py
   ```

3. **Input Requirements**:
   - When prompted, enter an integer \( N \) which represents the length of the string you want to analyze.
   - Enter the string \( S \) containing only the characters '-' and 'o'.

4. **Output**: After processing the input, the application will display the greatest level of dango string found in the input string.

### Example Usage

```plaintext
Enter an integer N (length of string to analyze): 10
Enter a string S (containing '-' and 'o' only): oo-o-o-o-o
Greatest level of dango string: 2
```

## Error Handling

- If the string \( S \) is empty, the application will notify you and exit.
- If the string contains invalid characters, it will display an error message.
- If the input integer \( N \) is not a valid integer, it will prompt you to enter a valid integer.

## Conclusion

The Dango String Analyzer is a simple yet effective tool for analyzing specific string patterns. It is designed to be user-friendly and provides clear feedback on input errors. For any further questions or support, please reach out to the development team.
```

This manual provides a comprehensive overview of the Dango String Analyzer, including installation instructions, usage guidelines, and error handling. It is structured to be easily readable and informative for users.