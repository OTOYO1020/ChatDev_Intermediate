Here's a detailed user manual for the Max Product Calculator software, formatted in Markdown:

```markdown
# Max Product Calculator

A Python application designed to calculate the maximum product of a subset of integers from an array, with special handling for negative numbers.

## Main Functions

The Max Product Calculator performs the following key functions:

- **Input Handling**: Reads integers N (number of elements) and K (number of elements to consider for product calculation) from standard input.
- **Sorting**: Sorts the input array in descending order to prioritize larger values for product calculation.
- **Product Calculation**: Computes the maximum product of the first K elements, considering special cases for negative numbers.
- **Modulo Operation**: Ensures the final product fits within the constraints by applying a modulo operation with \(10^9 + 7\).
- **Output**: Prints the final value of the maximum product.

## Installation

To run the Max Product Calculator, ensure you have Python installed on your system. You can install the required dependencies using pip. 

### Step 1: Install Python

If you haven't installed Python yet, download it from [python.org](https://www.python.org/downloads/) and follow the installation instructions for your operating system.

### Step 2: Install Dependencies

Open your terminal or command prompt and run the following command to install any necessary dependencies:

```bash
pip install -r requirements.txt
```

*Note: As of now, there are no external dependencies required other than Python itself.*

## How to Use

### Step 1: Prepare Your Input

You will need to provide two integers, N and K, followed by an array of N integers. For example:

```
Enter N and K (space-separated): 5 3
Enter array elements (space-separated): 1 -2 -3 4 5
```

### Step 2: Run the Application

To run the Max Product Calculator, execute the `main.py` file. You can do this by navigating to the directory containing the file in your terminal and running:

```bash
python main.py
```

### Step 3: View the Output

After entering the required input, the application will calculate and display the maximum product based on the provided integers.

### Example

Here’s an example of how the input and output will look:

```
Enter N and K (space-separated): 5 3
Enter array elements (space-separated): 1 -2 -3 4 5
Max Product: 20
```

## Additional Notes

- Ensure that the number of elements in the array matches the value of N you provide; otherwise, a ValueError will be raised.
- The application handles cases where K is greater than the number of elements in the array by raising an appropriate error.
- The product calculation takes into account the presence of negative numbers and adjusts accordingly to maximize the product.

## Support

For any issues or questions regarding the Max Product Calculator, please reach out to our support team at support@chatdev.com.

```

This manual provides a comprehensive overview of the Max Product Calculator, including its main functions, installation instructions, usage guidelines, and support information.