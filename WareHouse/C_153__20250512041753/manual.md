Here is the `manual.md` file for the Monster Attack program, detailing the main functions, installation instructions, and usage guidelines.

```markdown
# Monster Attack Program

A simple application to calculate the minimum number of attacks needed to defeat monsters based on their health and the use of special moves.

## Main Functions

The Monster Attack program includes the following key functionalities:

- **Calculate Minimum Attacks**: The core function `minimum_attacks(N: int, K: int, H: List[int]) -> int` computes the minimum number of attacks required to defeat all monsters given their health and the maximum number of special moves allowed.
  
- **Input Handling**: The program reads the number of monsters, the special move limit, and the health of each monster from standard input.

- **Output Result**: After computation, the program outputs the minimum number of attacks needed.

## Installation

To run the Monster Attack program, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. **Clone the Repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**:
   Ensure you have the required dependencies. You can install them using pip:
   ```bash
   pip install typing
   ```

3. **Run the Program**:
   You can run the program directly using Python:
   ```bash
   python main.py
   ```

## How to Use

1. **Input the Number of Monsters**: When prompted, enter the total number of monsters (N).

2. **Input the Special Move Limit**: Enter the maximum number of special moves (K) you can use.

3. **Input Monster Healths**: Provide the health values of the monsters separated by spaces. For example:
   ```
   100 200 150
   ```

4. **View the Result**: After entering the inputs, the program will calculate and display the minimum number of attacks needed to defeat all monsters.

### Example Usage

```plaintext
Enter the number of monsters (N): 3
Enter the special move limit (K): 2
Enter the monster healths (H) separated by spaces: 100 200 150
Minimum Attacks Needed: 150
```

## Edge Cases

- If `K` is zero, the program will return `N`, as each monster will require one attack.
- If all monsters have health less than or equal to `K`, the program will determine that no attacks are needed.

## Testing

The program has been designed to handle various test cases efficiently. You can modify the input values to test different scenarios and validate the correctness of the output.

For further documentation and examples, please refer to the code comments in `main.py` and `monster_attack.py`.

```

This manual provides a comprehensive overview of the Monster Attack program, ensuring users can easily understand how to install and use the software effectively.