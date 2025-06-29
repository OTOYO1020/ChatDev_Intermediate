'''
Main application file for the front person determination.
'''
from person import find_front_person
def main():
    # Read integers N and Q from standard input
    N, Q = map(int, input().split())
    # Read the list of integers P
    P = list(map(int, input().split()))
    # Validate the length of P
    if len(P) != N:
        raise ValueError(f"The number of persons provided ({len(P)}) does not match the expected count N ({N}).")
    # Process each query
    for _ in range(Q):
        A, B = map(int, input().split())
        result = find_front_person(P, A, B)
        print(result)
if __name__ == "__main__":
    main()