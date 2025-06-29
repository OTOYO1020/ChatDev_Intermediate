Here's a detailed user manual for the LexicoSorter application, formatted in Markdown as requested:

```markdown
# LexicoSorter

A simple application to sort strings in lexicographical order.

## Introduction

LexicoSorter is a Python application designed to take an input string, validate its length, and return the lexicographically smallest permutation of that string. This application is useful for anyone needing to sort characters in a string for various applications, such as data processing, text analysis, or simply for educational purposes.

## Main Functions

- **Input Validation**: Ensures the input string is between 1 and 200,000 characters.
- **Character Sorting**: Converts the string into a list of characters, sorts them in lexicographical order, and joins them back into a string.
- **Output**: Prints the sorted string to the console.

## Installation

To run the LexicoSorter application, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. **Install Python**: Download and install Python from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: If you have Git installed, you can clone the repository using the following command:
   ```bash
   git clone <repository-url>
   cd lexico_sorter
   ```

3. **Install Dependencies**: Although this application does not have external dependencies, ensure you have Python's standard library available. You can check your Python installation by running:
   ```bash
   python --version
   ```

## How to Use LexicoSorter

1. **Run the Application**: Open your terminal or command prompt, navigate to the directory where `main.py` is located, and run the following command:
   ```bash
   python main.py
   ```

2. **Input String**: When prompted, enter a string that is between 1 and 200,000 characters long. For example:
   ```
   Please enter a string between 1 and 200,000 characters:
   hello world
   ```

3. **Output**: The application will process your input and print the sorted string. For the example above, the output will be:
   ```
   dehllloorw
   ```

4. **Error Handling**: If the input string does not meet the length requirements, the application will prompt you to try again:
   ```
   Input must be a non-empty string between 1 and 200,000 characters.
   ```

## Example Usage

Here’s a quick example of how the application works:

```bash
$ python main.py
Please enter a string between 1 and 200,000 characters:
banana
abann
```

## Conclusion

LexicoSorter is a straightforward tool for sorting strings in lexicographical order. It is designed to be user-friendly and efficient, making it suitable for a variety of applications. For any issues or further inquiries, please refer to the documentation or contact support.

```

This manual provides a comprehensive overview of the LexicoSorter application, including its purpose, installation instructions, and usage guidelines. Let me know if you need any further modifications or additional information!