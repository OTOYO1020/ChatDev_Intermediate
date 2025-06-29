Here's a detailed user manual for the software that implements the function `can_determine_permutation`. This manual provides an introduction to the main functions, installation instructions, and usage guidelines.

```markdown
# Permutation Checker

A Python application for determining if a unique permutation can be derived from a set of constraints represented as directed pairs.

## Quick Install

To run the application, ensure you have Python installed on your system. You can install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

## 🤔 What is this?

The Permutation Checker is designed to help users determine if a unique ordering of numbers from `1` to `N` can be established based on given constraints in the form of pairs. Each pair `(X_i, Y_i)` indicates a directed relationship where `X_i` must come before `Y_i` in the permutation.

### Main Functions

1. **Input Handling**: The application prompts the user to input the length of the sequence `N`, the number of pairs `M`, and the pairs themselves in a specified format.

2. **Graph Representation**: The application constructs a directed graph using an adjacency list based on the input pairs.

3. **Topological Sorting**: It implements a topological sorting algorithm to check if there exists a unique ordering of the elements based on the directed graph.

4. **Output**: The application returns a tuple indicating whether a unique permutation can be determined and the permutation itself if applicable.

## 📦 Dependencies

The application requires the following Python modules:
- `collections`
- `deque`
- `typing`
- `re`

These modules are part of the Python standard library, so no additional installation is required.

## 🛠️ How to Use

1. **Run the Application**: Execute the main application file `main.py` in your terminal or command prompt.

```bash
python main.py
```

2. **Input Parameters**:
   - You will be prompted to enter:
     - `N`: The length of the sequence (an integer).
     - `M`: The number of pairs (an integer).
     - `pairs`: A list of pairs in the format `(X, Y)`, separated by spaces (e.g., `(1, 2) (2, 3)`).

3. **Example Input**:
   ```
   Enter N (length of sequence): 3
   Enter M (number of pairs): 2
   Enter pairs (e.g., '(1, 2) (2, 3)'): (1, 2) (2, 3)
   ```

4. **Output**: After entering the inputs, the application will process the data and output whether a unique permutation can be determined, along with the permutation itself if applicable.

   **Example Output**:
   ```
   Unique permutation found: [1, 2, 3]
   ```

## 🧪 Testing

The application has been designed to handle various test cases, including:
- Cases with no constraints.
- Cases with maximum constraints.
- Edge cases where `N` and `M` are at their limits.

Feel free to test the application with different inputs to explore its capabilities.

## 📄 License

This software is provided as-is, without any guarantees or warranties. Use it at your own risk.

## 📞 Support

For any issues or questions, please contact the development team at support@chatdev.com.
```

This manual provides a comprehensive overview of the software, guiding users through installation, usage, and testing. It ensures that users can effectively utilize the application to determine unique permutations based on their input constraints.