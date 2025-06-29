Here's a detailed user manual for the Snake Queue application, formatted in Markdown:

```markdown
# Snake Queue Application

The Snake Queue application allows users to manage a queue of snakes, where each snake has a specified length. Users can add snakes to the queue, remove them, and query the head position of specific snakes in the queue.

## Main Functions

1. **Add Snake**: Add a snake of a specified length to the queue.
2. **Remove Snake**: Remove the first snake from the queue and adjust the head positions of the remaining snakes.
3. **Get Head Position**: Retrieve the head position of the k-th snake from the front of the queue.

## Installation

To run the Snake Queue application, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. **Install Python**: Download and install Python from the [official website](https://www.python.org/downloads/).

2. **Clone the Repository**: If you haven't already, clone the repository containing the Snake Queue application code.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

3. **Install Dependencies**: Currently, there are no external dependencies required for this project. However, you can create a `requirements.txt` file for future dependencies if needed.

   ```bash
   touch requirements.txt
   ```

## How to Use the Application

1. **Run the Application**: Open your terminal and navigate to the directory where the application files are located. Run the following command:

   ```bash
   python main.py
   ```

2. **Input Queries**: The application will prompt you to enter the number of queries (Q). After that, you can input your queries in the following format:

   - To add a snake: `1 l` (where `l` is the length of the snake)
   - To remove the first snake: `2`
   - To get the head position of the k-th snake: `3 k` (where `k` is the position from the front of the queue)

   Example input:
   ```
   5
   1 3
   1 5
   3 1
   2
   3 1
   ```

3. **View Results**: The application will output the results of all type `3` queries in the order they were processed.

## Example Usage

Here’s an example of how to interact with the application:

```
Enter the number of queries: 5
1 4
1 2
3 1
2
3 1
```

**Output:**
```
0
```

In this example:
- A snake of length 4 is added.
- A snake of length 2 is added.
- The head position of the first snake (which is 0) is queried.
- The first snake is removed.
- The head position of the first snake is queried again (which is now 2).

## Conclusion

The Snake Queue application provides a simple interface for managing a queue of snakes. You can easily add, remove, and query snakes using the provided commands. For any issues or feature requests, please reach out to the development team.

```

This manual provides a comprehensive overview of the Snake Queue application, including installation instructions, usage examples, and a description of its main functions.