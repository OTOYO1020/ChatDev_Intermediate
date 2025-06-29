Here's a detailed user manual for the sum calculation application, formatted in Markdown as requested:

```markdown
# Sum Calculation Application

A Python application for calculating the sum of the first K elements from subarrays of a given integer sequence.

## Main Functions

- **Input Handling**: Reads integers N, M, and K, and an integer sequence A of length N from standard input.
- **Subarray Extraction**: Loops through the sequence to extract subarrays of length M.
- **Sorting**: Sorts each subarray in ascending order.
- **Sum Calculation**: Calculates the sum of the first K elements in the sorted subarray using the utility function `sum_of_first_k`.
- **Output**: Prints the calculated sums for each valid subarray on a new line.

## Installation

To run the application, you need to have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Environment Dependencies

1. **Clone the Repository**: If you haven't already, clone the repository containing the application code.
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Required Packages**: Use pip to install any necessary dependencies. For this application, there are no external dependencies, but ensure you have Python 3.x installed.
   ```bash
   pip install -r requirements.txt
   ```

## How to Use the Application

1. **Run the Application**: Execute the main application file `main.py` from the command line.
   ```bash
   python main.py
   ```

2. **Input Format**: Provide the input in the following format:
   - First line: Three integers N, M, K separated by spaces.
   - Second line: N integers representing the sequence A.

   **Example Input**:
   ```
   5 3 2
   1 3 2 5 4
   ```

3. **Output**: The application will output the sums of the first K elements from each valid subarray on new lines.

   **Example Output**:
   ```
   3
   5
   7
   ```

## Example Usage

Here’s a complete example of how to run the application:

1. Open your terminal.
2. Navigate to the directory where `main.py` is located.
3. Run the application:
   ```bash
   python main.py
   ```
4. Input the following when prompted:
   ```
   5 3 2
   1 3 2 5 4
   ```
5. The output will be:
   ```
   3
   5
   7
   ```

## Additional Information

- The function `sum_of_first_k(sorted_subarray, K)` is defined in `utils.py` and is responsible for calculating the sum of the first K elements in a sorted subarray.
- If K exceeds the length of the subarray, the function will sum only the available elements.

For further assistance or to report issues, please contact the support team.

```

This manual provides a comprehensive overview of the application, including its main functions, installation instructions, usage guidelines, and example inputs and outputs.