Here's a detailed user manual for the software based on the provided code and requirements:

```markdown
# Operation Counter

A simple application to count the number of operations required to reduce a sequence of positive integers to one positive integer.

## Quick Install

To run the Operation Counter application, you need to have Python installed on your machine. You can install the required dependencies using pip:

```bash
pip install heapq
```

## 🤔 What is this?

The Operation Counter application allows users to input a sequence of positive integers and calculates how many operations are needed to reduce the list to a single positive integer. The operations consist of repeatedly sorting the list and decrementing the two largest integers until only one remains.

### Main Functions

- **Input Handling**: The application reads an integer N, which represents the number of positive integers in the sequence, and then reads the sequence of integers A.
- **Operation Counting**: The core functionality is encapsulated in the `OperationCounter` class, which counts the number of operations needed to reduce the list.
- **Max-Heap Implementation**: The application uses a max-heap to efficiently retrieve and manipulate the two largest integers in the sequence.

## 📖 How to Use

1. **Run the Application**: Execute the `main.py` file in your terminal or command prompt.

   ```bash
   python main.py
   ```

2. **Input the Number of Integers**: When prompted, enter the number of positive integers you wish to include in the sequence.

   ```
   Enter the number of positive integers: 5
   ```

3. **Input the Sequence of Integers**: Enter the sequence of integers separated by spaces.

   ```
   Enter 5 positive integers (space-separated): 5 3 2 8 6
   ```

4. **View the Result**: The application will output the total number of operations required to reduce the sequence to one positive integer.

   ```
   Operations Count: 6
   ```

## Error Handling

- If the input does not match the expected format (e.g., non-integer values or incorrect number of integers), the application will prompt the user with an error message.

   ```
   Please ensure you enter exactly N positive integers.
   ```

- If invalid input is detected (e.g., negative integers or zero), the application will notify the user.

   ```
   Invalid input. Please enter integers only.
   ```

## Conclusion

The Operation Counter application is a straightforward tool for counting operations on a sequence of integers. It leverages efficient data structures to ensure optimal performance. For any further questions or support, please reach out to our development team.
```

This manual provides a comprehensive overview of the software, its installation, usage, and error handling, ensuring that users can effectively utilize the application.