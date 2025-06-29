Here's a detailed user manual for the grid illumination software, formatted in Markdown as requested:

```markdown
# Grid Illumination Software

Illuminate your grid with bulbs while avoiding blocks!

## Overview

This software allows users to create a grid of specified dimensions, place bulbs and blocks on it, and calculate the number of illuminated squares. Bulbs illuminate squares in all four directions until they encounter a block or the edge of the grid.

## Main Functions

- **Grid Creation**: Initialize a grid of specified height (H) and width (W).
- **Bulb Placement**: Add bulbs to the grid at specified coordinates.
- **Block Placement**: Add blocks to the grid at specified coordinates.
- **Illumination Calculation**: Calculate and return the number of unique illuminated squares.

## Installation

To run the software, you need Python installed on your machine. Follow these steps to set up the environment:

1. **Install Python**: Ensure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: If you have the source code in a repository, clone it using:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

3. **Install Dependencies**: Use pip to install any required dependencies. If there are no additional dependencies, you can skip this step. Otherwise, run:
   ```bash
   pip install -r requirements.txt
   ```

## How to Use the Software

1. **Run the Application**: Execute the main script to start the application:
   ```bash
   python main.py
   ```

2. **Input the Grid Dimensions**: When prompted, enter the height (H) and width (W) of the grid, separated by a space. For example:
   ```
   5 5
   ```

3. **Input the Number of Bulbs and Blocks**: Enter the number of bulbs (N) and blocks (M), separated by a space. For example:
   ```
   3 2
   ```

4. **Input Bulb Coordinates**: For each bulb, enter its coordinates (A_i, B_i) in the format:
   ```
   A B
   ```
   For example:
   ```
   1 1
   2 2
   3 3
   ```

5. **Input Block Coordinates**: For each block, enter its coordinates (C_i, D_i) in the same format:
   ```
   C D
   ```
   For example:
   ```
   0 1
   4 4
   ```

6. **View the Result**: After entering all the data, the application will calculate and print the number of unique illuminated squares.

## Example Usage

Here’s an example of how to use the software:

```plaintext
$ python main.py
5 5
3 2
1 1
2 2
3 3
0 1
4 4
```

**Output**:
```plaintext
10
```

This indicates that there are 10 unique illuminated squares in the grid.

## Error Handling

- If you enter an invalid number of bulbs or blocks, or if the coordinates are out of bounds, the application will display an error message.
- Ensure that bulbs and blocks do not overlap in their coordinates.

## Conclusion

This grid illumination software is a simple yet powerful tool for visualizing how bulbs illuminate a grid while avoiding obstacles. Feel free to modify and enhance the code as needed for your specific use cases!

For any issues or feature requests, please contact the development team.
```

This manual provides a comprehensive guide for users to understand and effectively utilize the grid illumination software.