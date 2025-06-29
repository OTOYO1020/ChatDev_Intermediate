```markdown
# Card Hitting Cost Calculator

This software calculates the minimum cost required to ensure that all cards are "hit" based on given constraints. The constraints define relationships between cards in terms of their parity (even or odd).

## Main Functions

1. **Input Reception and Initialization**: The software reads integers N (number of cards) and M (number of constraints) from standard input, followed by M constraints in the form of (X_i, Y_i, Z_i).

2. **Condition Parity Conversion**: It converts the constraints to a parity-based format, treating card values as 0 (even) or 1 (odd).

3. **Constraint Graph Construction**: Constructs an undirected graph based on the constraints, where each edge represents an XOR-constrained relationship.

4. **Union-Find Structure**: Implements a Union-Find data structure to manage connected components of cards based on the constraints.

5. **Grouping by Constraint Propagation**: Applies the constraints to the Union-Find structure to group cards.

6. **Cost Calculation**: Determines the minimum number of cards that need to be investigated to deduce the values of all cards.

7. **Output Processing**: Outputs the calculated minimum cost as an integer.

## Installation Instructions

To set up the environment for the Card Hitting Cost Calculator, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**:
   Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

   Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

   Note: If `requirements.txt` is empty, you can proceed without installing additional packages.

## How to Use the Software

1. **Run the Application**:
   Execute the main application file:
   ```bash
   python main.py
   ```

2. **Input Format**:
   - First, enter the integer N (number of cards).
   - Second, enter the integer M (number of constraints).
   - Then, for each constraint, enter three integers (X_i, Y_i, Z_i) on a new line:
     - X_i and Y_i are the indices of the cards (1-based).
     - Z_i is the parity condition (0 or 1).

   Example input:
   ```
   5
   3
   1 2 0
   2 3 1
   4 5 0
   ```

3. **Output**:
   The program will output the minimum cost required to ensure that all cards are hit. The output will be displayed in the console.

   Example output:
   ```
   Minimum Cost: 3
   ```

## Additional Information

For any issues or questions regarding the software, please refer to the code comments or reach out to the development team.

Happy coding!
```