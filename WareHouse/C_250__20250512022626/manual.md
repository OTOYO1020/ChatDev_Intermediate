Here's a detailed user manual for the Ball Swapper application, formatted in Markdown as requested.

```markdown
# Ball Swapper

An interactive application for performing ball swapping operations based on user-defined inputs.

## Overview

The Ball Swapper application allows users to define a series of operations to swap balls represented by integers. Each ball is initially numbered from 1 to N. The application processes a list of operations, where each operation specifies which ball to swap. The final arrangement of the balls is displayed after all operations are completed.

## Main Functions

- **perform_swaps(N: int, Q: int, operations: List[int]) -> List[int]**: This function initializes the balls and processes the swap operations based on the input parameters.
- **swap(balls: List[int], index1: int, index2: int)**: A helper function that swaps two balls in the list.

## Installation

To run the Ball Swapper application, ensure you have Python installed on your machine. You can install the required dependencies using pip. 

1. **Clone the repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd ball-swapper
   ```

2. **Install dependencies** (if any):
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   python main.py
   ```

## How to Use the Application

1. **Input Format**:
   - The first line should contain two integers, N and Q, where:
     - N is the number of balls.
     - Q is the number of operations.
   - The next Q lines should each contain one integer, x_i, representing the ball to be swapped.

   **Example Input**:
   ```
   5 3
   1
   2
   5
   ```

2. **Output Format**:
   - The application will output the final state of the balls in a single line, with each integer separated by a space.

   **Example Output**:
   ```
   2 1 3 5 4
   ```

3. **Running the Application**:
   - After starting the application, enter the input as specified above. The application will process the swaps and display the final arrangement of the balls.

## Example Usage

To see the application in action, you can use the following example:

1. Start the application:
   ```bash
   python main.py
   ```

2. Provide the input:
   ```
   5 3
   1
   2
   5
   ```

3. The output will be:
   ```
   2 1 3 5 4
   ```

## Conclusion

The Ball Swapper application is a simple yet effective tool for demonstrating basic list manipulation and user interaction in Python. Feel free to modify the code and explore different scenarios to enhance your understanding of the swapping logic.

For any issues or feature requests, please reach out to the development team.
```

This manual provides a comprehensive guide for users to understand the functionality of the Ball Swapper application, how to install it, and how to use it effectively.