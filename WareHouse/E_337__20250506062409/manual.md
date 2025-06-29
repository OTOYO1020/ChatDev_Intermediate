Here's a detailed user manual for the bottle testing application, formatted in Markdown:

```markdown
# Bottle Testing Application

A systematic approach to identify a spoiled bottle among a given number of bottles using a minimal number of friends.

## Overview

This application allows you to determine which bottle is spoiled by utilizing a group of friends to test the bottles. Each friend will report whether they feel unwell after testing specific bottles, allowing the application to deduce which bottle is spoiled based on their responses.

## Main Functions

1. **Input Handling**: The application reads the number of bottles and the responses from friends.
2. **Bottle Distribution**: It distributes the bottles among friends using a systematic approach based on binary representation.
3. **Response Analysis**: The application analyzes the responses to determine which bottle is spoiled.
4. **Error Handling**: It gracefully handles input errors and provides informative messages.

## Installation

To run the Bottle Testing Application, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. **Install Python**: Make sure you have Python 3.6 or higher installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **Install Dependencies**: Open your terminal or command prompt and run the following command to install any required dependencies (if applicable):

   ```bash
   pip install -r requirements.txt
   ```

   Note: As of now, there are no additional dependencies required for this application.

## How to Use the Application

1. **Run the Application**: Execute the `main.py` script in your terminal:

   ```bash
   python main.py
   ```

2. **Input the Number of Bottles**: When prompted, enter the integer value representing the number of bottles (N). Ensure that N is a positive integer.

   Example input:
   ```
   5
   ```

3. **Input the Responses**: After the application distributes the bottles to friends, it will prompt you to enter a string of responses (S) consisting of '0's and '1's, where '1' indicates that the friend feels unwell after testing the assigned bottles, and '0' indicates they are fine.

   Example input:
   ```
   010
   ```

4. **View the Result**: The application will analyze the responses and print the number of the spoiled bottle. If no spoiled bottle is detected, it will inform you accordingly.

   Example output:
   ```
   3
   ```

## Error Handling

The application includes error handling for the following scenarios:

- **Empty Input**: If the input for the number of bottles is empty, an error message will be displayed.
- **Non-positive Integer**: If a non-positive integer is entered, an error message will be displayed.
- **Response Length Mismatch**: If the length of the response string does not match the number of friends, an error message will be displayed.
- **Invalid Response Characters**: If the response string contains characters other than '0' or '1', an error message will be displayed.

## Conclusion

The Bottle Testing Application is a simple yet effective tool for identifying spoiled bottles using a minimal number of friends. By following the instructions in this manual, you can easily set up and run the application to determine the spoiled bottle efficiently.

For any further inquiries or support, please contact the development team at ChatDev.
```

This manual provides a comprehensive guide for users to understand and utilize the Bottle Testing Application effectively.