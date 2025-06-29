Here's a detailed user manual for the software based on the provided specifications:

```markdown
# Bag Management Application

Manage a collection of integers efficiently through a series of queries.

## Overview

The Bag Management Application allows users to perform operations on a collection of integers, including adding, removing, and counting unique integers. This application is designed to handle a large number of queries efficiently, making it suitable for scenarios where performance is critical.

## Main Functions

1. **Add an Integer**: Add an integer to the bag. If the integer already exists, its count is incremented.
2. **Remove an Integer**: Remove an integer from the bag. If the integer's count reaches zero, it is removed from the bag entirely.
3. **Count Unique Integers**: Retrieve the count of unique integers currently in the bag.

## Installation

To run the Bag Management Application, you need to have Python installed on your system. Follow these steps to set up the environment:

1. **Install Python**: Ensure you have Python 3.6 or higher installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: Clone the repository containing the application files.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

3. **Install Dependencies**: The application does not require any external dependencies beyond Python itself. You can run the application directly after cloning.

## Usage

To use the Bag Management Application, follow these steps:

1. **Run the Application**: Execute the main application file.

   ```bash
   python main.py
   ```

2. **Input Queries**: The application will prompt you to enter the number of queries (Q) followed by the queries themselves. Each query should follow the format specified below:

   - **Add an Integer**: `1 x` (where `x` is the integer to add)
   - **Remove an Integer**: `2 x` (where `x` is the integer to remove)
   - **Count Unique Integers**: `3` (this will output the count of unique integers)

### Example Usage

```plaintext
5
1 10
1 20
1 10
3
2 10
3
```

**Output**:
```plaintext
2
1
```

### Query Breakdown

- The first query `1 10` adds the integer 10 to the bag.
- The second query `1 20` adds the integer 20 to the bag.
- The third query `1 10` increments the count of integer 10.
- The fourth query `3` counts the unique integers (10 and 20), resulting in `2`.
- The fifth query `2 10` removes one instance of integer 10.
- The sixth query `3` counts the unique integers again, resulting in `1` (only 20 remains).

## Error Handling

- If you attempt to remove an integer that does not exist in the bag, a `KeyError` will be raised, and an error message will be displayed.
- Invalid query types will prompt an error message indicating the valid types (1, 2, or 3).
- Invalid inputs will also prompt an error message for clarification.

## Conclusion

The Bag Management Application is a powerful tool for managing collections of integers efficiently. With its simple command structure and robust error handling, users can easily manipulate their data and retrieve insights on unique integers in real-time.
```

This manual provides a comprehensive guide for users to understand the functionality, installation process, and usage of the Bag Management Application.