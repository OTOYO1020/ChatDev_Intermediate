'''
Main entry point for the Pigeon Management application without GUI.
'''
def main():
    import sys
    from pigeon_manager import PigeonManager
    input = sys.stdin.read
    data = input().splitlines()
    # Read N and Q
    N, Q = map(int, data[0].split())
    manager = PigeonManager(N)  # Initialize with N pigeons and N nests
    results = []
    for i in range(1, Q + 1):
        query = list(map(int, data[i].split()))
        if query[0] == 1:  # Move pigeon
            _, P, H = query
            manager.move_pigeon(P, H)
        elif query[0] == 2:  # Count nests with multiple pigeons
            count = manager.count_nests_with_multiple_pigeons()
            results.append(count)
    # Output results for all count queries
    print('\n'.join(map(str, results)))  # Minimized I/O operations
if __name__ == "__main__":
    main()