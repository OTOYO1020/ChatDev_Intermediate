Here's a detailed user manual for the software that implements the functionality to find the K-th smallest 321-like number. This manual includes an introduction to the main functions, installation instructions, and usage guidelines.

```markdown
# 321-like Number Finder

A Python application to find the K-th smallest 321-like number using combinations of digits from 1 to 9 in strictly decreasing order.

## Main Functions

1. **find_kth_321_like_number(K: int) -> int**
   - This function generates all possible 321-like numbers and returns the K-th smallest one.
   - It checks for valid input and raises an error if K is out of bounds.

2. **is_321_like_number(x: int) -> bool**
   - This helper function checks if a given number x is a 321-like number (strictly decreasing).

3. **GUI Implementation**
   - A graphical user interface (GUI) is provided using Tkinter, allowing users to input K and receive results in a user-friendly manner.

## Installation

To run the application, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. **Install Python**
   - Download and install Python from [python.org](https://www.python.org/downloads/).

2. **Set Up a Virtual Environment (Optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Required Dependencies**
   - The application uses the `itertools` library, which is included in the Python standard library, so no additional installation is required for it.
   - If you plan to use the GUI, ensure you have Tkinter installed (it usually comes with Python installations).

## Usage

### Running the Application from Command Line

1. Open your terminal or command prompt.
2. Navigate to the directory where the `main.py` file is located.
3. Run the application:
   ```bash
   python main.py
   ```
4. Enter a positive integer K when prompted. The application will output the K-th smallest 321-like number.

### Using the GUI

1. Open your terminal or command prompt.
2. Navigate to the directory where the `gui.py` file is located.
3. Run the GUI application:
   ```bash
   python gui.py
   ```
4. A window will appear. Enter a positive integer K in the input field and click the "Find K-th 321-like Number" button.
5. The result will be displayed in a message box.

## Error Handling

- If you enter a non-integer or a negative integer for K, the application will display an error message indicating the issue.
- Ensure that K is a positive integer to receive valid results.

## Testing

To ensure the correctness of the function, you can test it with various values of K. The application is designed to handle valid inputs as per the problem constraints.

## Conclusion

This application provides a straightforward way to find K-th smallest 321-like numbers using Python. Whether you prefer command-line interaction or a graphical interface, the 321-like Number Finder has you covered. Enjoy exploring the fascinating world of 321-like numbers!
```

This manual provides comprehensive guidance for users to understand, install, and effectively use the software. Let me know if you need any modifications or additional information!