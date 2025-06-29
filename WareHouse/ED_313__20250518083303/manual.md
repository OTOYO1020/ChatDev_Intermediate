Here's the `manual.md` file that provides a detailed user manual for the string transformation software we developed:

```markdown
# String Transformation Tool

Transforming strings based on specified rules and counting operations.

## Overview

This software provides a function to transform a string of digits (from '1' to '9') into a new string according to specific transformation rules. It also counts the number of operations required to reduce the string to a length of 1 or detects if the transformation results in an infinite cycle.

## Main Functions

1. **f(S: str) -> str**: 
   - Transforms the input string `S` into a new string `T` based on the specified rules.
   - For each character in `S`, it repeats the character based on the integer value of the next character.
   - Raises a `ValueError` if the output exceeds the maximum allowed length of 10^6 characters.

2. **count_operations(S: str) -> int**: 
   - Counts the number of operations required to reduce the string `S` to length 1.
   - Detects cycles in the transformation process and returns -1 if a cycle is detected or if the output exceeds the limit.
   - Returns the number of operations modulo 998244353 if the length of `S` becomes 1.

## Installation

To run the software, you need to have Python installed on your machine. You can install the required dependencies using pip. 

### Step 1: Install Python

Make sure you have Python 3.6 or higher installed. You can download it from [python.org](https://www.python.org/downloads/).

### Step 2: Install Dependencies

Open your terminal or command prompt and run the following command:

```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt` file, you can simply run the software without any additional dependencies as it only uses built-in Python libraries.

## How to Use

1. **Run the Application**:
   - Navigate to the directory where the `main.py` file is located.
   - Run the following command in your terminal:

   ```bash
   python main.py
   ```

2. **Input String**:
   - When prompted, enter a string of digits (from '1' to '9') with a length between 2 and 10^6.

3. **Output**:
   - The program will output the number of operations required to reduce the string to length 1 or indicate if infinite operations are detected.

## Example

### Input:
```
Enter a string of digits (1-9): 312
```

### Output:
```
Number of operations: 2
```

## Validation

The input string must meet the following criteria:
- Contains only digits from '1' to '9'.
- Length must be between 2 and 10^6 characters.

If the input does not meet these criteria, the program will notify you of the invalid input.

## Conclusion

This tool is designed to help you transform strings based on specific rules and efficiently count the operations required for transformation. For any issues or feature requests, please contact our support team.

```

This manual provides a comprehensive guide for users to understand the software's functionality, installation steps, and usage instructions.