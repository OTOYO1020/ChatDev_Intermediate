'''
Main application file to run the Pigeon Nest Manager without GUI.
'''
from pigeon_nest_manager import PigeonNestManager
def main():
    # Read integers N and Q
    N, Q = map(int, input().split())
    manager = PigeonNestManager(N)
    results = []
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:  # Move pigeon
            _, P, H = query
            manager.move_pigeon(P, H)
        elif query[0] == 2:  # Count nests with multiple pigeons
            count = manager.count_multiple_pigeons()
            results.append(count)
    # Output results for all count queries
    print("\n".join(map(str, results)))
if __name__ == "__main__":
    main()