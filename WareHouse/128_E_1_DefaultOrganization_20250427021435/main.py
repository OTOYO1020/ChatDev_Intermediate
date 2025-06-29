# main.py

from simulation import simulate


def main():
    import sys
    input = sys.stdin.readline

    N, Q = map(int, input().split())

    intervals = []
    for _ in range(N):
        S, T, X = map(int, input().split())
        intervals.append((S, T, X))

    queries = []
    for _ in range(Q):
        D = int(input())
        queries.append(D)

    results = simulate(intervals, queries)

    for res in results:
        print(res)

if __name__ == "__main__":
    main()
