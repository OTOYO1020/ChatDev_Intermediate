Here's a detailed user manual for the Santa simulation application, formatted in Markdown:

```markdown
# Santa Simulation Application

Welcome to the Santa Simulation Application! This software allows users to simulate Santa's movements on a grid, where he can visit houses and navigate through passable and impassable cells.

## Main Functions

The Santa Simulation Application includes the following main functions:

- **Grid Representation**: Users can define a grid with passable cells ('.'), impassable cells ('#'), and houses ('@').
- **Movement Commands**: Users can control Santa's movements using commands: 'U' (up), 'D' (down), 'L' (left), and 'R' (right).
- **House Tracking**: The application keeps track of distinct houses visited by Santa during his movements.
- **Input Validation**: The application ensures that the starting position and movement commands are valid.

## Installation

To run the Santa Simulation Application, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**:
   This application is self-contained and does not rely on any third-party packages. However, if you want to set up a virtual environment, you can do so with the following commands:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Create a requirements.txt File** (optional):
   If you anticipate future scalability and the potential need for libraries, you can create a `requirements.txt` file with the following content:
   ```
   # Placeholder for future dependencies
   ```

## How to Use the Application

1. **Run the Application**:
   Execute the main script to start the simulation:
   ```bash
   python main.py
   ```

2. **Input Grid Dimensions and Starting Position**:
   When prompted, enter the grid dimensions (H, W) and Santa's starting position (X, Y) in the following format:
   ```
   H W X Y
   ```
   For example:
   ```
   5 5 1 1
   ```

3. **Define the Grid**:
   Enter the grid representation, where each line corresponds to a row in the grid. Use the characters '.', '#', and '@' to represent passable cells, impassable cells, and houses, respectively. For example:
   ```
   .....
   ..#..
   .@...
   ..#..
   .....
   ```

4. **Enter Movement Commands**:
   After defining the grid, input the movement commands for Santa. Use the characters 'U', 'D', 'L', and 'R' to move Santa up, down, left, and right, respectively. For example:
   ```
   UURRDD
   ```

5. **View Results**:
   After processing the commands, the application will display Santa's final position and the number of distinct houses visited:
   ```
   Final Position: (X, Y)
   Distinct Houses Visited: N
   ```

## Example Usage

Here is an example of how to use the application:

1. Start the application:
   ```bash
   python main.py
   ```

2. Input the following when prompted:
   ```
   5 5 1 1
   .....
   ..#..
   .@...
   ..#..
   .....
   UURRDD
   ```

3. The output will be:
   ```
   Final Position: (3, 3)
   Distinct Houses Visited: 1
   ```

## Conclusion

Thank you for using the Santa Simulation Application! We hope you enjoy simulating Santa's adventures. If you have any questions or feedback, please feel free to reach out.
```

This manual provides a comprehensive overview of the application, including installation instructions, usage guidelines, and an example to help users get started quickly.