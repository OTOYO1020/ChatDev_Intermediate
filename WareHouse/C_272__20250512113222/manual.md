Here's a detailed user manual for the Max Even Sum Calculator software, formatted in Markdown as requested:

```markdown
# Max Even Sum Calculator

A simple application to find the maximum even sum of pairs from a list of distinct non-negative integers.

## Overview

The Max Even Sum Calculator allows users to input a list of distinct non-negative integers and computes the maximum even sum that can be formed by any two distinct integers from the list. If no valid pairs exist, the application will return -1.

## Main Functions

- **Input Handling**: The application prompts the user to enter the number of integers and the integers themselves, ensuring they are distinct and non-negative.
- **Calculation**: The core function `find_max_even_sum` processes the list to find the maximum even sum of pairs.
- **Output**: The result is displayed to the user, either as the maximum even sum or -1 if no valid pairs exist.

## Installation

To run the Max Even Sum Calculator, ensure you have Python installed on your machine. You can install the required dependencies using pip. 

### Step 1: Install Python

If you haven't installed Python yet, download and install it from [python.org](https://www.python.org/downloads/).

### Step 2: Install Dependencies

Open your terminal or command prompt and run the following command:

```bash
pip install typing
```

## How to Use

### Step 1: Run the Application

To start the Max Even Sum Calculator, navigate to the directory where the `main.py` file is located and run:

```bash
python main.py
```

### Step 2: Input Data

1. **Enter the Number of Integers**: You will be prompted to enter the number of distinct non-negative integers. Ensure this number is at least 2.
   
   Example Input:
   ```
   Enter the number of distinct non-negative integers (must be at least 2): 5
   ```

2. **Enter the Integers**: Next, input exactly the number of integers you specified, separated by spaces. Ensure all integers are distinct and non-negative.

   Example Input:
   ```
   Enter exactly 5 distinct non-negative integers (space-separated): 1 2 3 4 5
   ```

### Step 3: View the Result

After entering the integers, the application will compute the maximum even sum of pairs and display the result.

Example Output:
```
Maximum even sum: 8
```

If no valid pairs exist, the output will be:
```
-1
```

## Edge Cases

- If you enter fewer than 2 integers, the application will prompt you to enter at least 2 distinct non-negative integers.
- If all integers are odd or all are even, the application will handle these cases and return -1 if no valid pairs can be formed.

## Conclusion

The Max Even Sum Calculator is a straightforward tool for calculating the maximum even sum from a list of distinct non-negative integers. By following the steps outlined in this manual, users can easily install and utilize the application to meet their needs.
```

This manual provides a comprehensive guide for users to understand the functionality, installation, and usage of the Max Even Sum Calculator software.