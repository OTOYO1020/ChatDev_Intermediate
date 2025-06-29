Here's a detailed user manual for the software based on the provided code and requirements:

```markdown
# Sequence Determination Application

This application is designed to determine a sequence of integers based on user-defined parameters and queries. It utilizes a systematic approach to validate inputs, generate queries, and process responses to derive the final sequence.

## Main Functions of the Software

1. **Input Validation**: Ensures that the integers N and K meet the specified criteria (K is odd and 1 ≤ K < N ≤ 1000).
2. **Query Generation**: Randomly selects K distinct integers from the range 1 to N for querying.
3. **Response Processing**: Updates the sequence based on the parity of the sum of the queried integers.
4. **Conflict Resolution**: Handles conflicts in the sequence values using a simple overwrite strategy.
5. **Final Output**: Once the sequence is fully determined, it outputs the sequence in the specified format.

## Installation of Environment Dependencies

To run the application, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. **Install Python**: Ensure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **Install Required Libraries**: Open your terminal or command prompt and run the following command to install any necessary dependencies (if applicable):
   ```bash
   pip install random
   ```

   Note: The provided code does not require any external libraries beyond the standard Python library.

## How to Use the Application

1. **Run the Application**: Execute the main application file using Python. You can do this by navigating to the directory containing the `main.py` file and running:
   ```bash
   python main.py
   ```

2. **Input Parameters**: When prompted, enter two integers N and K separated by a space. Ensure that K is an odd number and that it satisfies the condition 1 ≤ K < N ≤ 1000.

   Example input:
   ```
   10 3
   ```

3. **Respond to Queries**: The application will generate queries in the format `? x_1 x_2 ... x_K`. You will need to provide a response indicating the parity of the sum of the selected integers:
   - Respond with `0` if the sum is even.
   - Respond with `1` if the sum is odd.
   - Respond with `-1` if the query was invalid (this will terminate the program).

4. **Completion**: Once the application has determined the sequence, it will output the final sequence in the format `! A_1 A_2 ... A_N` and terminate.

## Example Usage

1. Start the application:
   ```
   python main.py
   ```

2. Input the parameters:
   ```
   10 3
   ```

3. Respond to queries:
   ```
   ? 1 2 3
   1
   ```

4. Final output:
   ```
   ! 1 0 1 0 1 0 1 0 1 0
   ```

## Conclusion

This application provides a systematic approach to determining a sequence based on user-defined parameters and queries. Follow the instructions above to set up and use the software effectively. For any issues or further assistance, please refer to the documentation or contact support.
```

This manual provides a comprehensive overview of the software, including its main functions, installation instructions, and usage guidelines, ensuring that users can effectively utilize the application.