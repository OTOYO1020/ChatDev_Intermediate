Here's a detailed user manual for the subsequence calculator software, formatted in Markdown as requested:

```markdown
# Subsequence Calculator

A Python application for calculating the number of valid subsequences from a given sequence of integers.

## Quick Install

To run the Subsequence Calculator, you need to have Python installed on your system. You can install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

Make sure you have the following dependencies in your `requirements.txt`:

```
# requirements.txt
# Add any additional dependencies here
```

## 🤔 What is this?

The Subsequence Calculator is designed to read a sequence of integers and compute the number of valid subsequences that can be formed with those integers. The algorithm utilizes sorting and binary search to efficiently count valid subsequences.

### Main Functions

1. **calculate_subsequences(N, sequence)**: 
   - Takes an integer `N` (length of the sequence) and a list of integers `sequence`.
   - Returns the count of valid subsequences modulo `998244353`.

2. **binary_search(sorted_list, value)**:
   - Performs a binary search on a sorted list to find the count of elements that are less than or equal to a specified `value`.
   - Returns the count of such elements.

## 📖 How to Use

1. **Prepare Input**:
   - The program expects input from standard input (stdin). You need to provide:
     - An integer `N` representing the length of the sequence.
     - A sequence of `N` integers separated by spaces.

2. **Run the Application**:
   - You can run the application from the command line. Make sure you are in the directory where `main.py` is located.
   - Use the following command to execute the program:
   
   ```bash
   python main.py
   ```

3. **Example Input**:
   ```
   5
   3 1 2 3 4
   ```

4. **Expected Output**:
   - The program will output the count of valid subsequences based on the provided input.

## Example Usage

Here’s a complete example of how to use the Subsequence Calculator:

1. Create a text file named `input.txt` with the following content:
   ```
   5
   3 1 2 3 4
   ```

2. Run the program and redirect the input from the file:
   ```bash
   python main.py < input.txt
   ```

3. The output will display the count of valid subsequences.

## 📚 Additional Information

For more details on the implementation, you can refer to the source code in `main.py` and `utils.py`. The code is well-commented to help you understand the logic behind the calculations.

If you encounter any issues or have questions, feel free to reach out for support.
```

This manual provides a comprehensive overview of the software, including installation instructions, usage guidelines, and examples to help users effectively utilize the subsequence calculator.