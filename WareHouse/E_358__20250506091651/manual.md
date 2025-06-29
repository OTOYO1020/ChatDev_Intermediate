Here's the `manual.md` file for the software developed to solve the customer's task:

```markdown
# Valid String Calculator

Calculate the total number of valid strings based on specified constraints for uppercase English letters.

## Introduction

The Valid String Calculator is a Python application designed to compute the total number of valid strings that can be formed using uppercase English letters (A-Z) under specific constraints. Users can define the maximum length of the strings and the maximum occurrences allowed for each letter.

## Main Functions

- **Input Handling**: The application reads the maximum string length (K) and an array of occurrences (C) for each letter.
- **String Calculation**: It calculates the total number of valid strings that can be formed based on the provided constraints.
- **Output**: Displays the total count of valid strings.

## Installation

To run the Valid String Calculator, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. **Install Python**: Make sure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: If you haven't already, clone the repository containing the code.
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

3. **Install Dependencies**: The application does not require any external libraries, but ensure you have Python installed.

## Usage

To use the Valid String Calculator, follow these steps:

1. **Run the Application**: Open your terminal or command prompt, navigate to the directory where the code is located, and run the following command:
   ```bash
   python main.py
   ```

2. **Input the Maximum Length (K)**: When prompted, enter the maximum length of the strings you want to calculate.

   ```
   Enter maximum length (K): 
   ```

3. **Input the Occurrences (C)**: Enter 26 space-separated integers representing the maximum occurrences allowed for each letter from A to Z.

   ```
   Enter occurrences (26 space-separated integers): 
   ```

   Example input:
   ```
   3
   1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
   ```

4. **View the Result**: After entering the inputs, the application will calculate and display the total number of valid strings.

   ```
   Total valid strings: <calculated_value>
   ```

## Example

Here’s an example of how to use the application:

1. Run the application:
   ```bash
   python main.py
   ```

2. Input:
   ```
   Enter maximum length (K): 3
   Enter occurrences (26 space-separated integers): 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
   ```

3. Output:
   ```
   Total valid strings: 17576
   ```

## Conclusion

The Valid String Calculator is a powerful tool for calculating valid strings based on user-defined constraints. By following the installation and usage instructions, users can easily compute the total number of valid strings for any given set of parameters.
```

This manual provides a comprehensive overview of the software, including its purpose, installation instructions, usage guidelines, and an example to help users understand how to interact with the application effectively.