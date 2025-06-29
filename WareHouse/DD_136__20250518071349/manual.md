Here's a detailed user manual for the `count_children` software, formatted in Markdown as requested:

```markdown
# Count Children

A simple application to count the number of children on squares based on movements defined by a string of 'L' and 'R'.

## Quick Install

To run the application, ensure you have Python installed on your machine. You can install the required dependencies using pip:

```bash
pip install typing
```

## 🤔 What is this?

The `count_children` application allows users to input a string consisting of the characters 'L' and 'R'. The application simulates the movement of children on a series of squares based on the input string. Each 'R' moves a child to the right, and each 'L' moves a child to the left. The application ensures that children do not move out of bounds.

## Main Functions

1. **Input Validation**: The application validates the input string to ensure it:
   - Starts with 'R'
   - Ends with 'L'
   - Has a length between 2 and 100,000 characters.

2. **Counting Children**: The application initializes a list representing the number of children on each square and updates this list based on the movements defined in the input string.

3. **Output**: The final output is a list of integers, where each integer represents the number of children standing on each square after all movements have been processed.

## How to Use

1. **Run the Application**: Execute the `main.py` file in your terminal or command prompt.

   ```bash
   python main.py
   ```

2. **Input the String**: When prompted, enter a string that starts with 'R' and ends with 'L'. For example:

   ```
   Enter the string (starts with 'R' and ends with 'L'): RLRLLR
   ```

3. **View the Result**: After entering a valid string, the application will process the movements and display the final count of children on each square.

   ```
   Children count: [2, 3, 2, 1, 1, 1]
   ```

## Example Test Cases

Here are some example inputs and expected outputs to help you understand how the application works:

- **Input**: `RLLL`
  - **Output**: `[1, 2, 2, 1]`
  
- **Input**: `RRRLL`
  - **Output**: `[1, 2, 3, 2, 1]`
  
- **Input**: `RLRLRLRL`
  - **Output**: `[2, 3, 2, 3, 2, 1, 1, 1]`

## 📖 Documentation

For more detailed information on the code structure and functions, refer to the source files:

- **`main.py`**: The main application file that handles user input and output.
- **`utils.py`**: Contains utility functions for input validation and counting children.

Feel free to modify the code as needed to fit your specific requirements or to add additional features!
```

This manual provides a comprehensive overview of the `count_children` software, including installation instructions, usage guidelines, and examples to help users understand how to interact with the application effectively.