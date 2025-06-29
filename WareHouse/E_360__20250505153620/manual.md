Here's the `manual.md` file for the Ball Swapper application, detailing its main functions, installation instructions, and usage guidelines.

```markdown
# Ball Swapper

A simple application for simulating the swapping of balls and calculating the expected position of a black ball after a series of random swaps.

## Quick Install

To run the Ball Swapper application, you need to have Python installed on your system. You can install the required dependencies using pip. 

```bash
pip install -r requirements.txt
```

Make sure you have the following dependencies in your `requirements.txt`:

```
# requirements.txt
```

## 🤔 What is this?

The Ball Swapper application allows users to simulate the random swapping of a black ball (initially at position 0) with white balls (at positions 1 to N-1). After performing a specified number of swaps, the application calculates the expected position of the black ball and returns it in a modular arithmetic format.

### Main Functions

- **Input Handling**: The application reads two integers, N (number of balls) and K (number of swaps), from standard input.
- **Ball Swapping Logic**: The application randomly selects two distinct positions and swaps the balls at those positions for K iterations.
- **Expected Position Calculation**: After K swaps, the application calculates the expected position of the black ball and returns it as an irreducible fraction in the form of R, where \( R \times Q \equiv P \mod 998244353 \).

## How to Use

1. **Run the Application**: Execute the `main.py` script in your terminal.

   ```bash
   python main.py
   ```

2. **Input Values**: When prompted, enter the number of balls (N) and the number of swaps (K). Ensure that:
   - N is greater than or equal to 1.
   - K is greater than or equal to 0.

   Example input:
   ```
   Enter number of balls (N): 5
   Enter number of swaps (K): 10
   ```

3. **View Results**: After processing, the application will output the expected position of the black ball.

   Example output:
   ```
   Expected Position R: 123456789
   ```

## Edge Cases

- If **N = 1**, the application will always return 0 since there is only one ball.
- If **K = 0**, the expected position will also be 0 as no swaps are performed.

## 📖 Documentation

For further details on the implementation and the mathematical concepts used in the application, please refer to the source code in `ball_swapper.py` and `main.py`.

Feel free to reach out for support or suggestions for improvements!
```

This manual provides a comprehensive overview of the Ball Swapper application, ensuring users can easily understand how to install and use the software effectively.