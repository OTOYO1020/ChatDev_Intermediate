Here is the `manual.md` file for the software that processes queries as per the customer's requirements:

```markdown
# Query Processor

A simple application for processing a series of integer queries efficiently.

## Overview

The Query Processor is designed to handle a sequence of queries that manipulate a list of integers. It supports three types of operations: appending integers, retrieving and removing the first integer, and sorting the list. This application is built to efficiently manage up to 200,000 queries.

## Main Functions

- **Append an Integer**: Add an integer to the end of the list.
- **Retrieve and Remove First Integer**: Print and remove the first integer from the list.
- **Sort the List**: Sort the list of integers in ascending order.

## Installation

To run the Query Processor, you need to have Python installed on your machine. You can install the required dependencies using pip. 

### Step 1: Install Python

Make sure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).

### Step 2: Install Dependencies

You can install any required dependencies using pip. Open your terminal or command prompt and run:

```bash
pip install typing
```

## Usage

### Running the Application

1. Clone the repository or download the files `main.py` and `query_processor.py`.
2. Open your terminal and navigate to the directory containing the files.
3. Run the application using Python:

```bash
python main.py
```

### Input Format

The application expects the following input format:

- The first line should contain an integer `Q`, the number of queries.
- The next `Q` lines should contain the queries in the following format:
  - `1 x` to append the integer `x` to the list.
  - `2` to print and remove the first integer from the list.
  - `3` to sort the list in ascending order.

### Example Input

```
5
1 10
1 20
2
3
2
```

### Example Output

```
10
20
```

### Error Handling

The application is designed to handle invalid operations gracefully. For example, if a type `2` query is issued when the list is empty, a `ValueError` will be raised.

## Conclusion

The Query Processor is a straightforward yet powerful tool for managing integer queries. With its efficient handling of operations, it is well-suited for applications requiring quick access and manipulation of data.

For any further questions or support, please reach out to our development team.
```

This manual provides a comprehensive guide for users to understand the functionality, installation process, and usage of the Query Processor application.