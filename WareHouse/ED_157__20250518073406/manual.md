Here is the `manual.md` file that provides a detailed user manual for the software developed to process queries on a string:

```markdown
# Query Processor

A Python application for processing string queries, allowing users to update characters in a string and count distinct characters in specified substrings.

## Main Functions

The Query Processor provides two main functionalities:

1. **Update Character**: Change the character at a specified index in the string if it differs from the current character.
2. **Count Distinct Characters**: Count the number of distinct characters in a substring defined by a range of indices.

## Quick Install

To run the Query Processor, ensure you have Python installed on your machine. You can install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

Make sure to create a `requirements.txt` file that includes the necessary libraries, such as:

```
# requirements.txt
re
```

## 🤔 What is this?

The Query Processor is designed to handle queries on a string efficiently. It allows users to perform updates and count distinct characters in a user-friendly manner. The application is structured to ensure that input validation is performed, providing a robust solution for string manipulation.

### Key Features:

- **Input Validation**: Ensures that the input string consists only of lowercase English letters.
- **Error Handling**: Provides user-friendly error messages for invalid queries or out-of-bounds indices.
- **Dynamic Updates**: The string can be updated in real-time based on user queries.

## 📖 How to Use

1. **Run the Application**: Execute the `main.py` file to start the application.

   ```bash
   python main.py
   ```

2. **Input String**: When prompted, enter a string consisting of lowercase letters.

   ```
   Enter a string consisting of lowercase letters: abcde
   ```

3. **Input Queries**: Enter the queries in the specified format. For example:
   - To update the character at index 1 to 'x': `1 1 x`
   - To count distinct characters from index 0 to 4: `2 0 4`
   - Separate multiple queries with a semicolon (`;`).

   ```
   Enter queries (e.g., '1 0 a' for update or '2 0 5' for distinct count, separated by ';'): 1 1 x; 2 0 4
   ```

4. **View Results**: The application will output the results of the distinct character queries.

   ```
   Results: [5]
   ```

## Example Queries

- **Update Query**: `1 2 z` (Changes the character at index 2 to 'z')
- **Distinct Count Query**: `2 0 3` (Counts distinct characters from index 0 to 3)

## Error Handling

The application will notify you of any errors encountered during query processing, such as:

- Invalid query format
- Out-of-bounds indices
- Empty input string

## Conclusion

The Query Processor is a powerful tool for string manipulation, providing an easy-to-use interface for updating characters and counting distinct characters. For any issues or feature requests, please contact the development team.
```

This manual provides a comprehensive overview of the software, including installation instructions, usage guidelines, and examples to help users effectively utilize the Query Processor.