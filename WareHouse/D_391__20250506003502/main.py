'''
Main entry point for the block simulation application.
'''
from block_simulator import BlockSimulator
from block import Block
def main():
    # Read integers N, W, and Q from standard input
    try:
        N, W, Q = map(int, input("Enter N, W, Q: ").split())
        if N <= 0 or W <= 0 or Q <= 0:
            raise ValueError("N, W, and Q must be positive integers.")
    except ValueError as e:
        print(f"Input error: {e}")
        return  # Exit the program if input is invalid
    blocks = []
    # Read N pairs of integers (X_i, Y_i)
    for i in range(N):
        x, y = map(int, input(f"Enter position for block {i + 1} (X Y): ").split())
        if x < 0 or x >= W or y < 0:
            print("Error: Block position must be within the simulation width and non-negative.")
            return
        blocks.append(Block(x, y, i + 1))  # Assign a unique ID to each block
    # Create BlockSimulator instance
    simulator = BlockSimulator(blocks)
    # Validate height before simulating
    if W < max(y for _, y in blocks):
        print("Error: Simulation width must be greater than the maximum y-coordinate of the blocks.")
        return
    # Simulate the downward movement
    simulator.simulate(W)
    # Process Q queries
    results = []
    for j in range(Q):
        a, t = map(int, input(f"Enter query {j + 1} (A T): ").split())
        exists = simulator.query(a, t)
        results.append(f"Block {a} exists at time {t + 0.5}." if exists else f"Block {a} does not exist at time {t + 0.5}.")
    # Print results for each query
    for result in results:
        print(result)
if __name__ == "__main__":
    main()