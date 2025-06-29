Here is the `manual.md` file for the grid pathfinding application using BFS:

```markdown
# Grid Pathfinding Application

A Python application for finding the shortest path in a grid using Breadth-First Search (BFS) algorithm.

## Overview

This application allows users to input a grid of characters, where 'S' represents the starting point, 'G' represents the goal, and '#' represents obstacles. The application will determine the shortest time taken to reach 'G' from 'S', considering valid moves and teleporters.

## Main Functions

- **Input Grid Dimensions**: Users can specify the height (H) and width (W) of the grid.
- **Grid Population**: Users can populate the grid with characters from standard input.
- **Pathfinding**: The application uses BFS to find the shortest path from 'S' to 'G'.
- **Teleportation**: The application supports teleportation through characters 'a' to 'z', allowing instant travel between the same characters.

## Installation

To run the application, you need to have Python installed on your system. You can install the required dependencies using pip. Follow these steps:

1. **Clone the Repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

   If you don't have a `requirements.txt`, ensure you have the following packages:
   - `collections` (part of Python standard library, no installation needed)

## Usage

1. **Run the Application**:
   Execute the main application file:
   ```bash
   python main.py
   ```

2. **Input the Grid**:
   - First, input the dimensions of the grid (H and W) separated by a space. For example:
     ```
     5 5
     ```
   - Then, input the grid rows, where each row contains characters. For example:
     ```
     S....
     .#...
     ..#..
     ...#G
     .....
     ```
   - Ensure that 'S' and 'G' are present in the grid.

3. **Output**:
   - The application will output the time taken to reach 'G' from 'S'. If 'G' is unreachable, it will output `-1`.

## Example

Here’s an example of how to use the application:

```plaintext
Input:
5 5
S....
.#...
..#..
...#G
.....

Output:
8
```

In this example, it took 8 moves to reach 'G' from 'S'.

## Notes

- The maximum grid size supported is 2000x2000.
- Ensure that the grid is properly formatted with valid characters.
- The application handles teleportation efficiently, allowing for quick navigation through the grid.

## Support

For any issues or questions, please reach out to our support team via the provided contact methods.

```

This manual provides a comprehensive guide for users to understand the application, its functionality, and how to effectively use it.