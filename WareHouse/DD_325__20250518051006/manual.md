Here's a detailed user manual for the product printing application, formatted in Markdown as requested:

```markdown
# Product Printing Application

This application is designed to manage and calculate the maximum number of products that can be printed based on their timing constraints. It allows users to input product timings and efficiently determines how many products can be printed without overlap.

## Main Functions

1. **Input Products**: Users can input products in the format `(T_i, D_i)` where `T_i` is the entry time and `D_i` is the deadline for printing.
2. **Calculate Maximum Printable Products**: The application calculates the maximum number of products that can be printed based on the provided timings, considering a 1 microsecond charge time after each print.
3. **Error Handling**: The application includes error handling for invalid inputs, ensuring a smooth user experience.

## Installation

To set up the environment for this application, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**:
   Since there are no external dependencies at this time, you can simply ensure you have Python installed. If you decide to include any libraries in the future, you can add them to the `requirements.txt` file.

3. **Run the Application**:
   You can run the application using the following command:
   ```bash
   python main.py
   ```

## How to Use the Application

1. **Start the Application**:
   Run the `main.py` file. The application will prompt you to enter the number of products.

2. **Input Number of Products**:
   Enter a non-negative integer representing the number of products you wish to input.

3. **Input Product Timings**:
   When prompted, enter the product timings in the format `(T_i, D_i)` separated by semicolons. For example:
   ```
   1, 5; 2, 6; 3, 7
   ```

4. **View Results**:
   After entering the product timings, the application will calculate and display the maximum number of products that can be printed.

5. **Error Handling**:
   If you enter invalid data (e.g., non-integer values, mismatched counts), the application will prompt you to try again until valid input is provided.

## Example Usage

1. Start the application:
   ```
   python main.py
   ```

2. Input number of products:
   ```
   Enter number of products: 3
   ```

3. Input product timings:
   ```
   Enter products (T_i, D_i) separated by semicolons: 1, 5; 2, 6; 3, 7
   ```

4. Output:
   ```
   Max Printable Products: 3
   ```

## Conclusion

This application provides a straightforward way to manage product printing based on timing constraints. By following the instructions above, users can easily install and utilize the software to maximize their printing capabilities.
```

This manual provides a comprehensive guide for users to understand the functionality of the product printing application, how to install it, and how to use it effectively.