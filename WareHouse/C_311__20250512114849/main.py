'''
Main file to run the directed cycle detection application.
'''
from cycle_detector import CycleDetector
def main():
    '''
    Main function to execute the cycle detection.
    '''
    try:
        N = int(input("Enter number of vertices (N): "))
        edges_input = input("Enter edges (comma-separated): ")
        edges = list(map(int, edges_input.split(',')))
        # Validate that edges are in pairs
        if len(edges) % 2 != 0:
            raise ValueError("Edges must be provided in pairs (u, v).")
        cycle_detector = CycleDetector(N, edges)
        result = cycle_detector.find_directed_cycle()
        if result:
            print(f"Cycle detected: {result}")
        else:
            print("No cycle detected.")
    except ValueError as e:
        print(f"Input Error: {e}")
if __name__ == "__main__":
    main()