Here's the user manual for the software based on the provided task and code structure:

```markdown
# Parentheses and Letter Validation Program

A Python application designed to validate strings containing lowercase letters and parentheses, ensuring that the letters are unique within their respective parentheses.

## Quick Install

To run the application, you need to have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

Once Python is installed, you can clone the repository and run the application directly.

```bash
git clone <repository-url>
cd <repository-directory>
```

## Environment Dependencies

This application requires no additional dependencies beyond Python's standard library. However, it is recommended to use a virtual environment to manage your Python packages.

To create a virtual environment, you can use the following commands:

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

## 🤔 What is this?

This program checks if a given string `S` consists of lowercase English letters and parentheses. It ensures that:

- Each letter is unique within its respective parentheses.
- Parentheses are balanced and properly nested.

### Main Functions

1. **check_parentheses_and_letters(S)**: 
   - Validates the string `S` for unique letters and balanced parentheses.
   - Returns "YES" if the string is valid, otherwise returns "NO".

2. **is_good_string(substring)**: 
   - Checks if a substring contains balanced parentheses.
   - Returns `True` if balanced, otherwise `False`.

3. **validate_input(input_string)**: 
   - Validates the input string to ensure it consists only of lowercase letters and parentheses.
   - Returns `True` if valid, otherwise `False`.

## How to Use

1. **Run the Application**:
   - Execute the main application file `main.py` using Python.

   ```bash
   python main.py
   ```

2. **Input a String**:
   - When prompted, enter a string that consists of lowercase letters and parentheses. For example:
     ```
     Enter a string: a(bc)d(e)
     ```

3. **View the Result**:
   - The program will output either "YES" or "NO" based on the validity of the input string.

### Example Inputs and Outputs

- Input: `a(bc)d(e)`  
  Output: `YES`

- Input: `a(bc)(a)`  
  Output: `NO` (duplicate letter 'a')

- Input: `a(b(c)d)e)`  
  Output: `NO` (unbalanced parentheses)

- Input: `a(b(c)d)`  
  Output: `NO` (unbalanced parentheses)

## 📖 Documentation

For more detailed information on the functions and their usage, please refer to the code comments within the `main.py` and `utils.py` files.

If you encounter any issues or have questions, feel free to reach out for support.

```

This manual provides a comprehensive overview of the software, including installation instructions, usage guidelines, and examples to help users understand how to interact with the application effectively.