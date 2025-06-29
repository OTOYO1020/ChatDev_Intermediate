Here's a detailed user manual for the Pentagon Distance Calculator software, formatted in Markdown:

```markdown
# Pentagon Distance Calculator

A simple application to calculate and compare distances between points defined by vertices of a regular pentagon.

## Overview

The Pentagon Distance Calculator allows users to input characters representing vertices of a regular pentagon (A, B, C, D, E) and calculates the distances between two pairs of vertices. It validates the input to ensure that the characters are valid and distinct, and then compares the lengths of the line segments formed by these vertices.

## Main Functions

- **Input Validation**: Ensures that the characters entered are from the set {A, B, C, D, E} and that the pairs of characters are distinct.
- **Coordinate Retrieval**: Maps each character to its corresponding coordinates on a regular pentagon.
- **Distance Calculation**: Computes the distance between two points using the distance formula.
- **Comparison**: Compares the distances of two segments and outputs whether they are equal.

## Installation

To run the Pentagon Distance Calculator, you need to have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

### Dependencies

This application requires the following Python standard library modules:
- `math`

No additional dependencies are required, as the application uses built-in Python functionality.

## How to Use

1. **Clone the Repository**: If you have the source code, clone the repository to your local machine.
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Run the Application**: Open a terminal and run the main application file.
   ```bash
   python main.py
   ```

3. **Input Characters**: You will be prompted to enter four characters (S1, S2, T1, T2). Make sure to enter characters from the set {A, B, C, D, E} and ensure that S1 is not equal to S2 and T1 is not equal to T2.

4. **View Results**: After entering valid inputs, the application will calculate the distances between the specified points and print 'YES' if the distances are equal, or 'NO' if they are not.

### Example Usage

```plaintext
Enter S1 (A, B, C, D, E): A
Enter S2 (A, B, C, D, E): B
Enter T1 (A, B, C, D, E): C
Enter T2 (A, B, C, D, E): D
YES
```

## Error Handling

- If you enter an invalid character (not in {A, B, C, D, E}), the application will prompt you to enter the characters again.
- If S1 equals S2 or T1 equals T2, the application will notify you and ask for new inputs.

## Conclusion

The Pentagon Distance Calculator is a straightforward tool for calculating and comparing distances between points defined by the vertices of a pentagon. It is designed for ease of use and provides immediate feedback on input validity and distance comparisons.

For any further questions or support, please contact the development team.
```

This manual provides a comprehensive guide for users to understand the software's functionality, installation process, and usage instructions.