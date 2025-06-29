'''
Main entry point for the Pigeon Management application.
'''
from pigeon_manager import PigeonManager
import sys
def main():
    # Read N and Q
    N, Q = map(int, sys.stdin.readline().strip().split())
    manager = PigeonManager(N)
    results = []
    for _ in range(Q):
        query = list(map(int, sys.stdin.readline().strip().split()))
        if query[0] == 1:  # Move pigeon
            _, P, H = query
            manager.move_pigeon(P, H)
        elif query[0] == 2:  # Count nests with multiple pigeons
            results.append(manager.count_multiple_pigeons())
    # Output all results for count queries
    print('\n'.join(map(str, results)))
if __name__ == "__main__":
    main()