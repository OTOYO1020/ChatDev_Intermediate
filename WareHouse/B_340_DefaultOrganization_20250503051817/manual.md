Here's a detailed user manual for the query retrieval software, formatted in Markdown as requested:

```markdown
# Query Retrieval Software

A simple command-line application for managing and retrieving queries based on user input.

## Main Functions

The Query Retrieval Software allows users to perform the following operations:

1. **Add Queries**: Users can add integer values to a list by issuing a type 1 query.
2. **Retrieve Queries**: Users can retrieve the k-th value from the end of the list by issuing a type 2 query.
3. **Error Handling**: The application provides user-friendly error messages for invalid inputs and operations.

## Installation

To run the Query Retrieval Software, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. **Install Python**: Download and install Python from [python.org](https://www.python.org/downloads/).
2. **Clone the Repository**: Clone the repository containing the software files to your local machine.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

3. **Install Dependencies**: If there are any additional dependencies, you can install them using pip. For this software, no external libraries are required, as it only uses built-in Python functionalities.

   ```bash
   pip install -r requirements.txt  # If a requirements file is provided
   ```

## How to Use

1. **Run the Application**: Start the application by executing the `main.py` file.

   ```bash
   python main.py
   ```

2. **Input Queries**: The application will prompt you to enter the number of queries (Q). Enter a positive integer.

   ```
   Enter the number of queries: 3
   ```

3. **Enter Queries**: For each query, input the type followed by the associated value. The format is as follows:
   - For type 1 queries (to add a value): `1 x` (where `x` is an integer)
   - For type 2 queries (to retrieve a value): `2 k` (where `k` is the position from the end)

   Example:
   ```
   1 10
   1 20
   2 1
   ```

4. **View Results**: After entering all queries, the application will display results for all type 2 queries, each on a new line. If there are any errors during the input process, they will also be displayed.

   Example Output:
   ```
   20
   ```

## Error Handling

The application includes error handling for various scenarios:
- If the number of queries is not a positive integer, an error message will prompt the user to enter a valid integer.
- If a type 1 query does not provide a valid integer, an error message will indicate the issue.
- For type 2 queries, if the list is empty or if `k` exceeds the number of elements in the list, appropriate error messages will be shown.

## Conclusion

The Query Retrieval Software is a straightforward tool for managing and retrieving integer queries. It is designed to be user-friendly, with clear prompts and error messages to guide users through the process. For any further assistance or feature requests, please reach out to the development team.
```

This manual provides a comprehensive overview of the software, including its main functions, installation instructions, usage guidelines, and error handling mechanisms. Let me know if you need any further modifications or additional information!