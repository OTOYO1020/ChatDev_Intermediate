Here is the `manual.md` file that provides a detailed user manual for the software developed to sort a permutation array and count the number of swaps:

```markdown
# Permutation Sorter

A simple application for sorting a permutation array and counting the number of swaps required to achieve the sorted order.

## Quick Install

To run the application, you need to have Python installed on your machine. You can install the required dependencies using the following command:

```bash
pip install -r requirements.txt
```

If you prefer to leave the `requirements.txt` empty, you can simply run the application without any additional dependencies.

## 🤔 What is this?

The Permutation Sorter is designed to read a permutation of integers from standard input, sort it in ascending order, and count the number of swaps performed during the sorting process. The application ensures that the input is a valid permutation of numbers from 1 to N.

### Main Functions

1. **Input Handling**: The application reads the length of the permutation and the permutation array from the user.
2. **Validation**: It checks if the input array is a valid permutation of numbers from 1 to N.
3. **Sorting**: The application sorts the array using a swap-based method, counting the number of swaps performed.
4. **Output**: It prints the total number of swaps required to sort the array.

## How to Use

1. **Run the Application**: Execute the `main.py` file in your terminal or command prompt.

   ```bash
   python main.py
   ```

2. **Input the Length of the Permutation**: When prompted, enter the integer N, which represents the length of the permutation.

   ```
   Enter the length of the permutation (N): 5
   ```

3. **Input the Permutation Array**: Enter the permutation array as space-separated integers.

   ```
   Enter the permutation array (space-separated): 3 1 2 5 4
   ```

4. **View the Result**: After processing, the application will output the total number of swaps performed to sort the array.

   ```
   Total swaps performed: 4
   ```

## Error Handling

If the input array is not a valid permutation (i.e., it does not contain unique integers from 1 to N), the application will raise a `ValueError` and display an appropriate error message.

## Example

### Input
```
Enter the length of the permutation (N): 4
Enter the permutation array (space-separated): 4 3 2 1
```

### Output
```
Total swaps performed: 6
```

## Conclusion

The Permutation Sorter is a straightforward tool for sorting permutations and counting swaps. It is designed to be user-friendly and efficient, making it suitable for educational purposes or simple sorting tasks.
```

This manual provides a comprehensive overview of the software, including installation instructions, usage guidelines, and examples to help users understand how to interact with the application effectively.