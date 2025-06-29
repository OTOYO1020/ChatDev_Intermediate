Here's a detailed user manual for the Jewel Converter application, formatted in Markdown:

```markdown
# Jewel Converter

The Jewel Converter application allows users to convert red jewels into blue jewels through a systematic process based on specified levels and conversion rates.

## Main Functions

- **Convert Jewels**: The application takes an integer N (level of the red jewel) and two integers X and Y, which represent the number of blue jewels obtained from converting a red jewel and a blue jewel, respectively. It calculates the total number of blue jewels of level 1 after processing all levels from N down to 1.

## Installation

To run the Jewel Converter application, you need to have Python installed on your machine. Follow the steps below to set up the environment and install the necessary dependencies.

### Step 1: Install Python

Make sure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).

### Step 2: Set Up a Virtual Environment (Optional)

It's a good practice to create a virtual environment for your project. You can do this using the following commands:

```bash
# Create a virtual environment
python -m venv jewel_converter_env

# Activate the virtual environment
# On Windows
jewel_converter_env\Scripts\activate
# On macOS/Linux
source jewel_converter_env/bin/activate
```

### Step 3: Install Dependencies

Create a `requirements.txt` file with the following content:

```
# Currently, there are no external dependencies required.
# You can add future dependencies like numpy or pandas if needed.
```

Then, install the dependencies using pip:

```bash
pip install -r requirements.txt
```

## How to Use the Application

### Running the Application

You can run the Jewel Converter application in two ways: through a graphical user interface (GUI) or via the command line.

### Option 1: Using the GUI

1. Run the `app.py` file to launch the GUI:

   ```bash
   python app.py
   ```

2. Enter the required values:
   - **Level of Red Jewel (N)**: Enter the integer value representing the level of the red jewel.
   - **Blue Jewels from Red Jewel (X)**: Enter the integer value for the number of blue jewels obtained from converting a red jewel.
   - **Blue Jewels from Blue Jewel (Y)**: Enter the integer value for the number of blue jewels obtained from converting a blue jewel.

3. Click the "Calculate" button to see the total number of blue jewels of level 1 displayed on the screen.

### Option 2: Using the Command Line

1. Run the `main.py` file from the command line:

   ```bash
   python main.py
   ```

2. Follow the prompts to enter the values for N, X, and Y.

3. The application will calculate and print the total number of blue jewels of level 1 in the console.

## Example Usage

- **Example Input**:
  ```
  Enter level of red jewel (N): 3
  Enter blue jewels from red jewel (X): 2
  Enter blue jewels from blue jewel (Y): 3
  ```

- **Example Output**:
  ```
  Total blue jewels of level 1: 12
  ```

## Conclusion

The Jewel Converter application provides a straightforward way to calculate the conversion of jewels based on user-defined parameters. For any issues or feature requests, please reach out to the development team.

```

This manual provides a comprehensive overview of the Jewel Converter application, including installation instructions, usage guidelines, and examples to help users effectively utilize the software.