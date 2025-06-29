# User Manual for Divisor Counter Application

## Overview

The Divisor Counter Application is designed to help users find how many integers from 1 to N have exactly 9 positive divisors. This application utilizes mathematical concepts to efficiently count divisors and provides both a command-line interface and a graphical user interface (GUI) for user interaction.

## Main Functions

1. **Count Divisors**: The core functionality of the application is to count the number of positive divisors of integers. The application identifies numbers with exactly 9 divisors based on specific mathematical conditions:
   - Numbers of the form \( p^8 \) (where \( p \) is a prime number).
   - Numbers of the form \( p^4 \times q \) (where \( p \) and \( q \) are distinct prime numbers).
   - Numbers of the form \( p^2 \times q^2 \) (where \( p \) and \( q \) are distinct prime numbers).

2. **User Input**: Users can input an integer \( N \) to specify the range for counting numbers with exactly 9 divisors.

3. **Output**: The application will display the count of numbers with exactly 9 divisors either in the console or through a GUI message box.

## Installation Instructions

To run the Divisor Counter Application, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. **Install Python**: Download and install Python from [python.org](https://www.python.org/downloads/).

2. **Install Dependencies**: Open your terminal or command prompt and run the following command to install any required dependencies:
   ```bash
   pip install math
   ```

3. **Download the Application**: Clone or download the repository containing the application files (`main.py`, `divisor_counter.py`, and `gui.py`).

## How to Use the Application

### Command-Line Interface

1. Open your terminal or command prompt.
2. Navigate to the directory where the application files are located.
3. Run the application using the following command:
   ```bash
   python main.py
   ```
4. When prompted, enter a positive integer \( N \) and press Enter.
5. The application will display the count of numbers with exactly 9 divisors.

### Graphical User Interface (GUI)

1. Open your terminal or command prompt.
2. Navigate to the directory where the application files are located.
3. Run the GUI application using the following command:
   ```bash
   python gui.py
   ```
4. A window will appear prompting you to enter a positive integer \( N \).
5. Enter the integer and click the "Count Divisors" button.
6. A message box will display the count of numbers with exactly 9 divisors.

## Conclusion

The Divisor Counter Application is a powerful tool for mathematical exploration and can be used for educational purposes or personal interest in number theory. Whether you prefer using the command line or a graphical interface, this application provides an easy way to engage with the fascinating world of divisors. 

For any issues or feedback, please reach out to the development team at ChatDev. Happy counting!