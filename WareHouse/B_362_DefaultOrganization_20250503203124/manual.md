Here's the `manual.md` file for the Triangle Right Check application:

```markdown
# Triangle Right Check Application

A simple application to determine if a triangle formed by three points in a 2D plane is a right triangle based on user-provided coordinates.

## Main Functions

The Triangle Right Check application provides the following main functionalities:

- **Input Coordinates**: Users can input the coordinates of three points in the format `xA, yA, xB, yB, xC, yC`.
- **Validation**: The application validates the input to ensure that exactly six integers are provided and that they can form a valid triangle.
- **Right Triangle Check**: The application calculates the squared lengths of the triangle's sides and checks if the triangle is a right triangle using the Pythagorean theorem.
- **Output Result**: The application outputs "YES" if the triangle is a right triangle and "NO" otherwise.

## Installation

To run the Triangle Right Check application, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. **Install Python**: Ensure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: Clone the repository containing the application files.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

3. **Install Dependencies**: The application does not require any external libraries, but ensure you have Python's built-in libraries available.

## How to Use the Application

1. **Run the Application**: Open a terminal or command prompt, navigate to the directory where the application files are located, and run the main application file.

   ```bash
   python main.py
   ```

2. **Input Coordinates**: When prompted, enter the coordinates of the three points in the specified format. For example:

   ```
   Enter coordinates in the format xA, yA, xB, yB, xC, yC (e.g., 0,0,3,0,0,4):
   ```

   Input: `0,0,3,0,0,4`

3. **View Results**: After entering the coordinates, the application will validate the input and check if the triangle is a right triangle. The result will be printed as either "YES" or "NO".

## Example Usage

- **Valid Input**: 
   ```
   Enter coordinates in the format xA, yA, xB, yB, xC, yC (e.g., 0,0,3,0,0,4):
   0,0,3,0,0,4
   YES
   ```

- **Invalid Input**: 
   ```
   Enter coordinates in the format xA, yA, xB, yB, xC, yC (e.g., 0,0,3,0,0,4):
   0,0,3,0,0,0
   Input Error: Please enter exactly six integers that can form a triangle (non-collinear).
   ```

## Conclusion

The Triangle Right Check application is a straightforward tool for checking the properties of triangles based on user input. For any issues or feature requests, please contact our support team.

```

This manual provides a comprehensive overview of the application, including its main functions, installation instructions, usage guidelines, and example interactions.