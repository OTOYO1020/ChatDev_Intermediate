Here's a detailed user manual for the probability calculator software, formatted in Markdown as requested:

```markdown
# Probability Calculator

A simple application for calculating the probability based on the doubling logic of natural numbers.

## Quick Install

To get started with the Probability Calculator, you need to install the required dependencies. You can do this using pip:

```bash
pip install -r requirements.txt
```

Make sure you have Python installed on your system. This application is compatible with Python 3.6 and above.

## 🤔 What is this?

The Probability Calculator is designed to compute the probability of how many times a natural number must be doubled until it reaches or exceeds a given threshold. The main functionality revolves around two integers, N and K, where:

- **N**: The number of natural numbers to consider (from 1 to N).
- **K**: The threshold value that the numbers will be compared against.

The application calculates the probability based on the doubling logic and outputs the result.

## 📖 Main Functions

### 1. `num_twice(A, K)`

This function takes two natural numbers, A and K, as arguments and returns how many times A must be doubled until it becomes greater than or equal to K.

**Parameters:**
- `A`: A natural number (the starting point).
- `K`: A natural number (the threshold).

**Returns:**
- An integer representing the number of times A must be doubled.

### 2. `calculate_probability(N, K)`

This function calculates the overall probability based on the doubling logic for all natural numbers from 1 to N.

**Parameters:**
- `N`: The upper limit of natural numbers to consider.
- `K`: The threshold value.

**Returns:**
- A float representing the calculated probability.

## 🛠️ How to Use

1. **Run the Application:**
   To run the application, execute the `main.py` file. You can do this from the command line:

   ```bash
   python main.py
   ```

2. **Input Values:**
   The application will prompt you to enter two integers:
   - First, enter the value for N (must be a natural number greater than 0).
   - Second, enter the value for K (must also be a natural number greater than 0).

3. **Output:**
   After processing the inputs, the application will output the calculated probability. The output will be formatted as an integer if it is a whole number, or with six decimal places if it is not.

## 🚀 Example Usage

```bash
$ python main.py
5
10
```

**Output:**
```
0.312500
```

In this example, the user inputs `5` for N and `10` for K, and the application calculates the probability based on the defined logic.

## 📄 Error Handling

The application includes basic error handling for invalid inputs:
- If N or K is less than or equal to 0, a `ValueError` will be raised with an appropriate message.

## 📚 Additional Resources

For more information on Python programming and mathematical concepts related to probability, consider checking out:
- [Python Official Documentation](https://docs.python.org/3/)
- [Probability Theory Basics](https://en.wikipedia.org/wiki/Probability)

Feel free to reach out for support or suggestions to improve the application!
```

This manual provides a comprehensive overview of the software, including installation instructions, main functions, usage examples, and error handling. Let me know if you need any further modifications or additional information!