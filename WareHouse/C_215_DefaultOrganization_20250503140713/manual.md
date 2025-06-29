Here's a detailed user manual for the software that generates permutations of a string, formatted in Markdown:

```markdown
# Permutation Generator

A simple application to generate distinct permutations of a given string and retrieve the K-th smallest permutation.

## Quick Install

To run the application, ensure you have Python installed on your system. You can install the required dependencies using pip:

```bash
pip install itertools
```

## 🤔 What is this?

The Permutation Generator application allows users to input a string and an integer K, and it will generate all distinct permutations of the string. The application ensures that the permutations are unique and sorted in lexicographical order. Users can then retrieve the K-th smallest permutation based on their input.

## 📖 Main Functions

### 1. Input Validation
- The application reads a string `S` and an integer `K` from standard input.
- It validates that the length of `S` is between 1 and 8 characters.
- It checks that `K` is a valid positive integer.

### 2. Generate Permutations
- The application uses the `generate_permutations(S)` function to create all distinct permutations of the string `S`.
- It utilizes a set to ensure uniqueness and sorts the permutations in lexicographical order.

### 3. Retrieve K-th Permutation
- The application accesses the `K-1` index of the sorted list of permutations to retrieve the K-th smallest permutation.
- If `K` exceeds the number of generated permutations, an appropriate message is displayed.

## 🛠️ How to Use

1. **Run the Application**
   - Save the provided code in two files: `main.py` and `permutation_generator.py`.

2. **Input Format**
   - The application expects input in the following format:
     ```
     <string S>
     <integer K>
     ```
   - For example:
     ```
     abc
     2
     ```

3. **Execution**
   - Run the application from the command line:
     ```bash
     python main.py
     ```
   - Provide the input string and integer when prompted.

4. **Output**
   - The application will print the K-th permutation of the string `S` or an error message if the input is invalid.

## 🚀 Example Usage

### Input
```
abc
2
```

### Output
```
K-th Permutation: acb
```

## 📄 Error Handling
- If the string length is not between 1 and 8 characters, the application will output:
  ```
  String length must be between 1 and 8 characters.
  ```
- If `K` is not a valid positive integer, the output will be:
  ```
  Please enter a valid positive integer for K.
  ```
- If `K` exceeds the number of permutations, the output will be:
  ```
  K is out of range for the number of permutations.
  ```

## 💡 Conclusion
This application provides a straightforward way to generate and retrieve permutations of a string. It is designed to be user-friendly with clear input requirements and error handling to guide users through the process.
```

This manual provides a comprehensive overview of the application's functionality, installation instructions, usage guidelines, and error handling, ensuring users can effectively utilize the software.