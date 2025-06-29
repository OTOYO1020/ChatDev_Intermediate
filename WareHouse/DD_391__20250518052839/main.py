'''
Main entry point for the block simulation application.
'''
from block_simulator import BlockSimulator
from input_handler import InputHandler
def main():
    # Sample input for testing
    N = 5
    W = 5
    blocks = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]
    Q = 3
    queries = [(0, 1), (1, 2), (2, 3)]
    # Validate and process input
    blocks, queries = InputHandler.get_input(N, W, blocks, Q, queries)
    # Create a BlockSimulator instance
    simulator = BlockSimulator(N, W, blocks, Q, queries)
    # Execute queries and get results
    results = []
    for index, time in queries:
        if index < len(simulator.blocks):  # Ensure the index is valid after simulation
            results.append(simulator.block_exists(index, time))
        else:
            results.append("NO")  # If index is out of bounds, return "NO"
    # Print results
    for result in results:
        print(result)
if __name__ == "__main__":
    main()