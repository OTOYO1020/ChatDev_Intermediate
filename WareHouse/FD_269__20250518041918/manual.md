Here's the `manual.md` file for the grid sum application, detailing its main functions, installation instructions, and usage guidelines:

```markdown
# Grid Sum Application

Efficiently calculate sums in a large grid without explicitly creating it.

## Overview

The Grid Sum Application allows users to perform sum calculations on a virtual grid defined by its dimensions (N x M). The grid values are calculated using the formula `(i-1) * M + j`, and the application can handle large grids and multiple queries efficiently.

## Main Functions

- **Grid Representation**: The application initializes a grid representation that can handle large sizes without explicitly creating it.
- **Value Calculation**: Each cell's value can be calculated using the formula `(i-1) * M + j`.
- **Range Sum Queries**: Users can query the sum of values in a specified rectangular range, with the option to include or exclude zeros based on the odd/even condition of the sum of the row and column indices.
- **Modulo Operation**: All results are returned modulo `998244353` to ensure they fit within the required bounds.

## Installation

To run the Grid Sum Application, you need to have Python installed on your machine. You can install the required dependencies using pip:

```bash
pip install typing
```

## Usage

1. **Setup the Application**: Import the necessary classes and create an instance of `MainApp`.

2. **Input Configuration**: Use the `setup_input` method to define the grid dimensions (N, M) and the list of queries.

3. **Calculate Sums**: Call the `calculate_sum` method to process the queries and retrieve the results.

### Example Code

Here’s a sample code snippet to demonstrate how to use the application:

```python
from main import MainApp

if __name__ == "__main__":
    app = MainApp()
    # Setup grid dimensions and queries
    app.setup_input(5, 5, [(1, 3, 1, 3), (2, 4, 2, 4)])  # Sample input
    results = app.calculate_sum()
    print(results)  # Output results
```

### Query Format

Each query should be a tuple of four integers `(A, B, C, D)` where:
- `A` is the starting row index (1-based).
- `B` is the ending row index (1-based).
- `C` is the starting column index (1-based).
- `D` is the ending column index (1-based).

### Edge Cases

The application is designed to handle edge cases, including:
- Invalid ranges (e.g., `A < 1`, `B > N`, `C < 1`, `D > M`, or `A > B`, `C > D`), which will return a sum of `0`.
- Maximum values for `N`, `M`, and `Q` to ensure performance under load.

## Conclusion

The Grid Sum Application is a powerful tool for efficiently calculating sums in large grids based on user-defined queries. By leveraging the mathematical properties of grid indexing, it avoids the need for large memory allocations while providing accurate results quickly.

For further information, please refer to the source code and comments within the application files.
```

This manual provides a comprehensive overview of the Grid Sum Application, guiding users through installation, usage, and understanding its core functionalities.