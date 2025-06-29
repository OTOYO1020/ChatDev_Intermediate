Here's a detailed user manual for the software that encapsulates the function `min_operations_to_contiguous_ones`. This manual provides an introduction to the main functions, installation instructions, and usage guidelines.

```markdown
# Contiguous Ones Calculator

The Contiguous Ones Calculator is a Python application designed to determine the minimum number of operations required to make all '1's in a binary string contiguous. This tool is useful for developers and data analysts who need to manipulate binary data efficiently.

## Main Functions

- **min_operations_to_contiguous_ones(S: str) -> int**: This function takes a binary string as input and calculates the minimum number of swaps needed to make all '1's contiguous. It handles edge cases, such as when the string contains only one '1' or none at all.

## Installation

To run the Contiguous Ones Calculator, you need to have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

### Step 1: Clone the Repository

Clone the repository containing the application files:

```bash
git clone <repository-url>
cd <repository-directory>
```

### Step 2: Install Dependencies

Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

Install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

### Step 3: Run the Application

You can run the application by executing the `main.py` file:

```bash
python main.py
```

When prompted, enter a binary string (composed of '0's and '1's) to calculate the minimum operations required to make all '1's contiguous.

## Usage Example

1. Start the application by running `python main.py`.
2. When prompted, enter a binary string, for example: `1001001`.
3. The application will output the minimum operations required, for example: `Minimum operations: 2`.

## Error Handling

The application includes basic error handling. If the input string contains characters other than '0' or '1', an error message will be displayed:

```
Error: Input string must only contain '0's and '1's.
```

## Additional Information

For testing purposes, you may want to include common libraries such as `pytest`. You can add it to your `requirements.txt` file:

```
pytest
```

## Conclusion

The Contiguous Ones Calculator is a simple yet powerful tool for manipulating binary strings. By following the installation and usage instructions, you can quickly determine the minimum number of operations needed to achieve contiguous '1's in any binary string.
```

This manual provides a comprehensive overview of the software, ensuring that users can easily understand how to install and use the application effectively.