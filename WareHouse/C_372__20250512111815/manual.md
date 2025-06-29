Here’s a detailed user manual for the software based on the provided specifications. This manual will guide users on how to install the necessary dependencies, understand the main functions of the software, and how to use it effectively.

```markdown
# ABC Query Application

The ABC Query Application allows users to process a string and execute a series of queries to modify the string and count occurrences of the substring "ABC". This application is designed to be efficient and user-friendly.

## Main Functions

- **process_queries(S: str, queries: List[Tuple[int, str]]) -> List[int]**: This function takes an input string `S` and a list of queries. Each query specifies an index and a character to replace in the string. After each modification, it counts the occurrences of the substring "ABC" and returns a list of counts.

- **count_abc(S: str) -> int**: This helper function counts the occurrences of the substring "ABC" in the provided string `S`.

## Installation

To run the ABC Query Application, you need to have Python installed on your machine. You can install the required dependencies using the following steps:

1. **Clone the repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install dependencies**:
   Create a `requirements.txt` file with the following content (if not already provided):
   ```
   # No additional dependencies required for this application
   ```

   Then, install the dependencies using pip:
   ```bash
   pip install -r requirements.txt
   ```

## How to Use the Application

1. **Prepare Input**: The application expects input in the following format:
   - The first line should contain the input string `S`.
   - The second line should contain an integer `Q`, the number of queries.
   - The next `Q` lines should each contain a query in the format: `<index> <character>`, where `<index>` is the position in the string to modify (1-based index) and `<character>` is the character to insert.

2. **Run the Application**:
   You can run the application from the command line. Make sure you are in the directory where `main.py` is located. Use the following command:
   ```bash
   python main.py
   ```

3. **Example Input**:
   ```
   ABCD
   2
   2 X
   3 Y
   ```

   In this example:
   - The initial string is "ABCD".
   - There are 2 queries: 
     - Replace the character at index 2 with 'X' → "AXCD".
     - Replace the character at index 3 with 'Y' → "AXYD".

4. **Output**:
   After processing the queries, the application will output a list of integers representing the counts of "ABC" after each query. For the above example, the output would be:
   ```
   [1, 0]
   ```

## Conclusion

The ABC Query Application is a simple yet powerful tool for string manipulation and substring counting. By following the installation and usage instructions, you can easily integrate this functionality into your projects or use it as a standalone application.

For any issues or feature requests, please contact the support team.
```

This manual provides a comprehensive overview of the application, ensuring users can easily understand and utilize its features.