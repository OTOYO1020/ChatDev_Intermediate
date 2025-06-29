Here's a detailed user manual for the railroad scheduling application, formatted in Markdown as requested:

```markdown
# Railroad Scheduling Application

This application is designed to calculate the earliest arrival time between cities using a network of railroads. It utilizes a graph representation of cities and railroads, implementing a priority queue to efficiently determine the shortest travel time based on train schedules.

## Main Functions

- **earliest_arrival_time(N, M, X, Y, railroads)**: This function calculates the earliest time to reach city Y from city X given N cities and M railroads. It takes the following parameters:
  - `N`: Number of cities.
  - `M`: Number of railroads.
  - `X`: Starting city.
  - `Y`: Destination city.
  - `railroads`: A list of tuples, each containing:
    - `A_i`: Starting city of the railroad.
    - `B_i`: Destination city of the railroad.
    - `K_i`: Departure interval of the railroad.
    - `T_i`: Travel time of the railroad.

## Installation

To run the application, you need to have Python installed on your system. Follow these steps to set up the environment:

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**:
   Since this application does not require any external libraries at this time, you can simply ensure you have Python installed. However, if you anticipate future enhancements, you may want to create a `requirements.txt` file with potential dependencies.

   If you decide to include potential future dependencies, you could also consider adding:
   ```plaintext
   # Example future dependencies
   numpy
   pandas
   ```

3. **Run the Application**:
   You can run the application by executing the following command in your terminal:
   ```bash
   python main.py
   ```

## How to Use the Application

1. **Input Frame**:
   - Upon running the application, a graphical user interface (GUI) will appear.
   - Fill in the following fields:
     - **Number of Cities (N)**: Enter the total number of cities.
     - **Number of Railroads (M)**: Enter the total number of railroads.
     - **Starting City (X)**: Enter the starting city number.
     - **Destination City (Y)**: Enter the destination city number.
     - **Railroads (A, B, K, T)**: Enter the railroads in the format `A,B,K,T`, separated by semicolons for multiple entries. For example: `1,2,10,5; 2,3,15,10`.

2. **Calculate**:
   - Click the "Calculate" button to compute the earliest arrival time.
   - The result will be displayed in a message box indicating either the earliest arrival time or that the destination is unreachable.

## Example Usage

- **Input**:
  ```
  Number of Cities (N): 3
  Number of Railroads (M): 2
  Starting City (X): 1
  Destination City (Y): 3
  Railroads (A, B, K, T): 1,2,10,5; 2,3,15,10
  ```

- **Output**:
  ```
  Earliest Arrival Time: 15
  ```

## Troubleshooting

- Ensure that all input values are positive integers.
- Each railroad entry must contain exactly four values: A, B, K, T.
- If you encounter any errors, check the input format and ensure that the cities and railroads are defined correctly.

## Conclusion

This railroad scheduling application provides a robust solution for calculating travel times between cities based on train schedules. With its user-friendly interface and efficient algorithm, it simplifies the process of planning travel routes.

For further assistance or to report issues, please contact the support team.
```

This manual provides a comprehensive overview of the application, including its functionality, installation instructions, usage guidelines, and troubleshooting tips.