Here is the `manual.md` file for the Santa's movement simulation software:

```markdown
# Santa's Movement Simulation

A fun simulation to track Santa's movements and the distinct houses he visits during his journey.

## Overview

This software allows users to simulate Santa's movements based on given instructions and track the distinct houses he passes through or arrives at. The main function, `find_final_position_and_houses`, processes the input parameters and calculates Santa's final position along with the count of distinct houses visited.

## Main Functions

- **find_final_position_and_houses(N: int, houses: List[Tuple[int, int]], M: int, movements: List[Tuple[str, int]], S: Tuple[int, int])**
  - **Parameters:**
    - `N`: Number of houses.
    - `houses`: A list of tuples representing the coordinates of the houses.
    - `M`: Number of movements.
    - `movements`: A list of tuples where each tuple contains a direction and a distance.
    - `S`: A tuple representing Santa's starting position.
  - **Returns:** A tuple containing Santa's final position and the count of distinct houses visited.

## Installation

To run the Santa's Movement Simulation, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install dependencies:**
   You can use pip to install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

   If you don't have a `requirements.txt`, you can run the main application without additional dependencies as it uses standard libraries.

## How to Use

1. **Run the application:**
   Execute the main application file:
   ```bash
   python main.py
   ```

2. **Input Parameters:**
   You will be prompted to enter the following:
   - The number of houses (N).
   - The coordinates of the houses as a list of tuples (e.g., `[(1, 2), (3, 4)]`).
   - The number of movements (M).
   - The movement instructions as a list of tuples (e.g., `[(‘U’, 2), (‘R’, 3)]`).
   - Santa's starting position as a tuple (e.g., `(0, 0)`).

3. **Output:**
   After entering the required inputs, the application will display:
   - Santa's final position.
   - The count of distinct houses he visited.

## Example Usage

```
Enter the number of houses (N): 3
Enter the houses as a list of tuples (e.g., [(1, 2), (3, 4)]): [(1, 2), (3, 4), (5, 5)]
Enter the number of movements (M): 4
Enter the movements as a list of tuples (e.g., [('U', 2), ('R', 3)]): [('U', 2), ('R', 3), ('D', 1), ('L', 1)]
Enter the starting position as a tuple (e.g., (0, 0)): (0, 0)
Final Position: (2, 1)
Distinct Houses Count: 2
```

## Conclusion

This software provides an engaging way to visualize Santa's journey and the houses he visits. Feel free to modify the movement instructions and house coordinates to explore different scenarios!
```

This manual provides a comprehensive guide for users to understand the software's functionality, installation process, and usage instructions.