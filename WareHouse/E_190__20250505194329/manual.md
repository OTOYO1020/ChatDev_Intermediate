Here is the `manual.md` file that provides a detailed user manual for the gem adjacency application, including installation instructions, main functions, and usage guidelines.

```markdown
# Gem Adjacency Application

The Gem Adjacency Application allows users to manage and analyze gem types based on their adjacency relationships. This application constructs an undirected graph from user input and determines if a valid sequence of required gem types can be formed.

## Main Functions

1. **Graph Construction**: 
   - The application reads integers representing the number of gem types and the number of adjacency pairs.
   - It constructs an undirected graph where each gem type is a node, and edges represent adjacency.

2. **Connected Components Identification**: 
   - The application uses Depth-First Search (DFS) to identify connected components in the graph.

3. **Validation of Required Gems**: 
   - For each connected component, the application checks if it contains all required gem types specified by the user.

4. **Minimum Gems Calculation**: 
   - If a valid sequence can be formed, the application calculates the minimum number of gems needed.

5. **User Interaction**: 
   - The application provides a console interface for user input and displays results clearly.

## Installation Instructions

To run the Gem Adjacency Application, you need to set up your environment with the required dependencies. Follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   Ensure you have `pip` installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

## How to Use the Application

1. **Run the Application**:
   Execute the main script to start the application:
   ```bash
   python main.py
   ```

2. **Input Data**:
   - You will be prompted to enter the number of gems (N) and the number of edges (M).
   - Enter M pairs of integers representing the adjacency relationships between gems.
   - Input the number of required gems (K) followed by K unique integers representing the required gem types.

3. **View Results**:
   - After processing the input, the application will display either the minimum number of gems needed to form a valid sequence or indicate that it is not possible.

## Example Usage

```plaintext
Enter number of gems (N) and number of edges (M): 5 4
Enter the edges (A B) one per line:
1 2
2 3
3 4
4 5
Enter number of required gems (K): 3
Enter the required gems (C1 C2 ...): 1 3 5
Minimum gems needed: 5
```

## Additional Notes

- Ensure that the gem types and edges you input are valid according to the constraints (1 ≤ gem type ≤ N).
- The application will prompt you for input until valid data is provided, ensuring a smooth user experience.

For further assistance or feature requests, please contact the development team.
```

This manual provides a comprehensive overview of the application, ensuring users can easily understand how to install and use it effectively.