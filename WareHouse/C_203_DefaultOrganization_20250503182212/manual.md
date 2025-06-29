```markdown
# Taro's Travel Distance Calculator

A Python application designed to help Taro maximize his travel distance by strategically visiting friends who provide yen while considering the constraints of his journey.

## Main Functions

- **Input Handling**: The application reads the number of friends (N), the initial amount of yen (K), and a list of pairs representing each friend's village number (A_i) and the amount of yen they provide (B_i).
- **Processing Logic**: The application calculates how far Taro can travel by visiting friends in ascending order of their village numbers, ensuring he maximizes his travel distance based on the yen received.
- **Output Display**: The application outputs the last village Taro can reach based on his journey.

## Installation Instructions

To run the Taro's Travel Distance Calculator, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. **Install Python**: Make sure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: Clone the repository containing the application files.
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

3. **Install Dependencies**: If there are any additional dependencies, install them using pip. For this application, no external libraries are required, but ensure you have the latest version of Python.
   ```bash
   pip install -r requirements.txt  # If a requirements file is provided
   ```

## How to Use the Application

1. **Run the Application**: Navigate to the directory where the `main.py` file is located and run the application using the following command:
   ```bash
   python main.py
   ```

2. **Input Data**: Follow the prompts to enter the required data:
   - **Number of Friends (N)**: Enter the total number of friends.
   - **Initial Money (K)**: Enter the initial amount of yen Taro has.
   - **Friends' Data**: Enter the friends' data in the format `A_i,B_i` separated by semicolons. For example:
     ```
     1,100; 2,200; 3,150
     ```

3. **View Output**: After entering the data, the application will process the information and display the last village Taro can reach based on his journey.

## Example Usage

```
Enter number of friends (N): 3
Enter initial money (K): 100
Enter friends' data (A_i, B_i) separated by semicolons (e.g., '1,100; 2,200'): 1,100; 3,200; 5,150
The last village Taro can reach is: 205
```

## Conclusion

This application provides a simple yet effective way for users to understand how Taro can maximize his travel distance by visiting friends and collecting yen. For any issues or feature requests, please contact the support team.

```
