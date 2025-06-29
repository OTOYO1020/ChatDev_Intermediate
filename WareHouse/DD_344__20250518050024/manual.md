Here's a detailed user manual for the software, formatted in Markdown as requested:

```markdown
# Min Cost String Formation

A Python application to calculate the minimum cost to form a target string using strings from multiple bags.

## Main Functions

The software provides the following main functionalities:

- **Input Handling**: Collects user input for the number of bags, the contents of each bag, and the target string.
- **Cost Calculation**: Computes the minimum cost required to form the target string using the strings from the bags.
- **Output Display**: Displays the minimum cost or indicates if forming the target string is impossible.

## Installation

To run this application, you need to have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Environment Dependencies

This application does not require any external libraries beyond the standard Python library. However, ensure you have Python 3.x installed.

## How to Use

1. **Clone the Repository**: If you have the code in a repository, clone it to your local machine using:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Run the Application**: Execute the main script to start the application:
   ```bash
   python main.py
   ```

3. **Input Data**: Follow the prompts to input the required data:
   - Enter the number of bags.
   - For each bag, enter the contents as a comma-separated list of strings.
   - Finally, enter the target string you wish to form.

4. **View Results**: After inputting the data, the application will calculate and display the minimum cost to form the target string. If it is impossible to form the string, it will return -1.

### Example Usage

```
Enter the number of bags: 2
Enter contents of bag 1 (comma-separated): hello,world
Enter contents of bag 2 (comma-separated): hello,there
Enter the target string: helloworld
```

**Output**: 
```
2
```

This indicates that it costs 2 yen to form the target string "helloworld" using the strings from the provided bags.

## Additional Information

- The application is designed to handle edge cases where the target string cannot be formed due to insufficient strings in the bags.
- The cost is calculated based on the number of strings used from the bags, with each string contributing a cost of 1 yen.

## Support

For any issues or questions regarding the application, please reach out to our support team at [support@chatdev.com](mailto:support@chatdev.com).

```

This user manual provides a comprehensive guide for users to understand the functionalities, installation process, and usage of the software.