Here's a detailed user manual for the software, formatted in Markdown as requested:

```markdown
# Sequence Manager

A Python application for managing a sequence of integers through various queries.

## Overview

The Sequence Manager allows users to perform operations on a list of integers, including inserting elements and removing them while ensuring the list remains distinct and non-empty. This application is designed to handle user interactions through standard input and output.

## Main Functions

1. **Insert Element**: Insert a new element immediately after a specified existing element in the sequence.
2. **Remove Element**: Remove a specified element from the sequence.
3. **Maintain Sequence Integrity**: Ensure that the sequence remains non-empty and contains distinct elements after each operation.

## Installation

To set up the environment and install the required dependencies, follow these steps:

1. **Clone the Repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**:
   Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

   Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To use the Sequence Manager application, follow these steps:

1. **Run the Application**:
   Execute the main script:
   ```bash
   python main.py
   ```

2. **Input Format**:
   - First, input the length of the sequence `N` and the number of queries `Q`:
     ```
     N Q
     ```
   - Next, input the sequence of integers of length `N`:
     ```
     A1 A2 A3 ... AN
     ```
   - Then, input `Q` queries in the following format:
     - For inserting an element:
       ```
       1 x y
       ```
       Where `x` is the existing element in the sequence and `y` is the new element to be inserted.
     - For removing an element:
       ```
       2 x
       ```
       Where `x` is the element to be removed.

3. **Example Input**:
   ```
   5 3
   1 2 3 4 5
   1 3 6
   2 2
   ```

4. **Output**:
   The application will print the final state of the sequence after processing all queries. If any errors occur (e.g., trying to insert a duplicate or remove an element that doesn't exist), appropriate warnings will be displayed.

## Error Handling

- If an attempt is made to insert an element that already exists in the sequence, a warning will be printed, and the insertion will be skipped.
- If an attempt is made to remove an element that does not exist, a warning will be printed.
- The application ensures that the sequence remains non-empty and distinct after each operation. If an operation would violate this rule, it will be reverted, and a warning will be displayed.

## Future Scalability

This application is designed with scalability in mind. Future enhancements could include:
- Support for additional query types.
- Enhanced error handling and logging mechanisms.
- A graphical user interface (GUI) for easier interaction.

## Support

For any issues or feature requests, please contact the support team or refer to the documentation for further assistance.
```

This manual provides a comprehensive guide for users to understand how to install, use, and troubleshoot the Sequence Manager application.