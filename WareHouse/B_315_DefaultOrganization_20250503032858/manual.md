Here is the `manual.md` file that provides a detailed user manual for the software developed to calculate the middle day of the year based on user input:

```markdown
# Middle Day Calculator

A simple application to calculate the middle day of the year based on the number of days in each month.

## Overview

This software allows users to input the number of months and the corresponding number of days in each month. It then calculates the total number of days in the year and determines the middle day, outputting the month and day.

## Main Functions

- **Input Handling**: The application prompts the user to enter the number of months and the number of days in each month, ensuring valid input.
- **Calculation**: It computes the total number of days in the year and identifies the middle day based on the input data.
- **Output**: The result is displayed in a user-friendly format indicating the month and day of the middle day.

## Installation

To run the application, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. **Install Python**: Download and install Python from [python.org](https://www.python.org/downloads/).

2. **Set Up a Virtual Environment (Optional but Recommended)**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**: Create a `requirements.txt` file with the following content (if you have additional dependencies in the future, add them here):
   ```
   # Currently, there are no external dependencies required for this application.
   ```

   Then, install the dependencies using:
   ```bash
   pip install -r requirements.txt
   ```

## How to Use

1. **Run the Application**:
   Execute the main application file using Python:
   ```bash
   python main.py
   ```

2. **Input Data**:
   - When prompted, enter the number of months (M).
   - For each month, input the number of days (D_i) when prompted.

3. **View Results**:
   After entering all the data, the application will calculate and display the middle day in the format:
   ```
   Middle Day: Month X, Day Y
   ```

## Example Usage

```
Enter number of months: 12
Days in month 1: 31
Days in month 2: 28
Days in month 3: 31
Days in month 4: 30
Days in month 5: 31
Days in month 6: 30
Days in month 7: 31
Days in month 8: 31
Days in month 9: 30
Days in month 10: 31
Days in month 11: 30
Days in month 12: 31
Middle Day: Month 7, Day 16
```

## Support

For any issues or questions, please reach out to our support team at [support@chatdev.com](mailto:support@chatdev.com).

Thank you for using the Middle Day Calculator!
```

This manual provides a comprehensive guide for users to understand the software's functionality, installation process, and usage instructions.