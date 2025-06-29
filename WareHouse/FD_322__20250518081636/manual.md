Here's a detailed user manual for the binary string application, formatted in Markdown:

```markdown
# Binary String Application

A simple application to process queries on binary strings consisting of '0's and '1's.

## Main Functions

The Binary String Application allows users to:
- Validate a binary string input.
- Process a list of queries that can either flip characters in a substring or calculate the maximum number of consecutive '1's in a substring.
- Handle edge cases, ensuring robust functionality.

### Key Features
- **Input Validation**: Ensures the binary string consists only of '0's and '1's.
- **Query Processing**: Supports two types of queries:
  - **Flip Characters**: Flips the characters in a specified substring.
  - **Max Consecutive Ones**: Calculates the maximum number of consecutive '1's in a specified substring.

## Installation

To run the Binary String Application, ensure you have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

### Environment Dependencies

This application does not require any external libraries beyond Python's standard library. Simply ensure you have Python 3.x installed.

## How to Use the Application

1. **Run the Application**:
   - Open your terminal or command prompt.
   - Navigate to the directory where `main.py` is located.
   - Execute the command:
     ```bash
     python main.py
     ```

2. **Input the Binary String**:
   - When prompted, enter a binary string that consists only of '0's and '1's. For example:
     ```
     Enter binary string (only 0s and 1s): 101010
     ```

3. **Input the Queries**:
   - Enter the queries in the format `c L R`, separated by semicolons. Here:
     - `c` is the query type (1 for flipping characters, 2 for calculating max consecutive '1's).
     - `L` is the starting index (1-based).
     - `R` is the ending index (1-based).
   - For example:
     ```
     Enter queries (format: c L R, separated by semicolons): 1 2 4; 2 1 6
     ```

4. **View Results**:
   - After processing the queries, the application will display the results for the queries of type `c=2`. For example:
     ```
     Results: [3]
     ```

## Example Usage

Here’s a complete example of how to use the application:

1. Start the application:
   ```
   python main.py
   ```

2. Input a valid binary string:
   ```
   Enter binary string (only 0s and 1s): 110011
   ```

3. Input queries:
   ```
   Enter queries (format: c L R, separated by semicolons): 1 1 3; 2 1 6
   ```

4. View the output:
   ```
   Results: [4]
   ```

## Error Handling

- If the binary string is empty or contains invalid characters, the application will display an error message.
- If the indices provided in the queries are invalid (out of range or incorrect), the application will raise a ValueError with a descriptive message.

## Conclusion

The Binary String Application is a straightforward tool for processing binary strings and performing specific queries. It is designed to be user-friendly and robust, ensuring that users can easily validate inputs and receive accurate results.

For any issues or further inquiries, please contact support.
```

This manual provides a comprehensive overview of the application, including its functionality, installation instructions, and usage guidelines.