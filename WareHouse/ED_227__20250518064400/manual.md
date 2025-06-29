Here's a detailed user manual for the software that implements the `count_swaps` function. This manual includes an introduction to the main functions of the software, installation instructions, and usage guidelines.

```markdown
# Count Swaps Application

This application provides a function to count the number of valid strings that can be formed from a given string with a specified number of adjacent swaps. It is designed to help users understand the permutations of characters in a string while considering the constraints of swaps.

## Main Functions

- **Input Handling**: The application reads a string `S` and an integer `K` from the user, ensuring that the string length is between 2 and 30 characters and that `K` is a non-negative integer not exceeding 10^9.
  
- **Character Counting**: The application counts the occurrences of the characters 'K', 'E', and 'Y' in the input string.

- **Unique Permutations Calculation**: It calculates the number of unique permutations of the string based on the character counts.

- **Adjacent Swaps Calculation**: The application determines the maximum number of adjacent swaps possible based on the character counts and the value of `K`.

- **Valid Strings Computation**: It computes the number of valid strings that can be formed with at most `K` swaps and returns this count.

## Installation Instructions

To run the application, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**:
   Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

   Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

   If you don't have a `requirements.txt` file yet, you can create one with the following content:
   ```
   # Add any required libraries here
   ```

## How to Use the Application

1. **Run the Application**:
   Execute the main application file:
   ```bash
   python main.py
   ```

2. **Input the Data**:
   - When prompted, enter a string `S` that is between 2 and 30 characters long.
   - Then, enter the maximum number of swaps `K`, which should be a non-negative integer not exceeding 10^9.

3. **View the Output**:
   The application will output the number of valid strings that can be formed based on your inputs.

## Example Usage

```
Enter String (2-30 characters): KEYKEY
Enter Maximum Swaps (0 to 10^9): 2
Number of valid strings: 30
```

## Error Handling

The application includes input validation. If the inputs do not meet the specified criteria, an error message will be displayed, prompting the user to enter valid inputs.

## Conclusion

This application is a powerful tool for understanding string permutations and the effects of adjacent swaps. It can be used in various applications, including combinatorial problems and string manipulation tasks. For any further assistance or feature requests, please reach out to our support team.

```

This manual provides a comprehensive overview of the application, ensuring that users can easily understand how to install and use it effectively.