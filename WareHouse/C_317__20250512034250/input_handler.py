'''
Handles user input for the number of towns, number of roads, and the roads themselves.
'''
def get_input(towns_input, roads_input, roads_text):
    try:
        N = int(towns_input)
        M = int(roads_input)
        if M > N * (N - 1) // 2:  # Maximum roads in a simple undirected graph
            raise ValueError("Number of roads exceeds the maximum possible connections.")
        roads = []
        lines = roads_text.strip().split("\n")
        for line in lines:
            parts = line.split()
            if len(parts) != 3:
                raise ValueError(f"Invalid road format: '{line}'. Each road must be in the format 'A B C' where A, B, and C are integers.")
            try:
                A, B, C = map(int, parts)
                if A < 0 or A >= N or B < 0 or B >= N:
                    raise ValueError(f"Invalid town number in road: {A}, {B}. Town numbers must be between 0 and {N-1}.")
                roads.append((A, B, C))
            except ValueError:
                raise ValueError(f"Invalid road format: '{line}'. Each road must be in the format 'A B C' where A, B, and C are integers.")
        # New validation for the number of roads
        if len(roads) != M:
            raise ValueError(f"Expected {M} roads, but got {len(roads)} roads.")
        return N, M, roads
    except ValueError as e:
        raise ValueError(f"Invalid input. {str(e)}")