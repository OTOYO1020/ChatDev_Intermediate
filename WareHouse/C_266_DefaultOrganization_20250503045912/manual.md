Here's a detailed user manual for the software that checks the convexity of a quadrilateral based on the provided specifications. This manual will guide users through the installation process, usage, and main functions of the software.

```markdown
# Convexity Checker

A simple application to determine if a quadrilateral formed by four vertices is convex.

## Main Functions

The Convexity Checker allows users to input the coordinates of four vertices and checks if the quadrilateral formed by these vertices is convex. The main functions include:

- **Input Handling**: Accepts user input for the coordinates of the vertices in a specified format.
- **Validation**: Ensures that the input coordinates are integers within the range of -10,000 to 10,000.
- **Convexity Check**: Computes the cross products of the vectors formed by the edges of the quadrilateral to determine if it is convex.
- **Output**: Returns 'YES' if the quadrilateral is convex and 'NO' otherwise.

## Installation

To run the Convexity Checker, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. **Install Python**: Make sure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: If you haven't already, clone the repository containing the code:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

3. **Install Dependencies**: The application does not have external dependencies beyond the standard library, so no additional installations are required.

## How to Use

1. **Run the Application**: Open your terminal or command prompt, navigate to the directory where the `main.py` file is located, and run the following command:
   ```bash
   python main.py
   ```

2. **Input Coordinates**: When prompted, enter the coordinates of the four vertices in the following format:
   ```
   Ax, Ay, Bx, By, Cx, Cy, Dx, Dy
   ```
   For example:
   ```
   0, 0, 1, 1, 1, 0, 0, 1
   ```

3. **View Results**: After entering the coordinates, the application will process the input and display whether the quadrilateral is convex:
   ```
   YES
   ```
   or
   ```
   NO
   ```

4. **Error Handling**: If the input is invalid (e.g., not integers, out of range, or incorrect format), the application will provide an error message and prompt you to enter the coordinates again.

## Example Usage

Here’s an example of how to use the application:

1. Start the application:
   ```bash
   python main.py
   ```

2. Input the coordinates:
   ```
   Enter coordinates as Ax, Ay, Bx, By, Cx, Cy, Dx, Dy (comma-separated): 0, 0, 1, 1, 1, 0, 0, 1
   ```

3. Output:
   ```
   YES
   ```

## Conclusion

The Convexity Checker is a straightforward tool for determining the convexity of a quadrilateral based on user-provided vertex coordinates. With its simple interface and robust validation, it ensures accurate results while guiding users through the input process.

For any issues or further inquiries, please contact support at [support@example.com].
```

This manual provides a comprehensive overview of the software, including installation instructions, usage guidelines, and examples to help users effectively utilize the Convexity Checker.