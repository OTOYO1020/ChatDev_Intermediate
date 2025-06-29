Here is the `manual.md` file for the occurrence finder software:

```markdown
# Occurrence Finder

A simple application to find the k-th occurrence of numbers in a sequence.

## Overview

The Occurrence Finder allows users to input a sequence of integers and a series of queries to determine the index of the k-th occurrence of specified numbers within that sequence. This tool is useful for tasks that require tracking occurrences of elements in a list, such as data analysis or debugging.

## Main Functions

- **Input Sequence**: Users can input a sequence of integers.
- **Input Queries**: Users can specify multiple queries to find the k-th occurrence of given integers.
- **Output Results**: The application returns the index of the k-th occurrence for each query or -1 if the occurrence does not exist.

## Installation

To run the Occurrence Finder, you need to have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

### Environment Dependencies

The application requires no additional dependencies beyond the standard Python library. However, ensure you have Python 3.x installed.

## How to Use

1. **Clone the Repository**: If you have the source code, clone it to your local machine.
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Run the Application**: Execute the main application file.
   ```bash
   python main.py
   ```

3. **Input Data**:
   - You will be prompted to enter the number of elements in the sequence (N).
   - Input the sequence of integers as space-separated values.
   - Enter the number of queries (Q).
   - For each query, input the integer (x) and the occurrence number (k) separated by a space.

4. **View Results**: After processing the queries, the application will display the results, showing the index of the k-th occurrence for each query or -1 if it does not exist.

### Example Usage

```
Enter the number of elements in the sequence: 5
Enter sequence (space-separated): 1 2 3 1 2
Enter the number of queries: 3
Enter query (x k): 1 1
Enter query (x k): 2 2
Enter query (x k): 3 2
Results: [0, 4, -1]
```

## Edge Cases

- If the sequence is empty (N = 0), the application will return -1 for each query.
- If a query requests an occurrence that exceeds the number of occurrences in the sequence, the application will return -1 for that query.

## Support

For any issues or questions, please reach out to our support team via the contact information provided in the repository.

Happy coding!
```

This user manual provides a comprehensive guide on how to use the Occurrence Finder software, including installation instructions, usage examples, and handling edge cases.