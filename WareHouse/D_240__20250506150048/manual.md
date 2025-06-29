Here's a detailed user manual for the Ball Management application, formatted in Markdown as requested:

```markdown
# Ball Management Application

Efficiently manage the insertion and removal of balls in a cylinder based on their values.

## Overview

The Ball Management application allows users to track the number of balls in a cylinder. Users can input the values of the balls, and the application will automatically manage consecutive occurrences of the same value, removing them as necessary. This ensures that the count of balls is always accurate and up-to-date.

## Main Functions

- **Add Ball**: Input the value of a ball, and it will be added to the cylinder.
- **Check Consecutive Balls**: Automatically checks for and removes consecutive balls with the same value (2 or more).
- **Current Count**: Displays the current number of balls in the cylinder after each insertion.

## Installation

To run the Ball Management application, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. **Install Python**: Make sure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: If the application is hosted on a version control system like Git, clone the repository using:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

3. **Install Dependencies**: The application does not have any external dependencies beyond Python's standard library. You can run the application directly without additional installations.

## How to Use the Application

1. **Run the Application**: Open your terminal or command prompt, navigate to the directory where the application files are located, and run:
   ```bash
   python main.py
   ```

2. **Input the Number of Balls**: When prompted, enter the integer value for the number of balls you want to add to the cylinder.

3. **Input Ball Values**: For each ball, you will be prompted to enter its value. Input the integer value for each ball one at a time.

4. **View Current Count**: After each ball is added, the application will display the current count of balls in the cylinder.

5. **Repeat**: Continue entering ball values until you have added the specified number of balls.

## Example Usage

```
Enter the number of balls: 5
Enter the value of the ball: 1
Current count of balls: 1
Enter the value of the ball: 1
Current count of balls: 0
Enter the value of the ball: 2
Current count of balls: 1
Enter the value of the ball: 2
Current count of balls: 0
Enter the value of the ball: 3
Current count of balls: 1
```

In this example, when two balls with the same value are added consecutively, they are removed from the cylinder, resulting in a count of zero for those values.

## Conclusion

The Ball Management application is a simple yet effective tool for managing a collection of balls based on their values. It automatically handles the complexities of consecutive occurrences, allowing users to focus on their inputs without worrying about the underlying logic.

For any questions or support, please reach out to the development team.
```

This manual provides a comprehensive guide for users to understand the functionality of the Ball Management application, how to install it, and how to use it effectively.