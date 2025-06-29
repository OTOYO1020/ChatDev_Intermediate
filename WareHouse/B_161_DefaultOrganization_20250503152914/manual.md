Here's a detailed user manual for the voting calculation software, formatted in Markdown as requested:

```markdown
# Voting Calculation Software

This software is designed to process voting data and determine if a certain number of items meet a specified threshold based on their votes. It reads input values, calculates totals, and outputs whether the selection criteria are met.

## Main Functions

1. **Input Handling**: The software reads integers N (number of items) and M (minimum required items to be selected) from standard input.
2. **Vote Processing**: It reads an array of votes and calculates the total number of votes.
3. **Threshold Calculation**: It computes a threshold value to determine which items qualify based on their votes.
4. **Selection Criteria**: It counts how many items meet or exceed the threshold and checks if this count is at least M.
5. **Output**: The software outputs "Yes" if the selection criteria are met, otherwise "No".

## Installation

To run the software, ensure you have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

### Environment Dependencies

This software does not require any external libraries beyond the standard Python library. However, ensure you have Python 3.x installed.

## How to Use

1. **Run the Software**: You can run the software from the command line or terminal by executing the following command:
   ```bash
   python main.py
   ```

2. **Input Format**: The software expects input in the following format:
   - The first line should contain two integers, N and M, separated by a space.
   - The second line should contain N integers representing the votes, separated by spaces.

   **Example Input**:
   ```
   5 3
   10 20 30 40 50
   ```

3. **Output**: After providing the input, the software will process the data and output either "Yes" or "No" based on the selection criteria.

   **Example Output**:
   ```
   Yes
   ```

## Example Usage

Here’s how you can use the software in practice:

1. Open your terminal or command prompt.
2. Navigate to the directory where `main.py` is located.
3. Run the command:
   ```bash
   python main.py
   ```
4. Input the required values when prompted.

   ```
   4 2
   15 25 35 45
   ```

5. The software will output:
   ```
   Yes
   ```

## Conclusion

This voting calculation software provides a straightforward way to assess voting data against specified criteria. By following the installation and usage instructions, users can easily determine if the required number of items meets the selection threshold.
```

This manual provides a comprehensive overview of the software's functionality, installation steps, and usage instructions, ensuring that users can effectively utilize the voting calculation tool.