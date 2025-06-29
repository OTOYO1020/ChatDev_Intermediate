Here's a detailed user manual for the software, formatted in Markdown as requested:

```markdown
# Integer Query Application

A Python application for querying the occurrences of integers in a sequence.

## Overview

The Integer Query Application allows users to input a sequence of integers and perform queries to find the indices of specific integers based on their occurrences. This application is designed to efficiently handle queries and provide results based on user input.

## Main Functions

1. **Input Handling**: The application reads integers N (length of the sequence) and Q (number of queries) from standard input.
2. **Sequence Storage**: It stores the sequence of integers and maintains a dictionary of occurrences, mapping each integer to its indices in the sequence.
3. **Query Processing**: For each query, it checks if the integer exists in the sequence and retrieves the index of its k-th occurrence.
4. **Output**: The results of the queries are printed to standard output.

## Installation

To run the Integer Query Application, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. **Install Python**: Make sure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: Clone the repository containing the application code.
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

3. **Install Dependencies**: The application does not require any external libraries beyond Python's standard library. Ensure you have Python installed correctly.

## Usage

To use the Integer Query Application, follow these steps:

1. **Run the Application**: Execute the main application file.
   ```bash
   python main.py
   ```

2. **Input N and Q**: When prompted, enter the values for N (length of the sequence) and Q (number of queries) separated by a space.
   ```
   Enter N and Q: 5 3
   ```

3. **Input the Sequence**: Enter the sequence of integers, ensuring the length matches N.
   ```
   Please enter the sequence of integers (length should be N):
   1 2 3 2 1
   ```

4. **Input Queries**: For each query, enter the integer x and the occurrence number k in the format `x k`.
   ```
   Enter query in the format 'x k' (where x is the integer to search for and k is the occurrence number): 2 1
   Enter query in the format 'x k' (where x is the integer to search for and k is the occurrence number): 1 2
   Enter query in the format 'x k' (where x is the integer to search for and k is the occurrence number): 3 1
   ```

5. **View Results**: The application will output the results for each query, indicating the index of the k-th occurrence or -1 if there are not enough occurrences.
   ```
   1
   4
   2
   ```

## Error Handling

The application includes basic error handling for user input. If the input is invalid (e.g., non-integer values, incorrect lengths), appropriate error messages will be displayed.

## Conclusion

The Integer Query Application is a simple yet powerful tool for querying integer occurrences in a sequence. It is designed for ease of use and efficiency, making it suitable for various applications where such functionality is required.

For any issues or feature requests, please contact the development team.
```

This manual provides a comprehensive overview of the application, including its functions, installation instructions, and usage guidelines. Let me know if you need any further modifications or additional information!