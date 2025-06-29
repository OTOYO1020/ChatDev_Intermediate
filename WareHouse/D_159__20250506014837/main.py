'''
Main application file for the ball counting program.
'''
def count_frequencies(A):
    """Count the frequency of each integer in the array A."""
    count = {}
    for num in A:
        count[num] = count.get(num, 0) + 1
    return count
def calculate_ways(count):
    """Calculate the number of ways to choose two distinct balls with equal integers."""
    ways = 0
    for f in count.values():
        if f > 1:
            ways += f * (f - 1) // 2
    return ways
def main():
    N = int(input("Enter number of balls (N): "))
    A = list(map(int, input("Enter integers on balls (comma-separated): ").split(',')))
    count = count_frequencies(A)
    results = []
    for k in range(N):
        removed_num = A[k]
        count[removed_num] -= 1
        if count[removed_num] == 0:
            del count[removed_num]
        ways = calculate_ways(count)
        results.append(ways)
        count[removed_num] = count.get(removed_num, 0) + 1
    print("Ways to choose two distinct balls:")
    for result in results:
        print(result)
if __name__ == "__main__":
    main()