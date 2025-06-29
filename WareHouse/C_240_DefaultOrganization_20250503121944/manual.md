Here's a detailed user manual for the Jump Reachability application, formatted in Markdown as requested:

```markdown
# Jump Reachability Application

A simple application to determine if a target coordinate can be reached using specified jumps.

## Main Functions

The Jump Reachability application provides the following main functionalities:

1. **Input Reading**: Reads integer values for the number of jumps (N) and the target coordinate (X) from standard input.
2. **Jump Pairs Storage**: Initializes an empty list to store pairs of jumps (a_i, b_i).
3. **Reachability Check**: Determines if the target coordinate X can be reached using the provided jump pairs through a breadth-first search algorithm.
4. **Output**: Prints "YES" if the target coordinate can be reached, otherwise prints "NO".

## Installation

To run the Jump Reachability application, you need to have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

### Environment Dependencies

The application requires no additional dependencies beyond the standard Python library. However, it is recommended to use Python 3.6 or higher.

## How to Use the Application

1. **Clone the Repository**: If you have the source code in a repository, clone it to your local machine.
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Run the Application**: You can run the application from the command line. Make sure to provide the required input in the specified format.
   ```bash
   python main.py
   ```

3. **Input Format**: The application expects input in the following format:
   - The first line should contain two integers, N (the number of jumps) and X (the target coordinate).
   - The next N lines should each contain two integers a_i and b_i, representing the jump pairs.

   **Example Input**:
   ```
   3 5
   1 2
   2 3
   3 4
   ```

4. **Output**: After providing the input, the application will output either "YES" or "NO" based on whether the target coordinate X can be reached.

## Example Usage

Here is an example of how to use the application:

1. Run the application:
   ```bash
   python main.py
   ```

2. Provide the input:
   ```
   3 5
   1 2
   2 3
   3 4
   ```

3. The output will be:
   ```
   YES
   ```

## Conclusion

The Jump Reachability application is a straightforward tool for checking the reachability of a target coordinate using specified jumps. It is designed to be user-friendly and efficient, leveraging Python's capabilities to handle input and perform calculations.

For any issues or further inquiries, please contact the development team.
```

This manual provides a comprehensive overview of the application, including its main functions, installation instructions, usage guidelines, and example input/output. Let me know if you need any further modifications or additional sections!