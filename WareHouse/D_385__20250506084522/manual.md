Here's a detailed user manual for the Santa Claus house tracking software, formatted in Markdown as requested:

```markdown
# Santa Claus House Tracking Software

This software allows users to track the movements of Santa Claus as he visits various houses based on user-defined movements. It reads the coordinates of houses and Santa's movements to determine how many distinct houses he visits.

## Main Functions

- **Input Handling**: The software reads the number of houses and movements, as well as their respective coordinates and directions.
- **Movement Tracking**: It updates Santa's position based on the movements provided and keeps track of all distinct houses visited.
- **Output**: After processing all movements, the software outputs Santa's final position and the count of distinct houses visited.

## Installation

To run this software, you need to have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

### Environment Setup

1. **Install Python**: Make sure you have Python 3.x installed.
2. **Install Required Dependencies**: This software does not require any external libraries, so you can run it directly after installing Python.

## How to Use the Software

1. **Run the Program**: Open your terminal or command prompt and navigate to the directory where `main.py` is located. Run the following command:
   ```bash
   python main.py
   ```

2. **Input the Number of Houses**: When prompted, enter the number of houses (N) as an integer.

3. **Input the Number of Movements**: Next, enter the number of movements (M) as an integer.

4. **Input House Coordinates**: For each house, input the coordinates in the format `x,y`. For example:
   ```
   Enter house coordinates (x,y): 1,2
   ```

5. **Input Santa's Starting Position**: Enter Santa's starting position in the same `x,y` format:
   ```
   Enter Santa's starting position (x,y): 0,0
   ```

6. **Input Movements**: For each movement, input the direction (U, D, L, R) and distance (C) in the format `D,C`. For example:
   ```
   Enter movement (D,C): U,5
   ```

7. **View Results**: After all movements have been entered, the program will display Santa's final position and the number of distinct houses visited.

## Example Usage

Here’s an example of how to use the software:

```
Enter the number of houses: 3
Enter the number of movements: 4
Enter house coordinates (x,y): 1,2
Enter house coordinates (x,y): 2,3
Enter house coordinates (x,y): 3,4
Enter Santa's starting position (x,y): 0,0
Enter movement (D,C): R,2
Enter movement (D,C): U,3
Enter movement (D,C): L,1
Enter movement (D,C): D,1
```

### Expected Output

```
Final Position: (1, 2)
Distinct Houses Visited: 1
```

## Conclusion

This software provides a simple yet effective way to track Santa's movements and the houses he visits. By following the instructions above, users can easily set up and run the program to see how many distinct houses Santa visits based on their input.

For any issues or further assistance, please reach out to our support team.
```

This manual provides a comprehensive guide for users to understand the software's functionality, installation process, and usage instructions.