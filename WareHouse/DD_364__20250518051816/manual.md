Here's a detailed user manual for the Distance Calculator software, formatted in Markdown:

```markdown
# Distance Calculator

A Python application for calculating the K-th closest distances between two sets of points.

## Overview

The Distance Calculator allows users to input two sets of points (A and B) and a list of K values. For each point in set B, the application computes the absolute distances to all points in set A and retrieves the K-th closest distance. This tool is useful in various applications, including spatial analysis and proximity queries.

## Main Functions

- **Input Parsing**: The application prompts users to enter the number of points in sets A and B, the coordinates of these points, and the K values.
- **Distance Calculation**: For each point in B, the application calculates the absolute distances to all points in A.
- **K-th Closest Distance Retrieval**: The application sorts the distances and retrieves the K-th closest distance based on user input.
- **Error Handling**: The application includes validation checks to ensure that inputs are valid and within expected ranges.

## Installation

To run the Distance Calculator, ensure you have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

### Environment Dependencies

The Distance Calculator does not require any external libraries beyond the standard Python library. However, it is recommended to run the application in a virtual environment. You can set up a virtual environment using the following commands:

```bash
# Create a virtual environment
python -m venv distance_calculator_env

# Activate the virtual environment
# On Windows
distance_calculator_env\Scripts\activate
# On macOS/Linux
source distance_calculator_env/bin/activate
```

## How to Use

1. **Run the Application**: Execute the main application file `main.py` in your terminal or command prompt.

   ```bash
   python main.py
   ```

2. **Input Data**: Follow the prompts to enter the required data:
   - **Number of Points in A (N)**: Enter an integer value.
   - **Points A**: Enter the coordinates of points A as a comma-separated list of integers (e.g., `1,2,3`).
   - **Number of Points in B (Q)**: Enter an integer value.
   - **Points B**: Enter the coordinates of points B as a comma-separated list of integers.
   - **K Values**: Enter the K values as a comma-separated list of positive integers.

3. **View Results**: After entering the data, the application will calculate and display the K-th closest distances for each point in B.

## Example Usage

```
Enter the number of points in A: 3
Enter points A (comma-separated): 1,2,3
Enter the number of points in B: 2
Enter points B (comma-separated): 4,5
Enter K values (comma-separated): 1,2
Results: [1, 2]
```

## Error Handling

The application includes validation checks for:
- Matching the number of points with the specified counts (N and Q).
- Ensuring all input values are integers.
- Checking that all K values are positive integers and within the valid range.

If any input is invalid, the application will prompt the user to re-enter the data.

## Conclusion

The Distance Calculator is a simple yet powerful tool for calculating distances between sets of points. By following the instructions above, users can easily set up and utilize the application for their distance calculation needs.
```

This manual provides a comprehensive guide for users to understand the functionality, installation, and usage of the Distance Calculator software.