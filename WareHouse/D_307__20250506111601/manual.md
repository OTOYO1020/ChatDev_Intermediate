Here's a detailed user manual for the string processing application, formatted in Markdown as requested:

```markdown
# String Processing Application

A simple application to process strings by removing unmatched parentheses and retaining valid characters.

## Main Functions

The application provides the following main functions:

- **Read Input**: Accepts an integer N and a string S from the user.
- **Process String**: Removes unmatched opening and closing parentheses while retaining lowercase letters.
- **Output Result**: Displays the processed string containing valid characters.

## Quick Install

To run the application, ensure you have Python installed on your system. You can install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt` file, you can manually ensure you have the necessary Python version (3.6 or higher) and install any additional libraries as needed.

## 🤔 What is this?

The String Processing Application is designed to help users clean up strings by removing unmatched parentheses. This is particularly useful in scenarios where parentheses are used for grouping or nesting, and you want to ensure that only valid characters remain.

### Key Features:

- **Handles unmatched parentheses**: The application intelligently processes the input string to remove unmatched parentheses.
- **Retains valid characters**: Only lowercase letters and unmatched closing parentheses are retained in the output.
- **User-friendly interface**: Simple prompts guide the user through inputting data.

## 📖 How to Use

1. **Run the Application**: Execute the main application file `main.py` in your terminal or command prompt.

   ```bash
   python main.py
   ```

2. **Input Data**:
   - When prompted, enter an integer N, which specifies the number of characters to consider from the string.
   - Next, enter the string S that you want to process.

3. **View Results**: After processing, the application will display the resulting string, which contains only the valid characters.

### Example Usage:

```plaintext
Enter an integer N: 10
Enter a string: a(b(c)d)e)f(g)
Result: abcd)f
```

In this example, the application processes the string `a(b(c)d)e)f(g)` considering only the first 10 characters and outputs `abcd)f`, removing unmatched parentheses.

## Error Handling

- If the input string is empty, the application will prompt the user to enter a valid string.
- If the integer N exceeds the length of the string, it will automatically limit N to the length of the string.

## Conclusion

This String Processing Application is a straightforward tool for managing strings with parentheses. It can be easily extended or integrated into larger applications as needed. For any issues or feature requests, please contact the development team.

```

This manual provides a comprehensive overview of the application, including installation instructions, usage guidelines, and error handling. Let me know if you need any modifications or additional information!