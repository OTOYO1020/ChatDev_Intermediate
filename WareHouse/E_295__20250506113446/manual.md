```markdown
# Expected Value Calculator

A Python application designed to compute the expected value of a sequence of integers, with special handling for zeros. This software allows users to input a sequence and calculate the expected value based on specified rules.

## Main Functions

- **Input Handling**: Read integers N (length of the sequence) and K (position of the element to retrieve after sorting) from standard input, along with the sequence A of length N.
- **Expected Value Calculation**: Compute the expected value of the sequence, particularly focusing on elements that are zero.
- **Sorting and Retrieval**: Sort the modified sequence and retrieve the K-th element.
- **Modular Arithmetic**: Handle large integers and perform calculations under a modulus to ensure results fit within standard limits.

## Installation

To run the Expected Value Calculator, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. **Install Python**: Ensure you have Python 3.6 or higher. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: If you have the source code in a repository, clone it using:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

3. **Install Dependencies**: You may need to install any required dependencies. For this application, you can use:
   ```bash
   pip install -r requirements.txt
   ```
   (Note: If a `requirements.txt` file is not provided, ensure you have the necessary libraries installed, such as `numpy` if needed.)

## Usage

To use the Expected Value Calculator, follow these steps:

1. **Run the Application**: Execute the main application file:
   ```bash
   python main.py
   ```

2. **Input Data**: The application will prompt you for the following inputs:
   - **N**: Enter the length of the sequence.
   - **K**: Enter the position of the element you want to retrieve after sorting.
   - **A**: Enter the sequence of integers (space-separated).

   Example input:
   ```
   Enter N:
   5
   Enter K:
   3
   Enter sequence A (space-separated):
   0 2 0 4 5
   ```

3. **View Result**: After processing the input, the application will compute the expected value and print the result.

## Example

Here’s an example of how the application works:

- Input:
  ```
  Enter N:
  5
  Enter K:
  3
  Enter sequence A (space-separated):
  0 2 0 4 5
  ```

- Output:
  ```
  Result: <calculated_value>
  ```

## Important Notes

- Ensure that K is within the range of 1 to N. The application will return an error message if K is out of bounds.
- The application assumes that the maximum random integer M is set to 100. This can be adjusted in the `calculator.py` file if needed.
- All calculations are performed using modular arithmetic to handle large integers, specifically under the modulus 998244353.

## Support

For any issues or questions, please reach out to the development team or consult the documentation for further assistance.

```
