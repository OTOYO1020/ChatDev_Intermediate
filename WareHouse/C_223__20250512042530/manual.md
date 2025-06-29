Here's a detailed user manual for the Fuse Burning application, formatted in Markdown as requested:

```markdown
# Fuse Burning Application

The Fuse Burning application calculates the meeting point of two flames burning towards each other from opposite ends of a series of fuses. This application is designed to help users understand how different fuse lengths and burn speeds affect the point at which the flames meet.

## Main Functions

- **find_meeting_point(N: int, A: List[float], B: List[float]) -> float**: This function calculates the meeting point of two flames based on the number of fuses, their lengths, and their burn speeds. It simulates the burning process and returns the distance from the left end to the meeting point.

## Installation

To run the Fuse Burning application, you need to install the required dependencies. You can do this using `pip`. 

1. **Clone the repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install dependencies**:
   Create a `requirements.txt` file with the following content:
   ```
   # Optional: Uncomment if you plan to use numpy for numerical computations
   # numpy
   ```

   Then run:
   ```bash
   pip install -r requirements.txt
   ```

## How to Use the Application

1. **Run the application**:
   Execute the `main.py` script to start the application:
   ```bash
   python main.py
   ```

2. **Input the required parameters**:
   - Enter the number of fuses (N).
   - Enter the lengths of the fuses as a comma-separated list (e.g., `1.5,2.0,3.0`).
   - Enter the burn speeds as a comma-separated list (e.g., `0.5,1.0,1.5`).

   Example input:
   ```
   Enter the number of fuses: 3
   Enter lengths of fuses (comma-separated): 1.5,2.0,3.0
   Enter burn speeds (comma-separated): 0.5,1.0,1.5
   ```

3. **View the output**:
   After entering the inputs, the application will calculate the meeting point and display it formatted to two decimal places:
   ```
   Meeting Point: 2.00
   ```

## Error Handling

The application includes basic error handling for the following scenarios:
- If the lengths of lists A and B do not match the number of fuses (N), an error message will be displayed.
- If any length or speed is less than or equal to zero, an error message will be displayed.

## Example Usage

To see the application in action, you can use the following example inputs:

- **Example 1**:
  ```
  Enter the number of fuses: 2
  Enter lengths of fuses (comma-separated): 2.0,3.0
  Enter burn speeds (comma-separated): 1.0,1.5
  ```
  Output:
  ```
  Meeting Point: 2.50
  ```

- **Example 2**:
  ```
  Enter the number of fuses: 1
  Enter lengths of fuses (comma-separated): 5.0
  Enter burn speeds (comma-separated): 2.0
  ```
  Output:
  ```
  Meeting Point: 5.00
  ```

## Conclusion

The Fuse Burning application provides a simple yet effective way to visualize and calculate the meeting point of flames burning from opposite ends of a series of fuses. By adjusting the lengths and speeds, users can explore how these factors influence the outcome.

For any further questions or support, please reach out to the development team.
```

This manual provides a comprehensive overview of the application, including installation instructions, usage guidelines, and examples to help users effectively utilize the Fuse Burning application.