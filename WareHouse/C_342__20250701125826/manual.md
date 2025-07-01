Here's a detailed user manual for the String Modifier software, formatted in Markdown as requested:

```markdown
# String Modifier

A simple application for modifying strings by replacing specified characters based on user-defined pairs.

## Quick Install

To set up the environment for the String Modifier, you can create a virtual environment and install the necessary dependencies. Since this project is self-contained and does not rely on any third-party libraries, no additional installations are required. However, you can create a `requirements.txt` file for future enhancements.

1. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

2. **Install dependencies (if any are added in the future):**
   ```bash
   pip install -r requirements.txt
   ```

## 🤔 What is this?

The String Modifier is a Python application that allows users to modify a given string by replacing specified characters based on a list of character pairs. This functionality can be useful in various scenarios, such as text processing, data cleaning, or simply for fun.

## 📖 Main Functions

### 1. Input Parameters

- **N**: An integer representing the length of the string.
- **Q**: An integer representing the number of character replacement operations.
- **S**: A string of length N that will be modified.
- **Pairs**: A list of Q pairs of characters (c_i, d_i) where:
  - `c_i` is the character to be replaced.
  - `d_i` is the character to replace `c_i` with.

### 2. How to Use

1. **Run the application:**
   Execute the `main.py` script in your terminal:
   ```bash
   python main.py
   ```

2. **Provide input:**
   - First, enter the values for N and Q separated by a space:
     ```
     5 2
     ```
   - Next, enter the string S:
     ```
     hello
     ```
   - Finally, enter the Q pairs of characters for replacement. For example:
     ```
     h y
     e a
     ```

3. **Output:**
   After entering the inputs, the application will print the modified string. For the above example, the output will be:
   ```
   yallo
   ```

## Example

Here’s a complete example of how to use the String Modifier:

```plaintext
Input:
5 2
hello
h y
e a

Output:
yallo
```

## Additional Information

For any questions or support regarding the String Modifier, please reach out to our support team.

We hope you enjoy using the String Modifier for your string manipulation needs!
```

This manual provides a comprehensive overview of the software, including installation instructions, usage guidelines, and examples to help users understand how to effectively use the String Modifier.