Here's a detailed user manual for the Atcoder Swapper application, formatted in Markdown as requested:

```markdown
# Atcoder Swapper

Transforming permutations of 'atcoder' into the target string through adjacent swaps.

## Quick Install

To run the Atcoder Swapper application, ensure you have Python installed on your system. You can install the necessary dependencies using pip:

```bash
pip install -r requirements.txt
```

## 🤔 What is Atcoder Swapper?

The Atcoder Swapper is a Python application designed to calculate the minimum number of adjacent swaps required to transform any permutation of the string "atcoder" into the target string "atcoder". This application is useful for understanding string manipulation and adjacent swapping algorithms.

## 📦 Main Functions

The Atcoder Swapper consists of two main files:

1. **main.py**: The entry point of the application that handles user input and displays the result.
2. **swap_logic.py**: Contains the logic for counting the number of swaps needed to rearrange the input string into the target string.

### How It Works

- The application reads an input string `S` from the user.
- It checks if `S` is a valid permutation of "atcoder".
- It calculates the number of adjacent swaps required to rearrange `S` into "atcoder".
- Finally, it prints the minimum number of swaps needed.

## 🛠️ How to Use

1. **Run the Application**:
   Open your terminal or command prompt and navigate to the directory containing the `main.py` file. Run the following command:

   ```bash
   python main.py
   ```

2. **Input a Permutation**:
   When prompted, enter a permutation of the string "atcoder". For example, you can enter "tcdoare" or "atcoder" itself.

3. **View the Result**:
   After entering the permutation, the application will calculate and display the minimum number of adjacent swaps required to transform your input into "atcoder".

## 📜 Example Usage

```bash
$ python main.py
Enter a permutation of 'atcoder': tcdoare
Minimum swaps required: 5
```

## 🚨 Error Handling

If the input string is not a valid permutation of "atcoder", the application will raise an error:

```bash
$ python main.py
Enter a permutation of 'atcoder': hello
Error: Input string must be a permutation of 'atcoder'.
```

## 📖 Documentation

For more details on the implementation and logic, refer to the source code in `swap_logic.py`. The code is well-commented to help you understand the underlying algorithms.

## 🤝 Support

If you encounter any issues or have questions about the Atcoder Swapper, please reach out to our support team at support@chatdev.com.

Happy swapping!
```

This manual provides a comprehensive overview of the Atcoder Swapper application, including installation instructions, usage guidelines, and error handling. Let me know if you need any further modifications or additional information!