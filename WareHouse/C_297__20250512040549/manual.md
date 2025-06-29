Here is the `manual.md` file for the string replacement application, detailing its main functions, installation instructions, and usage guidelines.

```markdown
# String Replacement Application

A simple application designed to replace occurrences of 'TT' with 'PC' in a list of strings. This application allows users to input multiple strings and processes them to provide modified outputs.

## Main Functions

- **Input Handling**: The application prompts the user to enter multiple strings, one per line, until an empty line is entered.
- **String Processing**: The core functionality of the application is to replace all occurrences of 'TT' with 'PC' in each input string while ensuring that replacements do not overlap.
- **Output Generation**: The modified strings are displayed to the user after processing.

## Quick Install

To run this application, you need to have Python installed on your system. You can install the required dependencies using pip:

```bash
pip install typing
```

## 🤔 What is this application?

This application is designed to demonstrate basic string manipulation in Python. It allows users to input a list of strings and processes them to replace specific substrings ('TT') with another substring ('PC'). This can be useful in various scenarios, such as text processing, data cleaning, or simply for educational purposes.

## How to Use the Application

1. **Run the Application**: Execute the `main.py` file in your terminal or command prompt.

   ```bash
   python main.py
   ```

2. **Input Strings**: When prompted, enter your strings one by one. Press `Enter` after each string. To finish inputting strings, simply press `Enter` on an empty line.

3. **View Output**: After processing, the application will display the modified strings, where all occurrences of 'TT' have been replaced with 'PC'.

### Example Usage

- Input:
  ```
  TTTT
  Hello World
  Test String
  TT
  ```
  
- Output:
  ```
  PCPC
  Hello World
  PesPC String
  P
  ```

## Error Handling

- If no strings are entered, the application will notify the user that no strings were provided.
- If any string exceeds the maximum length (set to 100 characters), the application will raise a ValueError and inform the user.

## Additional Notes

- The application is designed to handle edge cases, ensuring that if no replacements can be made, the original strings are returned unchanged.
- The maximum length of strings can be adjusted in the `main.py` file as needed.

For any further questions or support, please reach out to the development team.
```

This manual provides a comprehensive guide for users to understand and effectively utilize the string replacement application.