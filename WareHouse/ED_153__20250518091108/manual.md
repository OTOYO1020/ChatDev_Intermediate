Here is the user manual for the Magic Points Calculator software, formatted in Markdown as requested:

```markdown
# Magic Points Calculator

A simple application to calculate the minimum Magic Points needed to reduce a monster's health to zero using various spells.

## Quick Install

To install the required dependencies, you can use pip:

```bash
pip install -r requirements.txt
```

Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

## 🤔 What is this?

The Magic Points Calculator is designed to help users determine the minimum total Magic Points required to defeat a monster by casting spells. Each spell has a specific damage value and a cost in Magic Points. The application calculates the optimal combination of spells to minimize the total Magic Points spent.

### Main Functions

- **Input Monster Health (H)**: Enter the health of the monster you want to defeat.
- **Input Spells (A)**: Provide a list of spells available to cast, represented by their damage values.
- **Input Costs (B)**: Provide a list of costs associated with each spell in terms of Magic Points.

The application will then compute the minimum Magic Points required to reduce the monster's health to zero or below.

## How to Use

1. **Run the Application**: Execute the `main.py` file in your terminal or command prompt.

   ```bash
   python main.py
   ```

2. **Input Values**:
   - When prompted, enter the monster's health (H).
   - Enter the spells (A) as a comma-separated list. For example: `10,20,30`.
   - Enter the costs (B) as a comma-separated list corresponding to the spells. For example: `5,10,15`.

3. **Check for Errors**: The application will verify that the number of spells matches the number of costs. If they do not match, an error message will be displayed.

4. **View Results**: After processing the input, the application will display the minimum Magic Points required to defeat the monster. If it's impossible to reduce the monster's health to zero with the given spells, a message will indicate this.

## Example Usage

```
Enter Monster Health (H): 50
Enter Spells (A) - comma separated: 10,20,30
Enter Costs (B) - comma separated: 5,10,15
Minimum Magic Points: 15
```

## Edge Cases

- If the monster's health (H) is already 0 or less, the application will return 0 Magic Points needed.
- If no combination of spells can reduce the monster's health to zero, the application will return -1 and inform the user.

## 📖 Documentation

For more detailed information on the code structure and algorithms used, please refer to the source code in `calculator.py` and `main.py`.

Feel free to reach out for support or suggestions on improving the application!
```

This manual provides a comprehensive overview of the Magic Points Calculator, including installation instructions, usage guidelines, and examples to help users effectively utilize the software.