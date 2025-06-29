Here's a detailed user manual for the software that implements the functionality to check if a number is a multiple of 3 and to determine the minimum digits to erase from a number to form a multiple of 3.

```markdown
# Multiple of 3 Checker

A Python application that checks if a number is a multiple of 3 and calculates the minimum number of digits to erase from a given positive integer to form a multiple of 3.

## Quick Install

To run this application, you need to have Python installed on your machine. You can install the required dependencies using pip:

```bash
pip install itertools
```

## 🤔 What is this?

This application consists of two main functions:

1. **is_multiple_of_3(num: str) -> bool**: 
   - This function checks if the given number, represented as a string, is a multiple of 3. It does this by calculating the sum of its digits and checking if the sum is divisible by 3.

2. **min_digits_to_erase(N: int) -> Tuple[bool, int]**: 
   - This function takes a positive integer N and returns a tuple containing:
     - A boolean indicating if a multiple of 3 can be formed from the digits of N.
     - The minimum number of digits that need to be erased to form a multiple of 3.

## 🛠️ How to Use

1. **Run the Application**:
   - Execute the `main.py` file in your terminal or command prompt. You can do this by navigating to the directory where the file is located and running:
     ```bash
     python main.py
     ```

2. **Input a Positive Integer**:
   - When prompted, enter a positive integer. The application will process the input and determine if a multiple of 3 can be formed from its digits.

3. **View the Output**:
   - The application will output the result in the following format:
     ```
     Possible: True/False, Minimum digits erased: X
     ```
   - Here, `True/False` indicates whether a multiple of 3 can be formed, and `X` indicates the minimum number of digits that need to be erased. If no valid combination can be formed, it will display `-1`.

## 📖 Example Usage

- **Example 1**:
  - Input: `123`
  - Output: `Possible: True, Minimum digits erased: 0`
  
- **Example 2**:
  - Input: `14`
  - Output: `Possible: True, Minimum digits erased: 1`
  
- **Example 3**:
  - Input: `7`
  - Output: `Possible: False, Minimum digits erased: -1`

## 📜 Notes

- Ensure that the input is a positive integer. The application will raise an error if the input is invalid.
- The application uses combinations from the `itertools` library to generate possible digit combinations efficiently.

## 📄 License

This software is provided as-is without any warranty. Feel free to use and modify it as per your needs.

```

This manual provides a comprehensive overview of the software, including installation instructions, usage guidelines, and examples to help users understand how to interact with the application effectively.