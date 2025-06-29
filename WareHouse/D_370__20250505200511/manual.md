Here is the `manual.md` file that provides a detailed user manual for the wall management application:

```markdown
# Wall Management Application

Manage and destroy walls in a grid using bomb placement queries.

## Overview

The Wall Management Application allows users to define a grid filled with walls and process bomb placement queries to destroy walls based on specified coordinates. The application is designed to be simple and efficient, making it easy for users to interact with the grid.

## Main Functions

1. **Initialize Grid**: Define the dimensions of the grid (Height and Width) and fill it with walls.
2. **Process Queries**: For each bomb placement query, determine whether to destroy a wall at the specified coordinates or find the nearest wall in the four cardinal directions (up, down, left, right).
3. **Count Remaining Walls**: After processing all queries, count and display the total number of walls that remain in the grid.

## Installation

To run the Wall Management Application, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. **Install Python**: Download and install Python from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: Clone the repository containing the application code.
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

3. **Install Dependencies**: If there are any additional dependencies required, you can install them using pip. For this application, no external libraries are needed beyond Python's standard library.

## How to Use the Application

1. **Run the Application**: Open your terminal and navigate to the directory where the application is located. Run the following command:
   ```bash
   python main.py
   ```

2. **Input Grid Dimensions**: When prompted, enter the height and width of the grid separated by a space. For example:
   ```
   Please enter grid dimensions (Height Width): 5 5
   ```

3. **Input Number of Queries**: Enter the number of bomb placement queries you wish to process. For example:
   ```
   Please enter the number of bomb placement queries: 3
   ```

4. **Input Bomb Coordinates**: For each query, enter the row and column coordinates where you want to place the bomb. For example:
   ```
   Please enter bomb coordinates (Row Column): 3 3
   ```

5. **View Remaining Walls**: After processing all queries, the application will display the total number of remaining walls in the grid:
   ```
   Total remaining walls: 20
   ```

## Example Usage

Here’s an example of how to use the application:

1. Start the application:
   ```bash
   python main.py
   ```

2. Input grid dimensions:
   ```
   Please enter grid dimensions (Height Width): 4 4
   ```

3. Input number of queries:
   ```
   Please enter the number of bomb placement queries: 2
   ```

4. Input bomb coordinates:
   ```
   Please enter bomb coordinates (Row Column): 2 2
   Please enter bomb coordinates (Row Column): 4 4
   ```

5. View the result:
   ```
   Total remaining walls: 14
   ```

## Conclusion

The Wall Management Application is a straightforward tool for managing walls in a grid. By following the instructions above, users can easily set up the application and process bomb placement queries to manipulate the grid as needed.
```

This manual provides users with a comprehensive guide to understanding and using the Wall Management Application effectively.