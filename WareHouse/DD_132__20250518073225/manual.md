Here is the `manual.md` file for the Ball Arrangement Calculator software:

```markdown
# Ball Arrangement Calculator

A tool for calculating the number of arrangements of balls based on combinatorial methods.

## Introduction

The Ball Arrangement Calculator allows users to compute the number of arrangements of balls consisting of blue and red balls. The main function, `countArrangements(N: int, K: int)`, calculates the number of ways to arrange K blue balls and N-K red balls, ensuring that the arrangements can be collected in exactly i moves for each i from 1 to K.

## Main Functions

- **countArrangements(N: int, K: int) -> List[int]**: 
  - Computes the number of arrangements of N balls consisting of K blue and N-K red balls.
  - Returns a list containing the number of arrangements for each move count from 1 to K.
  - Utilizes combinatorial methods and dynamic programming to ensure efficiency.
  - Results are computed modulo \(10^9 + 7\) to handle large numbers.

## Installation

To run the Ball Arrangement Calculator, you need to have Python installed on your system. You can install the required dependencies using pip. 

### Step 1: Install Python

Make sure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).

### Step 2: Install Dependencies

Open your terminal or command prompt and run the following command:

```bash
pip install -r requirements.txt
```

**Note**: If you don't have a `requirements.txt` file, you can simply run the application as it does not have external dependencies.

## How to Use

1. **Run the Application**: 
   - Navigate to the directory where the `main.py` file is located.
   - Execute the following command:

   ```bash
   python main.py
   ```

2. **Input Values**:
   - When prompted, enter the total number of balls (N) and the number of blue balls (K).
   - Ensure that K is less than or equal to N and both values are non-negative.

3. **View Results**:
   - The application will output the number of arrangements for each move count from 1 to K.

## Example Usage

```plaintext
Enter N (Total Balls): 5
Enter K (Blue Balls): 3
Arrangements: [10, 30, 60]
```

In this example, with 5 total balls and 3 blue balls, the calculator outputs the number of arrangements for each move count from 1 to 3.

## Testing

To ensure correctness and efficiency, you can test the function with various inputs. The implementation handles edge cases, such as when K is 0 or K is greater than N.

## Conclusion

The Ball Arrangement Calculator is a powerful tool for combinatorial calculations involving arrangements of colored balls. By following the instructions above, you can easily set up and use the software to compute arrangements based on your needs.
```

This manual provides a comprehensive overview of the software, including installation instructions, usage guidelines, and examples to help users effectively utilize the Ball Arrangement Calculator.