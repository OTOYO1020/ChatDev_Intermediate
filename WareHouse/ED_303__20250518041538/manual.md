Here's a detailed user manual for the software that counts level-k stars in a tree, formatted in Markdown as requested:

```markdown
# Level-K Star Counter

A Python application for counting level-k stars in a tree structure defined by edges.

## Overview

This software allows users to input a tree structure defined by edges and counts the number of level-k stars that can be formed based on the degrees of the vertices. A level-k star is defined as a vertex with degree k+1 and k neighbors that are leaves (degree 1).

## Main Functions

- **parse_input**: Reads the input data and stores the edges in a suitable data structure.
- **calculate_degrees**: Calculates the degree of each vertex in the tree.
- **is_star**: Checks if a given vertex forms a level-k star.
- **count_stars**: Iterates through the edges of the tree and counts how many level-k stars can be formed.
- **output_results**: Formats the output to display the number and levels of stars found in the tree.

## Installation

To run this application, ensure you have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

### Dependencies

This application does not require any external libraries, but it is recommended to use Python 3.6 or higher.

## How to Use

1. **Clone the Repository**: If you have the source code, clone the repository to your local machine.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Run the Application**: Open a terminal and run the `main.py` file.

   ```bash
   python main.py
   ```

3. **Input Format**: When prompted, enter the number of edges followed by the edges themselves in the format `u v`, each on a new line. For example:

   ```
   4
   1 2
   1 3
   1 4
   3 5
   ```

   In this example, there are 4 edges, and the edges are defined as (1, 2), (1, 3), (1, 4), and (3, 5).

4. **View Results**: After entering the edges, the application will process the tree and output the number of level-k stars found, formatted by their levels.

## Example Usage

```plaintext
Enter the number of edges followed by the edges (u, v) in the format 'u v', each on a new line:
4
1 2
1 3
1 4
3 5
Level-1 stars: 1
Level-2 stars: 1
```

## Error Handling

The application includes error handling for the following scenarios:

- Non-integer input for the number of edges.
- Negative number of edges.
- Mismatched number of edges and provided edge list.
- Duplicate edges.
- Non-positive vertex values.

If an error occurs, a descriptive message will be displayed.

## Conclusion

This application provides a straightforward way to analyze tree structures and identify level-k stars. For any issues or feature requests, please reach out to the development team.

```

This manual provides a comprehensive guide for users to understand the software's functionality, installation process, and usage instructions. Let me know if you need any modifications or additional information!