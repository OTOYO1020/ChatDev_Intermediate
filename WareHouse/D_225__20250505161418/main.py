'''
Main entry point for the toy train car application.
'''
from train_manager import TrainManager
def main():
    N, Q = map(int, input().split())
    if N < 1 or Q < 1:
        return  # Validate input values for N and Q
    train_manager = TrainManager(N)
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:  # Connect
            if 1 <= query[1] <= N and 1 <= query[2] <= N:
                train_manager.connect(query[1], query[2])
            else:
                print(f"Invalid connect query: {query[1]} or {query[2]} is out of bounds.")
        elif query[0] == 2:  # Disconnect
            if 1 <= query[1] <= N and 1 <= query[2] <= N:
                success = train_manager.disconnect(query[1], query[2])
                if not success:
                    print(f"Car {query[2]} was not connected to Car {query[1]}.")
            else:
                print(f"Invalid disconnect query: {query[1]} or {query[2]} is out of bounds.")
        elif query[0] == 3:  # Print connected component
            if 1 <= query[1] <= N:
                component = train_manager.print_connected_component(query[1])
                print(" ".join(map(str, component)))
            else:
                print(f"Invalid print query: {query[1]} is out of bounds.")
if __name__ == "__main__":
    main()