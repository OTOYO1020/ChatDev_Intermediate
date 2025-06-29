Here's a detailed user manual for the software that calculates the sum of Manhattan distances between pairs in a grid configuration. This manual includes an introduction to the main functions, installation instructions, and usage guidelines.

```markdown
# Manhattan Distance Calculator

A Python application designed to compute the sum of Manhattan distances between pairs for various configurations of pieces placed on a grid defined by N rows and M columns.

## Main Functions

The software provides the following main functionalities:

1. **Input Handling**: 
   - Receives integers N (number of rows), M (number of columns), and K (number of pieces) from the user.
   - Validates the input to ensure that N, M, and K are positive integers and that K does not exceed N * M.

2. **Combination Precalculation**:
   - Precalculates factorials and their modular inverses to efficiently compute combinations C(n, k) in O(1) time.

3. **Distance Calculation**:
   - Computes the sum of Manhattan distances for all configurations of K pieces on an N x M grid.
   - Calculates distance costs in both row and column directions, taking into account the number of combinations for each distance.

4. **Output**:
   - Displays the total Manhattan distance modulo \(10^9 + 7\).

## Installation Instructions

To run the Manhattan Distance Calculator, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Set Up a Virtual Environment (Optional but Recommended)**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   Since there are currently no immediate dependencies, you can skip this step. However, if you wish to prepare for future enhancements, you can create a `requirements.txt` file as follows:
   ```bash
   touch requirements.txt
   ```

4. **Run the Application**:
   Ensure you have Python installed (version 3.6 or higher). You can run the application using:
   ```bash
   python main.py
   ```

## How to Use the Application

1. **Start the Application**:
   Run the `main.py` script. You will be prompted to enter the values for N, M, and K.

2. **Input Values**:
   - Enter the number of rows (N).
   - Enter the number of columns (M).
   - Enter the number of pieces (K).
   Ensure that:
   - N, M, and K are positive integers.
   - K does not exceed the total number of squares (N * M).

3. **View the Result**:
   After entering the values, the application will compute the total Manhattan distance and display the result.

## Example Usage

```plaintext
Enter N (rows): 3
Enter M (columns): 3
Enter K (pieces): 2
Total Manhattan Distance: 12
```

## Additional Information

For any issues or feature requests, please contact the development team at [support@chatdev.com].

## License

This software is licensed under the MIT License. See the LICENSE file for more details.

```

This manual provides a comprehensive guide for users to understand and utilize the Manhattan Distance Calculator effectively.