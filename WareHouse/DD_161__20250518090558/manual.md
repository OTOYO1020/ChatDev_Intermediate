Here's a detailed user manual for the Lunlun Number Finder application, formatted in Markdown as requested:

```markdown
# Lunlun Number Finder

A simple application to find the K-th lunlun number based on user input. Lunlun numbers are defined by the property that the absolute difference between each pair of adjacent digits is at most 1.

## Main Functions

1. **is_lunlun_number(num: int) -> bool**: 
   - Checks if a given integer is a lunlun number by evaluating the absolute difference between each pair of adjacent digits.

2. **generate_lunlun_numbers(limit: int) -> List[int]**: 
   - Generates lunlun numbers up to a specified limit using a breadth-first search approach starting from single-digit numbers.

3. **find_kth_lunlun_number(K: int) -> int**: 
   - Utilizes the `generate_lunlun_numbers` function to find the K-th smallest lunlun number.

4. **main()**: 
   - Handles user input and displays the K-th lunlun number based on the user's request.

## Installation

To run the Lunlun Number Finder application, you need to have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

### Environment Dependencies

You may need to install the following dependencies:

- **tkinter**: This is usually included with Python installations. If you encounter issues, please refer to your operating system's documentation on how to install tkinter.

To install any additional required packages, you can use pip:

```bash
pip install -U pip
```

## How to Use the Application

### Command Line Interface

1. **Run the Application**:
   - Open your terminal or command prompt.
   - Navigate to the directory where the `main.py` file is located.
   - Run the following command:
     ```bash
     python main.py
     ```

2. **Input**:
   - When prompted, enter an integer value for K (1 ≤ K ≤ 100000).
   - The application will calculate and display the K-th lunlun number.

### Graphical User Interface

1. **Run the GUI Application**:
   - Open your terminal or command prompt.
   - Navigate to the directory where the `gui.py` file is located.
   - Run the following command:
     ```bash
     python gui.py
     ```

2. **Input**:
   - Enter an integer value for K (1 ≤ K ≤ 100000) in the provided text box.
   - Click the "Find K-th Lunlun Number" button.
   - The result will be displayed below the button.

## Testing the Implementation

You can test the implementation by entering various values of K within the specified range to ensure correctness and performance. The application is designed to handle values up to 100,000 efficiently.

## Conclusion

The Lunlun Number Finder is a straightforward application that allows users to explore lunlun numbers easily. Whether you prefer using the command line or a graphical interface, the application provides a user-friendly experience for finding lunlun numbers.

For any issues or feature requests, please contact the development team at ChatDev.
```

This manual provides a comprehensive overview of the Lunlun Number Finder application, including its main functions, installation instructions, usage guidelines, and testing recommendations.