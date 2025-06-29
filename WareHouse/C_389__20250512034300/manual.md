Here is the `manual.md` file for the software, detailing its main functions, installation instructions, and usage guidelines:

```markdown
# Snake Queue Processor

A Python application for processing queries related to a queue of snakes, allowing users to manage snake lengths and head positions through various commands.

## Main Functions

The software provides the following functionalities:

1. **Add a Snake**: Add a new snake to the queue with a specified length.
   - Query Type: `1 l` (where `l` is the length of the snake)
  
2. **Remove a Snake**: Remove the first snake from the queue and adjust the head positions of the remaining snakes.
   - Query Type: `2`
  
3. **Get Head Position**: Retrieve the head position of the `k`-th snake in the queue.
   - Query Type: `3 k` (where `k` is the 1-based index of the snake)

## Installation

To run the application, you need to have Python installed on your system. Follow these steps to set up the environment:

1. **Install Python**: Make sure you have Python 3.6 or higher installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **Install Dependencies**: Open your terminal or command prompt and run the following command to install the required dependencies:
   ```bash
   pip install typing
   ```

## How to Use

1. **Run the Application**: Navigate to the directory containing the `main.py` file and execute the following command:
   ```bash
   python main.py
   ```

2. **Input Queries**: The application will prompt you to enter the number of queries. Input a positive integer representing the number of queries you want to process.

3. **Enter Each Query**: For each query, input the query type followed by the necessary parameters. For example:
   - To add a snake of length 5: `1 5`
   - To remove the first snake: `2`
   - To get the head position of the 1st snake: `3 1`

4. **View Results**: After processing all queries, the application will output a list of integers representing the head positions for each type 3 query processed.

## Example Usage

Here is an example of how to interact with the application:

```
Enter number of queries: 5
Enter query: 1 5
Enter query: 1 3
Enter query: 3 1
Enter query: 2
Enter query: 3 1
```

**Output:**
```
[1, 3]
```

## Error Handling

The application includes error handling for the following scenarios:
- Entering a non-positive integer for the number of queries.
- Attempting to remove a snake from an empty queue.
- Requesting the head position of a snake that does not exist in the queue.

## Conclusion

This application provides a simple yet effective way to manage a queue of snakes through a series of queries. By following the instructions above, you can easily set up and interact with the software.
```

This manual provides a comprehensive overview of the software, ensuring that users can easily understand how to install and use the application effectively.