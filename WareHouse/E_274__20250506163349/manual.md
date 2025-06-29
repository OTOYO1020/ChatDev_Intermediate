Here's a detailed user manual for the software based on the provided code and requirements:

```markdown
# Towns and Chests Travel Time Calculator

A Python application designed to calculate the minimum time required to visit a set of towns and return to the origin, while considering the presence of chests that can double the travel speed.

## Quick Install

To run this application, you need to have Python installed on your system. You can install the required dependencies using pip:

```bash
pip install math itertools
```

## 🤔 What is this?

This application allows users to input a number of towns and chests represented by their coordinates. The program calculates the minimum time required to visit all towns in every possible order and return to the starting point (origin). If a chest is encountered along the way, the travel speed is doubled.

### Main Functions

1. **Input Handling**: 
   - The application reads integers `N` (number of towns) and `M` (number of chests) from standard input.
   - It then reads the coordinates for towns and chests.

2. **Distance Calculation**:
   - The application uses the `euclidean_distance(x1, y1, x2, y2)` function to calculate the distance between two points.

3. **Permutations**:
   - It generates all possible permutations of the towns using `itertools.permutations`.

4. **Time Calculation**:
   - For each permutation, it calculates the total time taken to visit all towns and return to the origin, adjusting for speed when chests are encountered.

5. **Output**:
   - The minimum time required to complete the trip is printed to the console.

## 📖 How to Use

1. **Run the Application**:
   - Execute the main application file `main.py` in your terminal or command prompt.

   ```bash
   python main.py
   ```

2. **Input Format**:
   - When prompted, enter the number of towns (N) and the number of chests (M).
   - Enter the towns' coordinates in the format `X1,Y1;X2,Y2;...` (e.g., `1,2;3,4;5,6`).
   - Enter the chests' coordinates in the format `P1,Q1;P2,Q2;...` (e.g., `2,3;4,5`).

   Example Input:
   ```
   Enter the number of towns (N): 3
   Enter the number of chests (M): 2
   Enter towns (X1,Y1;X2,Y2;...): 1,2;3,4;5,6
   Enter chests (P1,Q1;P2,Q2;...): 2,3;4,5
   ```

3. **Output**:
   - The application will calculate and display the minimum time required to visit all towns and return to the origin.

   Example Output:
   ```
   Minimum time required: 10.50
   ```

## 🛠️ Dependencies

This application requires Python 3.x and the following libraries:
- `math`: For mathematical operations.
- `itertools`: For generating permutations.

## 📄 Error Handling

- The application includes basic error handling for input validation. If the input format is incorrect or the number of coordinates does not match the specified counts, an error message will be displayed.

## 💡 Additional Notes

- Ensure that the input coordinates are integers and follow the specified format to avoid input errors.
- The application is designed to handle a reasonable number of towns and chests; however, performance may degrade with a large number of towns due to the factorial growth of permutations.

For any further assistance or feature requests, please contact the development team.
```

This manual provides a comprehensive guide for users to understand how to install, use, and troubleshoot the application effectively.