Here's a detailed user manual for the Chocolate Cutting application, formatted in Markdown as requested:

```markdown
# Chocolate Cutting Application

Calculate the minimum number of cuts needed to ensure that each block of chocolate has K or fewer white squares.

## Overview

The Chocolate Cutting application allows users to input the dimensions of a chocolate bar represented as a 2D list of integers (0s and 1s), where 0 represents a brown square and 1 represents a white square. The application calculates the minimum number of cuts required to ensure that each resulting block of chocolate contains K or fewer white squares.

## Main Functions

- **Input Parameters**:
  - **Height (H)**: The number of rows in the chocolate bar.
  - **Width (W)**: The number of columns in the chocolate bar.
  - **Max White Squares (K)**: The maximum number of white squares allowed in each block after cutting.
  - **Chocolate Bar (S)**: A 2D list representing the chocolate bar, where each element is either 0 (brown) or 1 (white).

- **Calculate Cuts**: The application processes the input and computes the minimum number of cuts required.

## Installation

To run the Chocolate Cutting application, ensure you have Python installed on your machine. You can install the required dependencies using pip. Open your terminal or command prompt and run:

```bash
pip install tkinter
```

## How to Use the Application

1. **Run the Application**:
   - Execute the `main.py` file in your Python environment. This will launch the graphical user interface (GUI) for the Chocolate Cutting application.

2. **Input the Parameters**:
   - Enter the height (H) of the chocolate bar in the designated field.
   - Enter the width (W) of the chocolate bar in the designated field.
   - Enter the maximum number of white squares (K) allowed in each block.
   - Input the chocolate bar as a 2D list in the format `[[0, 1], [1, 0]]` in the provided text area.

3. **Calculate Minimum Cuts**:
   - Click the "Calculate Cuts" button to process the input. The application will compute the minimum number of cuts required and display the result.

4. **View Results**:
   - The result will be displayed below the button, indicating the minimum cuts required for the specified chocolate bar configuration.

## Example Input

For a chocolate bar of size 3x3 with the following configuration:

```
[[0, 1, 0],
 [1, 1, 0],
 [0, 0, 1]]
```

If you set K to 2, the application will calculate the minimum cuts needed to ensure that no block has more than 2 white squares.

## Edge Cases

- If the entire chocolate bar already satisfies the condition (i.e., contains K or fewer white squares), the application will return 0 cuts needed.
- If the height (H) or width (W) is 1, the application will handle it appropriately, returning 0 cuts if the condition is satisfied.

## Troubleshooting

- Ensure that the input for the chocolate bar (S) is a valid 2D list.
- If you encounter any errors, check the input values for correctness and format.

## Conclusion

The Chocolate Cutting application is a simple yet effective tool for calculating the minimum cuts needed for a chocolate bar based on user-defined parameters. Enjoy using the application to solve your chocolate cutting problems!
```

This manual provides a comprehensive guide for users to understand the functionality of the Chocolate Cutting application, how to install it, and how to use it effectively.