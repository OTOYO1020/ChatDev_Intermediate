Here's a detailed user manual for the Jewel Collector application, formatted in Markdown:

```markdown
# Jewel Collector

Welcome to the Jewel Collector application! This software allows users to collect jewels through a series of operations, maximizing the total value of jewels collected.

## Main Functions

The Jewel Collector application provides the following key functionalities:

- **Collect Jewels**: Users can collect jewels from either end of a deque (double-ended queue).
- **Move Jewels**: Users can move jewels between their hand and the deque.
- **Calculate Maximum Jewel Sum**: The application calculates the maximum sum of jewel values collected based on the operations performed.

## Installation

To run the Jewel Collector application, you need to have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

### Environment Dependencies

The application requires the following Python libraries:

- `collections` (part of the Python standard library)
- `typing` (part of the Python standard library)

You do not need to install any additional packages as the required libraries are included with Python.

## How to Use the Application

1. **Run the Application**: Open your terminal or command prompt and navigate to the directory where the application files are located. Run the following command:

   ```bash
   python main.py
   ```

2. **Input Values**: The application will prompt you to enter the following values:
   - **Number of Jewels (N)**: Enter the total number of jewels available.
   - **Maximum Number of Operations (K)**: Enter the maximum number of operations you wish to perform.
   - **Jewel Values (V)**: Enter the values of the jewels as space-separated integers.

3. **Input Operations**: After entering the jewel values, you will be prompted to enter the operations you wish to perform. The operations can be:
   - **A**: Collect the leftmost jewel from the deque.
   - **B**: Collect the rightmost jewel from the deque.
   - **C**: Move a jewel from your hand back to the left end of the deque.
   - **D**: Move a jewel from your hand back to the right end of the deque.

   Enter the operations as space-separated characters (e.g., `A B C D`).

4. **View Results**: After performing the operations, the application will calculate and display the maximum sum of jewel values collected.

## Example Usage

Here’s an example of how to use the Jewel Collector application:

```
Enter the number of jewels (N): 5
Enter the maximum number of operations (K): 3
Enter the jewel values (space-separated): 10 20 30 40 50
Enter 3 operations (A/B/C/D) separated by spaces: A B C
Max Jewel Sum: 70
```

In this example, the user collected jewels with values 10 and 50, moved one jewel back to the deque, and the maximum sum of jewels collected is 70.

## Conclusion

The Jewel Collector application is a fun and interactive way to engage with jewel collection through various operations. We hope you enjoy using it!

For any issues or feedback, please reach out to our support team.
```

This manual provides a comprehensive overview of the Jewel Collector application, guiding users through installation, usage, and examples to enhance their experience.