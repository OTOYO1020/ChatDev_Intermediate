Here's a detailed user manual for the Tree Distance Calculator software, formatted in Markdown as requested:

```markdown
# Tree Distance Calculator

A Python application for calculating the number of vertices at a specified distance from a given vertex in a binary tree structure.

## Main Functions

The Tree Distance Calculator provides the following main functionalities:

- **Input Parsing**: Reads the number of test cases and the values of N, X, and K for each test case.
- **Distance Calculation**: Implements the `find_distance_count(N, X, K)` function to calculate the number of vertices at distance K from vertex X.
- **Output**: Displays the results for all test cases in the required output format.

## Installation

To run the Tree Distance Calculator, you need to have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

### Environment Dependencies

1. **Python**: Ensure you have Python 3.x installed.
2. **No additional libraries** are required for this application, as it uses built-in Python functionalities.

## How to Use

1. **Clone the Repository**: If you haven't already, clone the repository containing the application files.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Run the Application**: Execute the main application file `main.py`.

   ```bash
   python main.py
   ```

3. **Input Format**: When prompted, enter the number of test cases followed by the values of N, X, and K for each test case. For example:

   ```
   Enter number of test cases: 2
   Enter N, X, K: 7 3 1
   Enter N, X, K: 10 5 2
   ```

4. **Output**: The application will print the results for each test case, indicating the number of vertices at distance K from vertex X.

   ```
   2
   3
   ```

## Example Usage

Here’s an example of how to use the Tree Distance Calculator:

1. Start the application.
2. Input the number of test cases.
3. For each test case, input the values of N (total vertices), X (starting vertex), and K (distance).

### Sample Input

```
Enter number of test cases: 1
Enter N, X, K: 15 8 2
```

### Sample Output

```
3
```

This output indicates that there are 3 vertices at a distance of 2 from vertex 8 in a tree with 15 vertices.

## Conclusion

The Tree Distance Calculator is a straightforward tool for calculating distances in a binary tree structure without the need to construct the entire tree. It efficiently handles large values of N (up to 10^18) and provides quick results for multiple test cases.

For any issues or feature requests, please contact the development team.
```

This manual provides a comprehensive overview of the software, including its main functions, installation instructions, usage guidelines, and examples to help users effectively utilize the Tree Distance Calculator.