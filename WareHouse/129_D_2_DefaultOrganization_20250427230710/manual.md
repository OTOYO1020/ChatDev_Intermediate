Here's a detailed user manual for the lighting grid application, formatted in Markdown as requested:

```markdown
# Lighting Grid Application

A Python application designed to calculate the maximum number of squares that can be lighted by placing a lamp optimally on a grid. The grid consists of empty squares ('.') and obstacles ('#').

## Main Functions

- **Input Handling**: Reads the dimensions of the grid and the grid layout from standard input.
- **Grid Management**: Initializes and manages the grid data and calculations for lighting.
- **Lighting Calculation**: Computes the number of squares that can be lighted from each position in the grid both horizontally and vertically.
- **Maximum Lighted Squares Calculation**: Determines the maximum number of squares that can be lighted by placing a lamp optimally.
- **Input Validation**: Ensures that the input data is valid before processing.

## Installation

To run the Lighting Grid Application, you need to have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

### Dependencies

This application requires no additional dependencies beyond the standard Python library. However, ensure you have Python 3.x installed.

## How to Use the Application

1. **Clone the Repository**: If the application is hosted in a repository, clone it to your local machine using:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Run the Application**: You can run the application by executing the `main.py` file. You will need to provide input through standard input. Here’s how to do it:
   ```bash
   python main.py
   ```

3. **Input Format**: The input should be provided in the following format:
   - The first line contains two integers, `H` (number of rows) and `W` (number of columns).
   - The next `H` lines contain strings of length `W`, representing the grid layout. Use `.` for empty squares and `#` for obstacles.

   **Example Input**:
   ```
   3 5
   ..#..
   .#...
   .....
   ```

4. **Output**: The application will output a single integer representing the maximum number of squares that can be lighted by placing a lamp optimally on the grid.

## Example Usage

Here’s an example of how to run the application with input:

```bash
echo -e "3 5\n..#..\n.#...\n....." | python main.py
```

This command will output the maximum number of squares that can be lighted based on the provided grid.

## Additional Information

For any issues or questions, please refer to the code comments or reach out to the development team for support.

Happy coding!
```

This manual provides a comprehensive overview of the application, its functionalities, installation instructions, and usage guidelines, ensuring that users can effectively utilize the software.