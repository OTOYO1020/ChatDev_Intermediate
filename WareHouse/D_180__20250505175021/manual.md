Here is the `manual.md` file for the training simulation software:

```markdown
# Training Simulation Software

Simulate the training process for Takahashi without letting him evolve.

## Quick Install

To run the training simulation, ensure you have Python installed on your machine. You can then install any necessary dependencies using the following command:

```bash
pip install -r requirements.txt
```

*Note: Ensure you have a `requirements.txt` file that lists any dependencies if needed.*

## 🤔 What is this?

This software simulates a training process for a character named Takahashi. The goal is to increase his strength (`STR`) through two training options: Kakomon Gym and AtCoder Gym, without allowing his strength to exceed a specified maximum (`Y`). The simulation tracks the experience points (`EXP`) gained during the training process.

### Main Functions

1. **Input Parameters**:
   - `X`: Initial strength of Takahashi.
   - `Y`: Maximum strength before evolution.
   - `A`: Multiplier for strength increase at Kakomon Gym.
   - `B`: Increment for strength increase at AtCoder Gym.

2. **Training Simulation**:
   - The simulation runs in a loop, calculating potential new strengths from both training options.
   - It chooses the option that maximizes experience points while keeping the strength below the maximum limit.

3. **Output**:
   - The final experience points (`EXP`) gained after the training simulation.

## 📖 How to Use

1. **Run the Application**:
   - Execute the main application file using Python:
   ```bash
   python main.py
   ```

2. **Input Values**:
   - When prompted, enter the integer values for `X`, `Y`, `A`, and `B`. For example:
     ```
     Enter X: 10
     Enter Y: 100
     Enter A: 2
     Enter B: 5
     ```

3. **View Results**:
   - After entering the values, the program will simulate the training and print the final experience points:
   ```
   Final EXP: 5
   ```

## Example

Here’s an example of how the program works:

1. Start the program:
   ```bash
   python main.py
   ```

2. Input the following values:
   ```
   Enter X: 10
   Enter Y: 100
   Enter A: 2
   Enter B: 5
   ```

3. The output will show the final experience points:
   ```
   Final EXP: 5
   ```

## Troubleshooting

- **Invalid Input**: If you enter a non-integer value, the program will prompt you to enter valid integers.
- **Performance Issues**: Ensure your Python environment is properly set up and that you are using a compatible version of Python.

## Conclusion

This training simulation software provides an engaging way to simulate character training while managing strength limits. Feel free to modify the parameters and explore different training strategies!
```

This manual provides a comprehensive overview of the software, including installation instructions, functionality, usage, and troubleshooting tips.