Here's a detailed user manual for the software based on the provided code and requirements:

```markdown
# Minimum Distance Calculator

A Python application to calculate the minimum distance between indices in a permutation array that can form a consecutive integer sequence.

## Main Functions

The Minimum Distance Calculator provides the following key functionalities:

- **Input Handling**: Reads integers N (total number of elements) and K (length of the subsequence) from standard input.
- **Permutation Validation**: Ensures the input permutation array contains integers from 1 to N without duplicates.
- **Sliding Window Approach**: Iterates through possible starting indices to find valid subsequences.
- **Consecutive Sequence Check**: Determines if a subsequence can be rearranged to form a consecutive integer sequence.
- **Minimum Distance Calculation**: Returns the minimum distance between valid indices or indicates if no valid subsequence is found.

## Installation

To run the Minimum Distance Calculator, you need to have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Environment Dependencies

This application does not require any external libraries beyond the standard Python library. Ensure you have Python 3.x installed.

## How to Use

1. **Clone the Repository**: If you haven't already, clone the repository containing the code files.

    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Run the Application**: Execute the main application file `main.py` using Python.

    ```bash
    python main.py
    ```

3. **Input Data**: When prompted, enter the total number of elements (N) and the length of the subsequence (K) as space-separated integers. Then, enter the permutation array as space-separated integers.

    ```
    Enter the total number of elements (N) and the length of the subsequence (K): 5 3
    Enter the permutation array (space-separated integers from 1 to N): 3 1 2 5 4
    ```

4. **View Results**: The application will output the minimum distance or indicate if no valid consecutive subsequence was found.

    ```
    Minimum Distance: 2
    ```

## Error Handling

- If K is greater than N, the application will return an error message.
- If the permutation array does not contain integers from 1 to N without duplicates, an error message will be displayed.
- If no valid consecutive subsequence is found, the application will indicate this with a message.

## Example Usage

Here’s an example of how to use the Minimum Distance Calculator:

1. Start the application.
2. Input the values:

    ```
    Enter the total number of elements (N) and the length of the subsequence (K): 6 4
    Enter the permutation array (space-separated integers from 1 to N): 4 1 3 2 6 5
    ```

3. The output will show the minimum distance:

    ```
    Minimum Distance: 3
    ```

## Conclusion

The Minimum Distance Calculator is a straightforward tool for analyzing permutations and finding consecutive integer sequences. For any issues or questions, please refer to the code comments or reach out for support.

```

This manual provides a comprehensive overview of the software, including installation instructions, usage guidelines, and error handling, ensuring that users can effectively utilize the Minimum Distance Calculator.