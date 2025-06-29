Here's a detailed user manual for the Cookie Finder application, formatted in Markdown as requested:

```markdown
# Cookie Finder

A simple application to identify the coordinates of a missing cookie in a grid representation.

## Overview

The Cookie Finder application allows users to input a grid of cookies ('C') and empty spaces ('.') and determines the position of a missing cookie within a defined rectangular area. This application is useful for scenarios where you need to track the presence of items in a grid format.

## Main Functions

- **find_eaten_cookie(H: int, W: int, grid: List[List[str]]) -> Tuple[int, int]**: This function processes the grid to find the coordinates of the missing cookie. It takes the height and width of the grid along with the grid itself as input.

- **GridManager**: A class that manages the grid input and invokes the `find_eaten_cookie` function. It ensures the grid is valid and processes the grid data.

## Installation

To run the Cookie Finder application, you need to have Python installed on your system. Follow these steps to set up the environment:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/cookie-finder.git
   cd cookie-finder
   ```

2. **Create a Virtual Environment (optional but recommended)**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   Since there are no additional packages required for this project, you can skip this step. However, if you want to keep it open for future scalability, you can create a `requirements.txt` file with common libraries (as shown below).

   Example `requirements.txt`:
   ```
   # No additional packages needed currently
   ```

4. **Run the Application**:
   You can run the application using the following command:
   ```bash
   python main.py
   ```

## How to Use the Application

1. **Input Format**:
   The application expects a grid input where:
   - 'C' represents a cookie.
   - '.' represents an empty space.
   The first line of input should be the height (H) and width (W) of the grid, followed by the grid itself.

   Example Input:
   ```
   4 5
   CCCCC
   C...C
   CCCCC
   CCCCC
   ```

2. **Running the Application**:
   - After starting the application, input the grid line by line. 
   - Press Enter after each line. 
   - To finish inputting the grid, simply press Enter on an empty line.

3. **Output**:
   The application will output the coordinates of the missing cookie in the format `(i, j)`, where `i` is the row index and `j` is the column index. If no missing cookie is found, it will output "No missing cookie found."

   Example Output:
   ```
   Missing cookie at: (1, 1)
   ```

## Example

Here’s a complete example of how to run the application:

1. Start the application:
   ```bash
   python main.py
   ```

2. Input the grid:
   ```
   4 5
   CCCCC
   C...C
   CCCCC
   CCCCC
   ```

3. Output:
   ```
   Missing cookie at: (1, 1)
   ```

## Conclusion

The Cookie Finder application is a straightforward tool for identifying missing items in a grid format. It is designed to be user-friendly and efficient, making it suitable for various applications where grid management is necessary.

For any issues or feature requests, please reach out to the development team.
```

This manual provides a comprehensive guide for users to understand the functionality, installation process, and usage of the Cookie Finder application.