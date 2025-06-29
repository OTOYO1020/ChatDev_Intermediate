Here's a detailed user manual for the Distance Calculator application, formatted in Markdown:

```markdown
# Distance Calculator

A simple application to calculate distances between two sets of coordinates.

## Overview

The Distance Calculator allows users to input two sets of coordinates, \( A \) and \( B \), and retrieve specific distances based on user-defined indices. The application calculates the absolute distances between each point in \( A \) and each point in \( B \), sorts these distances, and allows the user to select the k-th closest distance for each point in \( B \).

## Main Functions

- **Input Handling**: The application reads integers \( N \) (number of coordinates in \( A \)) and \( Q \) (number of coordinates in \( B \)), followed by the coordinates themselves and the k-th indices.
- **Distance Calculation**: Computes the absolute distance between each pair of coordinates from \( A \) and \( B \).
- **Sorting and Retrieval**: Sorts the calculated distances and retrieves the specified k-th closest distance for each query.

## Installation

To run the Distance Calculator, ensure you have Python installed on your system. You can install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

If you do not have a `requirements.txt` file, you can simply run the application as it does not have external dependencies beyond the Python standard library.

## How to Use

1. **Run the Application**: Execute the main script in your terminal or command prompt.

   ```bash
   python main.py
   ```

2. **Input Data**: Follow the prompts to enter the required data:
   - Enter two positive integers \( N \) and \( Q \) (e.g., `5 3`).
   - Enter \( N \) integers for coordinates \( A \) (e.g., `1 2 3 4 5`).
   - Enter \( Q \) integers for coordinates \( B \) (e.g., `2 3 5`).
   - Enter \( Q \) k-th indices (e.g., `1 2 3`), which should be between 1 and \( N \).

3. **View Results**: The application will output the k-th closest distances for each coordinate in \( B \), printed line by line.

## Example Usage

```plaintext
Enter two positive integers N (number of A coordinates) and Q (number of B coordinates): 5 3
Enter 5 coordinates for A (space-separated): 1 2 3 4 5
Enter 3 coordinates for B (space-separated): 2 3 5
Note: k_j values must be between 1 and 5 (inclusive). Please enter them as space-separated integers.
Enter 3 k_j values (1-based index, space-separated): 1 2 3
```

### Sample Output

```plaintext
0
1
2
```

## Error Handling

The application includes error handling for:
- Invalid input formats.
- Out-of-bounds k-th indices.
- Mismatched input lengths.

If an error occurs, the application will provide a descriptive message to guide the user in correcting their input.

## Conclusion

The Distance Calculator is a straightforward tool for calculating and retrieving distances between two sets of coordinates. It is designed for ease of use and provides clear feedback for user inputs. For any issues or suggestions, please contact the development team.
```

This manual provides a comprehensive guide for users to understand the functionality of the Distance Calculator, how to install it, and how to use it effectively.