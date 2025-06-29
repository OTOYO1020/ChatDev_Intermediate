Here's a detailed user manual for the Toy Box application, formatted in Markdown as requested:

```markdown
# Toy Box Application

A Python application designed to determine the minimum box size needed to store toys based on their sizes and the available box sizes.

## Main Functions

The Toy Box application provides the following main functions:

- **min_box_size(N: int, A: List[int], B: List[int]) -> int**: 
  - This function calculates the minimum size of a box required to store all toys.
  - It takes three parameters:
    - `N`: The number of toys.
    - `A`: A list of integers representing the sizes of the toys.
    - `B`: A list of integers representing the sizes of the available boxes.
  - The function sorts both lists, checks if the toys can fit into the available boxes, and returns the minimum size of a new box needed or -1 if all toys can be accommodated.

## Installation

To run the Toy Box application, you need to have Python installed on your system. Follow these steps to set up the environment:

1. **Install Python**: Ensure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **Install Dependencies**: Open your terminal or command prompt and run the following command to install the required dependencies:

   ```bash
   pip install typing
   ```

   Note: The `typing` module is included in Python 3.5 and later, so you may not need to install it separately.

## How to Use the Application

1. **Prepare Input Data**: The application reads input from standard input. You need to provide the following:
   - The first line should contain an integer `N`, the number of toys.
   - The second line should contain a comma-separated list of integers representing the sizes of the toys.
   - The third line should contain a comma-separated list of integers representing the sizes of the boxes.

   Example input format:
   ```
   5
   3,5,2,8,6
   4,7,5
   ```

2. **Run the Application**: You can run the application using the command line. Navigate to the directory where the `main.py` file is located and execute the following command:

   ```bash
   python main.py
   ```

3. **View Output**: The application will output the minimum box size needed to store all toys or -1 if it is not possible to store them.

## Example Usage

Given the following input:
```
4
1,2,3,4
2,3
```

The output will be:
```
4
```

This indicates that a box of size 4 is needed to accommodate the largest toy.

## Edge Cases

- If there are no toys (`N = 0`), the function will return `0`.
- If all toys are larger than the largest box available, the function will return the size of the largest toy.

## Conclusion

The Toy Box application is a simple yet effective tool for determining the minimum box size required to store toys based on their sizes and available box sizes. For any further questions or support, please contact the development team.
```

This manual provides a comprehensive overview of the Toy Box application, including its main functions, installation instructions, usage guidelines, and examples.