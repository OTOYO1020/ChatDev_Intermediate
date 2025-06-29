Here's a detailed user manual for the software, formatted in Markdown as requested:

```markdown
# Lattice Point Distance Checker

This software checks for the existence of lattice points at a distance of √5 from two given points in a 2D coordinate system.

## Main Functions

The primary function of this software is `is_lattice_point_distance_sqrt5(x1: int, y1: int, x2: int, y2: int) -> bool`. This function determines whether there exists a lattice point that is at a distance of √5 from both specified points (x1, y1) and (x2, y2).

### Key Features:
- Calculates squared distances from lattice points to the given points.
- Iterates through possible lattice points within a reasonable range.
- Returns `True` if any lattice point satisfies the distance condition, otherwise returns `False`.
- Handles input through a main function that reads integers from standard input.

## Installation

To run this software, you need to have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Environment Dependencies

This software does not require any external libraries beyond the standard Python library. Simply ensure you have Python 3.x installed.

## How to Use

1. **Clone the Repository**: If you have the code in a repository, clone it to your local machine.
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Run the Application**:
   - Open your terminal or command prompt.
   - Navigate to the directory where the `main.py` file is located.
   - Run the application using the following command:
     ```bash
     python main.py
     ```

3. **Input Format**:
   - The program expects four integers as input, representing the coordinates of the two points:
     ```
     x1 y1 x2 y2
     ```
   - For example, to check the points (1, 2) and (3, 4), you would input:
     ```
     1 2 3 4
     ```

4. **Output**:
   - The program will print `Yes` if there exists a lattice point at a distance of √5 from both points, otherwise it will print `No`.

5. **Error Handling**:
   - If the input is invalid (not four integers), the program will output:
     ```
     Invalid input. Please enter four integers.
     ```

## Example Usage

To check if there exists a lattice point at a distance of √5 from the points (0, 0) and (1, 2):

1. Run the program:
   ```bash
   python main.py
   ```

2. Input:
   ```
   0 0 1 2
   ```

3. Output:
   ```
   Yes
   ```

## Conclusion

This software provides a simple and effective way to determine the existence of lattice points at a specific distance from given coordinates. For any further assistance or inquiries, please contact the support team.
```

This manual provides a comprehensive overview of the software, its functionality, installation instructions, and usage guidelines, ensuring that users can effectively utilize the application.