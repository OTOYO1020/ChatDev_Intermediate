Here's a detailed user manual for the software that finds the K-th smallest 321-like number. This manual includes an introduction to the main functions, installation instructions, and usage guidelines.

```markdown
# 321-Like Number Finder

A simple application to find the K-th smallest 321-like number, where a 321-like number is defined as a positive integer whose digits are strictly decreasing.

## Main Functions

- **is_321_like_number(x)**: This function checks if a given positive integer x is a 321-like number. It returns `True` if the digits of x are strictly decreasing, otherwise it returns `False`.

- **generate_321_like_numbers()**: This function generates all possible 321-like numbers by using a backtracking approach. It returns a sorted list of these numbers.

- **main()**: The main function that orchestrates the user input and output. It prompts the user to enter a positive integer K and retrieves the K-th smallest 321-like number from the generated list.

## Installation Instructions

To run the application, you need to have Python installed on your machine. Follow these steps to set up your environment:

1. **Install Python**: Download and install Python from [python.org](https://www.python.org/downloads/).

2. **Install Required Dependencies**: Open your terminal or command prompt and run the following command to install any necessary dependencies (if applicable). For this application, no additional libraries are required beyond Python itself.

   ```bash
   pip install --upgrade pip
   ```

3. **Clone the Repository**: If you have the code in a repository, clone it to your local machine. If you have the code in a file, ensure you have `main.py` ready to execute.

## How to Use the Application

1. **Run the Application**: Navigate to the directory where `main.py` is located and run the following command:

   ```bash
   python main.py
   ```

2. **Input Prompt**: The application will prompt you to enter a positive integer value for K:

   ```
   Please enter a positive integer value for K to find the K-th smallest 321-like number:
   ```

3. **Enter a Valid K**: Type a positive integer and press Enter. If the input is invalid (not a positive integer), the application will prompt you to try again.

4. **Output**: Once a valid K is entered, the application will display the K-th smallest 321-like number or inform you if there are not enough 321-like numbers available.

   ```
   The K-th smallest 321-like number is: [number]
   ```

## Example Usage

- If you enter `3`, the application will output:

   ```
   The 3-th smallest 321-like number is: 321
   ```

- If you enter a number larger than the available 321-like numbers, it will inform you:

   ```
   There are only [count] 321-like numbers available.
   ```

## Conclusion

This application provides a straightforward way to find 321-like numbers based on user input. Feel free to explore and modify the code to enhance its functionality or adapt it to your needs.
```

This manual provides a comprehensive overview of the software, ensuring users can easily understand how to install and use it effectively.