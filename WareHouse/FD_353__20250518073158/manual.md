Here's a detailed user manual for the Toll Calculator software, formatted in Markdown:

```markdown
# Toll Calculator

A simple application to calculate the minimum toll required for Takahashi to move from a starting point to a target point on a grid of tiles.

## Main Functions

- **minimum_toll(K: int, S_x: int, S_y: int, T_x: int, T_y: int) -> int**: Calculates the minimum toll required for Takahashi to move from the starting point `(S_x, S_y)` to the target point `(T_x, T_y)`. It takes into account the type of tiles he crosses based on the given tile size `K`.

- **get_tile_type(i: int, j: int, K: int) -> str**: Determines the type of tile at the given coordinates `(i, j)`. Returns 'small' if the tile is small and 'large' if the tile is large based on the formula `floor(i/K) + floor(j/K)`.

## Installation

To run the Toll Calculator, you need to have Python installed on your machine. You can install the required dependencies using pip. Follow the steps below:

1. **Clone the repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

   If you don't have a `requirements.txt`, you can simply run the application without additional dependencies as it uses standard libraries.

## How to Use

1. **Run the application**:
   Execute the `main.py` file to start the Toll Calculator.
   ```bash
   python main.py
   ```

2. **Input Parameters**:
   - When prompted, enter the tile size `K`.
   - Enter the starting coordinates `(S_x, S_y)` separated by a space.
   - Enter the target coordinates `(T_x, T_y)` separated by a space.

3. **Output**:
   The application will calculate and display the minimum toll required for Takahashi to reach the target point.

### Example Usage

```plaintext
Enter K: 3
Enter Start (S_x, S_y): 0 0
Enter Target (T_x, T_y): 5 5
Minimum Toll: 2
```

## Edge Cases

- If the starting point is the same as the target point, the toll will be `0`.

## Additional Notes

- The application allows Takahashi to move in any direction (up, down, left, right).
- The toll is counted when crossing from one tile type to another.

## Support

For any issues or feature requests, please reach out to our support team at [support@chatdev.com](mailto:support@chatdev.com).

```

This manual provides a comprehensive overview of the Toll Calculator software, including its main functions, installation instructions, usage guidelines, and support information.