Here's a detailed user manual for the software that implements the `check_equal_sets` function. This manual will guide users on how to install the necessary dependencies, understand the main functions of the software, and how to use it effectively.

```markdown
# Set Equality Checker

A simple application to check the equality of sets derived from two integer sequences based on user-defined queries.

## Quick Install

To get started with the Set Equality Checker, you need to install the required Python environment. You can do this using pip:

```bash
pip install -r requirements.txt
```

Make sure you have Python 3.x installed on your machine.

## 📖 Overview

The Set Equality Checker allows users to input two sequences of integers and a series of queries. For each query, the application extracts a specified number of elements from each sequence, converts them into sets to eliminate duplicates, and checks if the two sets are equal. The results are returned as a list of strings indicating 'Yes' or 'No' for each query.

### Main Functions

1. **Input Sequences**: The application prompts the user to input two integer sequences (A and B) in a comma-separated format.

2. **Input Queries**: Users can specify how many queries they want to run. Each query consists of two integers, indicating how many elements to extract from sequences A and B.

3. **Set Comparison**: For each query, the application extracts the specified number of elements, converts them into sets, and checks for equality.

4. **Output Results**: The results of the comparisons are printed as 'Yes' or 'No' for each query.

## 🛠️ How to Use

1. **Run the Application**: Execute the main application file `main.py` in your terminal or command prompt.

   ```bash
   python main.py
   ```

2. **Input Sequence A**: When prompted, enter the first sequence of integers (A) in a comma-separated format. For example:
   ```
   Enter sequence A (comma-separated integers): 1,2,3,4,5
   ```

3. **Input Sequence B**: Next, enter the second sequence of integers (B) in a similar format:
   ```
   Enter sequence B (comma-separated integers): 3,4,5,6,7
   ```

4. **Input Number of Queries**: Specify the number of queries you wish to perform:
   ```
   Enter number of queries: 2
   ```

5. **Input Queries**: For each query, enter the two integers (x_i, y_i) separated by a comma. For example:
   ```
   Enter query (x_i, y_i): 3,3
   Enter query (x_i, y_i): 4,5
   ```

6. **View Results**: After entering all queries, the application will display the results for each query:
   ```
   Yes
   No
   ```

## ⚠️ Error Handling

- The application includes error handling for invalid inputs. If you enter non-integer values or negative numbers, you will be prompted to re-enter the values correctly.

## 📄 Example

Here’s a quick example of how the application works:

- Input:
  ```
  Enter sequence A (comma-separated integers): 1,2,3,4,5
  Enter sequence B (comma-separated integers): 3,4,5,6,7
  Enter number of queries: 2
  Enter query (x_i, y_i): 3,3
  Enter query (x_i, y_i): 4,5
  ```

- Output:
  ```
  Yes
  No
  ```

## 📚 Additional Resources

For more information on Python programming and handling lists and sets, you can refer to the official Python documentation:

- [Python Lists](https://docs.python.org/3/tutorial/introduction.html#lists)
- [Python Sets](https://docs.python.org/3/library/stdtypes.html#set)

Feel free to reach out for any support or questions regarding the Set Equality Checker application.
```

This manual provides a comprehensive guide for users to understand and utilize the software effectively. Let me know if you need any further modifications or additional information!