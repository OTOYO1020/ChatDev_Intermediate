'''
Main entry point for the Pigeon Management application.
'''
from pigeon_manager import PigeonManager
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    # Read N and Q
    N, Q = map(int, data[0].split())
    manager = PigeonManager(N)
    results = []
    for i in range(1, Q + 1):
        query = list(map(int, data[i].split()))
        if query[0] == 1:  # Move pigeon
            _, P, H = query
            manager.move_pigeon(P, H)
        elif query[0] == 2:  # Count nests with multiple pigeons
            results.append(manager.count_multiple_pigeons())
    # Output results for all count queries
    print('\n'.join(map(str, results)))