'''
Main entry point of the application that handles user input and output.
'''
from graph import Graph
from input_handler import get_input
def main():
    towns_input = input("Enter number of towns (N): ")
    roads_input = input("Enter number of roads (M): ")
    roads_text = []
    print("Enter roads in format: A B C (enter 'done' when finished):")
    while len(roads_text) < int(roads_input):  # Limit the number of roads to M
        line = input()
        if line.lower() == 'done':
            break
        roads_text.append(line)
    if len(roads_text) != int(roads_input):  # Check if the number of roads matches M
        raise ValueError(f"Expected {roads_input} roads, but got {len(roads_text)} roads.")
    roads_input_str = "\n".join(roads_text)
    N, M, roads = get_input(towns_input, roads_input, roads_input_str)
    graph = Graph(N)
    for road in roads:
        graph.add_road(road[0], road[1], road[2])
    max_length = graph.max_road_length()
    print(f"Max Road Length: {max_length}")
if __name__ == "__main__":
    main()