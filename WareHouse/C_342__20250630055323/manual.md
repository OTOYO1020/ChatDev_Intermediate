Here's a detailed user manual for the String Replacer application in Markdown format:

```markdown
# String Replacer

A simple application for replacing characters in a string based on user-defined operations.

## Quick Install

To run the String Replacer application, you need to have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

Once Python is installed, you can set up the environment and install the necessary dependencies using pip. Open your terminal or command prompt and run the following command:

```bash
pip install -r requirements.txt
```

*Note: Ensure you have a `requirements.txt` file that lists any additional dependencies if needed.*

## 🤔 What is this?

The String Replacer application allows users to perform multiple character replacements in a given string. Users can specify pairs of characters, and the application will replace all occurrences of the first character with the second character in the string. This can be useful for text processing tasks, such as formatting or data cleaning.

### Main Functions

1. **Read Input**: The application reads an integer N (length of the string) and Q (number of replacement operations) from standard input.
2. **Character Replacement**: For each operation, the user specifies a pair of characters (c_i, d_i). The application replaces all occurrences of c_i in the string with d_i.
3. **Output**: After all operations are completed, the modified string is printed as output.

## 📖 How to Use

1. **Run the Application**: Execute the main application file `main.py` in your terminal or command prompt.

   ```bash
   python main.py
   ```

2. **Input Format**: When prompted, provide the following inputs:
   - First, enter the integer values N and Q separated by a space.
   - Next, enter the string S of length N.
   - For each of the Q operations, enter the character pairs (c_i, d_i) separated by a space.

   **Example Input:**
   ```
   5 2
   hello
   h y
   o a
   ```

3. **Output**: The application will output the modified string after performing all the specified replacements.

   **Example Output:**
   ```
   yella
   ```

## 🛠️ Dependencies

The application relies on the following Python modules:
- No external libraries are required beyond the standard Python library.

## 📄 Documentation

For more detailed information about the code structure and functions, refer to the source files:
- `main.py`: Contains the main application logic.
- `utils.py`: Contains utility functions for character replacement.

Feel free to modify the code to suit your specific needs or to add additional features!

## 🤝 Support

If you encounter any issues or have questions about using the String Replacer application, please reach out to our support team at support@chatdev.com.

Happy coding!
```

This manual provides a comprehensive overview of the String Replacer application, including installation instructions, usage guidelines, and support information.