Here's a detailed user manual for the travel time calculator software using Dijkstra's algorithm, formatted in Markdown:

```markdown
# Travel Time Calculator

A Python application for calculating the shortest travel time between cities using Dijkstra's algorithm.

## Main Functions

The Travel Time Calculator allows users to:
- Input the number of cities and travel parameters.
- Enter a matrix representing travel times between cities.
- Calculate the minimum time required to travel from the starting city to the destination city using two transportation methods: company car and train.
- Output the minimum travel time.

## Installation

To run the Travel Time Calculator, ensure you have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

### Environment Dependencies

You will need the following Python packages:
- `heapq` (part of the standard library, no installation required)
- `math` (part of the standard library, no installation required)

No additional dependencies are required beyond Python's standard library.

## How to Use

1. **Clone the Repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Run the Application**:
   Execute the main application file `main.py` using Python:
   ```bash
   python main.py
   ```

3. **Input Parameters**:
   When prompted, enter the integers `N`, `A`, `B`, and `C` separated by spaces:
   - `N`: Number of cities.
   - `A`: Time multiplier for the company car.
   - `B`: Time multiplier for the train.
   - `C`: Fixed time cost for using the train.

   Example input:
   ```
   Enter N, A, B, C: 4 2 3 5
   ```

4. **Input Travel Times Matrix**:
   Enter the travel times between each pair of cities in a matrix format. Each row should contain `N` integers representing the travel times from the current city to all other cities.

   Example input:
   ```
   Enter the travel times matrix (size 4x4):
   0 10 15 20
   10 0 35 25
   15 35 0 30
   20 25 30 0
   ```

5. **View Results**:
   After entering the data, the application will calculate and display the minimum time required to travel from city 1 to city N.

   Example output:
   ```
   Minimum time from city 1 to city 4: 40
   ```

## Example Usage

Here’s a complete example of how to use the Travel Time Calculator:

1. Start the application:
   ```bash
   python main.py
   ```

2. Input the parameters:
   ```
   Enter N, A, B, C: 4 2 3 5
   ```

3. Input the travel times:
   ```
   Enter the travel times matrix (size 4x4):
   0 10 15 20
   10 0 35 25
   15 35 0 30
   20 25 30 0
   ```

4. View the result:
   ```
   Minimum time from city 1 to city 4: 40
   ```

## Conclusion

The Travel Time Calculator is a powerful tool for determining the shortest travel time between cities using different transportation methods. By following the steps outlined in this manual, users can easily set up and utilize the application for their travel planning needs.
```

This manual provides a comprehensive guide for users to understand the software's functionality, installation steps, and usage instructions.