Here's a detailed user manual for the Contest Rating application, formatted in Markdown:

```markdown
# Contest Rating Application

Calculate the maximum possible rating based on contest performances.

## Overview

The Contest Rating application allows users to input the number of contests and their respective performances, and calculates the maximum possible rating based on the provided performances. The rating is calculated using a specific formula that considers the sum of performances and the square root of the number of contests.

## Main Functions

- **max_rating(N: int, P: List[int]) -> float**: This function calculates the maximum rating based on the number of contests (N) and a list of performances (P). It iterates through all possible non-empty subsets of contests to find the maximum rating.

- **calculate_rating(subset: List[int]) -> float**: This helper function computes the rating for a given subset of performances using the formula:
  
  \[
  R = \frac{\text{sum of performances}}{\sqrt{\text{number of performances}}}
  \]

## Installation

To run the Contest Rating application, ensure you have Python installed on your machine. You can install the required dependencies using pip. 

### Step 1: Install Python

Download and install Python from the official website: [python.org](https://www.python.org/downloads/).

### Step 2: Install Dependencies

Open your terminal or command prompt and run the following command:

```bash
pip install math
```

(Note: The `math` module is part of the Python standard library, so no installation is needed for it. The command is included for completeness.)

## How to Use the Application

1. **Run the Application**: Execute the `main.py` file in your terminal or command prompt.

   ```bash
   python main.py
   ```

2. **Input Format**: When prompted, enter the number of contests followed by their performances in a comma-separated format. For example:

   ```
   Enter the number of contests followed by performances (comma-separated, e.g., '3,10,20,30'): 3,10,20,30
   ```

3. **Output**: The application will calculate and display the maximum rating based on the performances provided. The output will be formatted to two decimal places. For example:

   ```
   Maximum Rating: 21.91
   ```

## Error Handling

- If the number of performances does not match the specified number of contests (N), an error message will be displayed:

  ```
  Input Error: The number of performances must match N. Please ensure you enter a valid number of contests followed by their performances.
  ```

- Any unexpected errors will also be caught and displayed:

  ```
  Unexpected Error: <error message>. Please check your input format.
  ```

## Conclusion

The Contest Rating application is a simple yet powerful tool for calculating contest ratings based on performances. By following the instructions above, users can easily install and run the application to obtain their maximum ratings.

For any further questions or support, please reach out to our support team.
```

This manual provides a comprehensive guide for users to understand the functionality of the application, how to install it, and how to use it effectively.