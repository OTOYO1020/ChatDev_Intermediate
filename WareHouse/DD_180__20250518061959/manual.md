Here's a detailed user manual for the experience calculator application, formatted in Markdown:

```markdown
# Experience Calculator

A simple application to calculate the maximum experience (EXP) based on training parameters at two different gyms.

## Main Functions

The Experience Calculator allows users to:
- Input initial strength (STR) and evolution strength (Y).
- Specify training parameters for two gyms: Kakomon Gym (multiplier A) and AtCoder Gym (increment B).
- Calculate the maximum experience obtainable through training at both gyms.

## Quick Install

To run the Experience Calculator, ensure you have Python installed on your machine. You can install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

*Note: Currently, there are no additional dependencies required beyond Python's standard library.*

## 🤔 What is this?

The Experience Calculator simulates training at two different gyms to help users determine the maximum experience they can achieve before evolving. The application takes into account the user's initial strength and how it can be improved through training.

### Key Features:
- **Input Handling**: The application prompts users to enter their initial strength, evolution strength, and training parameters.
- **Training Simulation**: The application simulates training at Kakomon Gym and AtCoder Gym, calculating the maximum experience obtainable.
- **Immediate Evolution Check**: If the initial strength is already greater than or equal to the evolution strength, the application will return 0 as no training is needed.

## 📖 How to Use

1. **Run the Application**:
   Execute the `main.py` script in your terminal:

   ```bash
   python main.py
   ```

2. **Input Parameters**:
   You will be prompted to enter the following parameters:
   - **STR (X)**: Your initial strength.
   - **Evolution STR (Y)**: The strength required for evolution.
   - **Kakomon Gym Multiplier (A)**: The multiplier used for training at Kakomon Gym.
   - **AtCoder Gym Increment (B)**: The increment added to strength for training at AtCoder Gym.

   Example input:
   ```
   Enter STR (X): 10
   Enter Evolution STR (Y): 100
   Enter Kakomon Gym Multiplier (A): 2
   Enter AtCoder Gym Increment (B): 5
   ```

3. **View Results**:
   After entering the parameters, the application will calculate and display the maximum experience:

   ```
   Maximum Experience: 5
   ```

## Edge Cases

- If the initial strength (X) is greater than or equal to the evolution strength (Y), the application will immediately return 0, indicating no training is necessary.

## Support

For any issues or questions regarding the Experience Calculator, please reach out to our support team at support@chatdev.com.

Happy training!
```

This manual provides a comprehensive overview of the application, including installation instructions, usage guidelines, and support information, ensuring that users can easily understand and utilize the software.