Here's a detailed user manual for the integer bag management system, formatted in Markdown as requested:

```markdown
# Integer Bag Management System

A simple application for managing a collection of integers, allowing users to add, remove, and count unique integers efficiently.

## Main Functions

The Integer Bag Management System provides the following functionalities:

1. **Add an Integer**: Add a specified integer to the bag.
2. **Remove an Integer**: Remove a specified integer from the bag. If the integer is not found, a warning will be issued.
3. **Count Unique Integers**: Retrieve the count of unique integers currently stored in the bag.

## Installation

To run the Integer Bag Management System, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. **Clone the Repository**: 
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**: 
   Create a `requirements.txt` file with the following content (if you plan to add any dependencies in the future):
   ```
   # Add any required packages here
   ```

   Then, install the dependencies using pip:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To use the Integer Bag Management System, follow these steps:

1. **Run the Application**:
   Execute the main application file:
   ```bash
   python main.py
   ```

2. **Input Queries**:
   You will be prompted to enter the number of queries you wish to perform. Enter an integer value.

   Then, for each query, input the query type and value in the following format:
   - For adding an integer: `1 x` (where `x` is the integer to add)
   - For removing an integer: `2 x` (where `x` is the integer to remove)
   - For counting unique integers: `3`

   Example input:
   ```
   Enter number of queries: 5
   Enter query (type and value): 1 5
   Enter query (type and value): 1 10
   Enter query (type and value): 2 5
   Enter query (type and value): 3
   Enter query (type and value): 3
   ```

3. **View Results**:
   After entering all queries, the application will display the results of type `3` queries, showing the count of unique integers in the bag.

## Error Handling

The application includes error handling for the following scenarios:
- Invalid query formats will trigger a warning and skip the query.
- Attempting to remove an integer that is not present in the bag will raise a warning.

## Example

Here’s an example of how the application works:

1. Input:
   ```
   Enter number of queries: 4
   Enter query (type and value): 1 1
   Enter query (type and value): 1 2
   Enter query (type and value): 2 1
   Enter query (type and value): 3
   ```

2. Output:
   ```
   Results of type 3 queries: [1]
   ```

This indicates that there is 1 unique integer left in the bag after the operations.

## Conclusion

The Integer Bag Management System is a straightforward tool for managing integers with basic operations. It is designed to be user-friendly and efficient, making it suitable for various applications where integer management is required.
```

This manual provides a comprehensive overview of the system, including installation instructions, usage guidelines, and examples to help users understand how to interact with the application effectively.