Here’s a detailed user manual for the software that determines if a quadrilateral is convex, formatted in Markdown:

```markdown
# Convex Quadrilateral Checker

A Python application to determine if a quadrilateral formed by four points is convex.

## Main Functions

The software provides the following main functions:

- **Input Handling**: Reads the coordinates of four vertices from standard input, ensuring they are integers within the specified range.
- **Convexity Check**: Determines if the quadrilateral is convex by calculating the cross products of the edge vectors.
- **Error Handling**: Validates input to ensure no two vertices are the same and no three vertices are collinear.
- **Output**: Displays "Yes" if the quadrilateral is convex and "No" otherwise.

## Installation

To run the application, you need to have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

### Environment Dependencies

This application does not require any external libraries beyond the standard Python library. However, ensure you have Python 3.x installed.

## How to Use

1. **Clone the Repository**: If you have the source code, clone the repository to your local machine.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Run the Application**: Execute the `main.py` file in your terminal or command prompt.

   ```bash
   python main.py
   ```

3. **Input Coordinates**: When prompted, enter the coordinates for the four vertices in the format `A_x A_y`, `B_x B_y`, `C_x C_y`, and `D_x D_y`. For example:

   ```
   Enter coordinates for A (A_x A_y): 0 0
   Enter coordinates for B (B_x B_y): 1 0
   Enter coordinates for C (C_x C_y): 1 1
   Enter coordinates for D (D_x D_y): 0 1
   ```

4. **View Results**: After entering the coordinates, the application will check if the quadrilateral is convex and display the result:

   ```
   Yes, the quadrilateral is convex.
   ```

## Error Handling

The application includes error handling for the following cases:

- **Invalid Coordinates**: Coordinates must be integers within the range of -10^6 to 10^6.
- **Non-Unique Vertices**: All four vertices must be unique.
- **Collinear Points**: No three vertices can be collinear to form a valid quadrilateral.

If any of these conditions are not met, the application will display an appropriate error message.

## Test Cases

You can test the application with various configurations of quadrilaterals:

1. **Convex Quadrilateral**:
   ```
   Enter coordinates for A (A_x A_y): 0 0
   Enter coordinates for B (B_x B_y): 2 0
   Enter coordinates for C (C_x C_y): 2 2
   Enter coordinates for D (D_x D_y): 0 2
   ```

   Output: `Yes, the quadrilateral is convex.`

2. **Non-Convex Quadrilateral**:
   ```
   Enter coordinates for A (A_x A_y): 0 0
   Enter coordinates for B (B_x B_y): 2 2
   Enter coordinates for C (C_x C_y): 1 1
   Enter coordinates for D (D_x D_y): 0 2
   ```

   Output: `No, the quadrilateral is not convex.`

## Conclusion

This application provides a straightforward way to determine the convexity of a quadrilateral based on user-defined vertex coordinates. For further assistance or to report issues, please contact the development team.
```

This manual provides a comprehensive overview of the software's functionality, installation instructions, usage guidelines, and error handling, ensuring users can effectively utilize the application.