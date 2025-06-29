Here's a detailed user manual for the chocolate bar cutting program, formatted in Markdown as requested:

```markdown
# Chocolate Bar Cutting Program

This program is designed to help users determine the number of cuts needed to divide a chocolate bar represented as a matrix of dark and white squares. Each square can either be dark (`0`) or white (`1`). The program calculates the number of cuts required based on the maximum number of white squares allowed in a single block.

## Main Functions

- **Input Dimensions**: Users can input the height (H) and width (W) of the chocolate bar.
- **Matrix Input**: Users can input the H x W matrix representing the chocolate bar, where each element is either `0` (dark) or `1` (white).
- **Cut Calculation**: The program calculates the number of cuts needed based on the specified maximum number of white squares (K) allowed in a block.
- **Output**: The program outputs the total number of cuts required.

## Installation Instructions

To run the Chocolate Bar Cutting Program, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. **Install Python**: If you don't have Python installed, download and install it from [python.org](https://www.python.org/downloads/).

2. **Install Required Dependencies**: This program does not have any external dependencies, so you can run it with the standard Python installation.

## How to Use the Program

1. **Run the Program**: Open your terminal or command prompt and navigate to the directory where `main.py` is located. Run the program using the following command:
   ```bash
   python main.py
   ```

2. **Input Dimensions**: When prompted, enter the height (H) and width (W) of the chocolate bar. For example:
   ```
   Enter height (H): 3
   Enter width (W): 4
   ```

3. **Input Maximum White Squares**: Enter the maximum number of white squares (K) allowed in a single block. For example:
   ```
   Enter max white squares (K): 2
   ```

4. **Input the Matrix**: Enter the matrix row by row. Each row should consist of `0`s and `1`s separated by spaces. For example:
   ```
   Enter the matrix row by row (0 for dark, 1 for white):
   1 0 1 0
   1 1 1 0
   0 1 0 0
   ```

5. **View the Result**: After entering the matrix, the program will calculate and display the total number of cuts needed. For example:
   ```
   3
   ```

## Example Usage

Here’s an example of how to use the program:

```
$ python main.py
Enter height (H): 3
Enter width (W): 4
Enter max white squares (K): 2
Enter the matrix row by row (0 for dark, 1 for white):
1 0 1 0
1 1 1 0
0 1 0 0
3
```

## Conclusion

The Chocolate Bar Cutting Program is a simple yet effective tool for calculating the number of cuts needed to divide a chocolate bar based on user-defined parameters. Feel free to modify the code to suit your needs or to enhance its functionality.
```

This manual provides a comprehensive overview of the program, installation instructions, and usage guidelines, ensuring that users can easily understand and utilize the software.